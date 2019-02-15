from time import sleep
from flask import Flask, abort, request, jsonify, g, url_for
from bson.objectid import ObjectId
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager, UserMixin
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

application = Flask(__name__)

class ConfigClass(object):
    SECRET_KEY = 'some secret'

    MONGODB_SETTINGS = {
        'db': 'neatflex',
        'host': 'mongodb://localhost:27017/neatflex'
    }

    # Flask-User settings
    USER_APP_NAME = "NeatFlex"
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_REQUIRE_RETYPE_PASSWORD = False

application.config.from_object(__name__+'.ConfigClass')
db = MongoEngine(application)
auth = HTTPBasicAuth()


class Movie(db.Document):
    year = db.StringField()
    imdbid = db.StringField()
    title = db.StringField()
    genre = db.ListField(db.StringField())
    image = db.StringField()


class User(db.Document, UserMixin):
    # User authentication information
    username = db.StringField(default='')
    password_hash = db.StringField()

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(application.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'username': self.username})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(application.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.objects.get(username=data['username'])
        return user

class Rate(db.Document):
    movie = db.ReferenceField(Movie)
    user = db.ReferenceField(User)
    rating = db.IntField(min_val=1,max_val=5)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.objects.get(username=username_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@application.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.objects(username=username):
        abort(400) # already existing user
    user = User(username=username)
    user.hash_password(password)
    user.save()
    return (jsonify({'username': user.username}), 201, {'Location': url_for('get_user', username=user.username, _external=True)})

@application.route('/api/users/<string:username>')
def get_user(username):
    user = User.objects(username=username)
    if not user:
        abort(400)
    return jsonify({'username': user.username})

#@application.route('/api/token')
#@auth.login_required
#def get_auth_token():
#    token = g.user.generate_auth_token(600)
#    return jsonify({'token': token.decode('ascii'), 'duration': 600})

@application.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if verify_password(username, password):
        #user = User(username=username)
        #token = user.generate_auth_token(600)
        token = g.user.generate_auth_token(600)
        return jsonify({'token': token.decode('ascii'), 'duration': 600})
    else:
        abort(403)

@application.route('/api/ratemovie/<string:movieid>', methods=['POST'])
@auth.login_required
def rate_movie(movieid):
    movie = Movie.objects.get(imdbid=movieid)
    user = User.objects.get(username=g.user.username)
    rating = int(request.json.get('rating'))
    rate = Rate(movie=movie,user=user,rating=rating)
    rate.save()
    return jsonify({'data': rate})

@application.route('/api/recommend/', methods=['GET'])
@auth.login_required
def get_reco():
    # RE goes here
    user = User.objects.get(username=g.user.username)
    return jsonify({'data': 'nothing'})

@application.route('/api/movies/<int:page>', methods=['GET'])
def get_movies(page):
    offset = 10
    movies = Movie.objects[offset*page:(offset*page+offset)]
    return jsonify({'data': movies})

if __name__ == "__main__":
    application.run(host='localhost')
