import csv
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


URL = "https://www.imdb.com/title/tt"

# database inits
client = MongoClient('localhost', 27017)

# tempdb
tempdb = client['tempdb']
tempdb['movies'].drop()
tempmovies = tempdb['movies']

# maindb
moviedb = client['moviedb']
moviedb['movies'].drop()
finalmovies = moviedb['movies']

# csv inits
linkfile = open('data/links.csv')
moviefile = open('data/movies.csv')

moviereader = csv.reader(moviefile, delimiter=',', quotechar='"')
linkreader = csv.reader(linkfile, delimiter=',', quotechar='"')

next(moviereader, None) # skip header row
next(linkreader, None)

for row in moviereader:
   linkinfo = next(linkreader, None)
   tempmovies.insert_one(
    {
      'year': row[1][-5:-1],
      'name': row[1][:-7],
      'genre': row[2].split('|'),
      'link': linkinfo[1]
    }
   )

genres = tempmovies.distinct('genre')[:-1]
ids = set()

for g in genres:
    links = tempmovies.find({'genre': [g]},{'link': 1}).limit(20)
    for link in [m['link'] for m in links]:
        if len(ids) < 200:
            ids.add(link)
        else:
            break

for l in list(ids):
    r = requests.get(URL+l)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    poster = soup.find('div',{'class':'poster'}).img['src']
    movie = tempmovies.find_one({'link': l})
    finalmovies.insert_one(
    {
      '_id': l,
      'year': movie['year'],
      'title': movie['name'],
      'genre': movie['genre'],
      'image': poster
    })


tempmovies.drop()
linkfile.close()
moviefile.close()
client.close()
