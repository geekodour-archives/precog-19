import csv
from pymongo import MongoClient

# connect to the mongodb and create both database
client = MongoClient('localhost', 27017)
tempdb = client['tempdb']
moviedb = client['moviedb']

# create tempdb collections
tempmovies = tempdb['movies']

with open('data/movies.csv', newline='') as moviefile:
    moviereader = csv.reader(moviefile, delimiter=',', quotechar='|')
    for row in moviereader[1:]
        print(row)
        tempmovies.insert_one(
            {
                'name': row[1]
            }
        )

client.close()

#- title
#- thumbnal
#- image
#- year of release
#- synopsis
#- imdb rating
