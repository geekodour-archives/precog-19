from pymongo import MongoClient

# database inits
client = MongoClient('localhost', 27017)

# maindb
neatflex = client['neatflex']
moviedb = client['moviedb']

frommovies = moviedb['movies']
tomovies = neatflex['movie']

for m in frommovies.find({}):
    tomovies.insert_one(m)
