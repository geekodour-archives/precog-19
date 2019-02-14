import csv
from pymongo import MongoClient


# database inits
client = MongoClient('localhost', 27017)
moviedb = client['moviedb']

# tempdb
tempdb = client['tempdb']
tempdb['movies'].drop()
tempmovies = tempdb['movies']

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
      'genere': row[2].split('|'),
      'link': linkinfo[1]
    }
   )

# get 10 unique generes
# get 20 movies from each genere
# use requests

tempdb['movies'].drop()
linkfile.close()
moviefile.close()
client.close()

#- title
#- thumbnal
#- image
#- year of release
#- synopsis
#- imdb rating
