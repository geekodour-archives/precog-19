> **Note to reviewers:** Starting this project very late due to poor estimation of time.  
> I will be following a development methodology called [Readme driven development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html). I'll try to reason for everything I do in this project along the way.


## Neatflex
- A neat way to flex what movies you like.
- Precog19 internship interview project
- [Link to problem statement](https://docs.google.com/document/d/1DQkEL1ua52MXwhRnWqJ5rtJtHWOVOHqd_qkgeYMJtPo/edit)


## Timeline
- [ ] design the database schema
- [ ] write the script to run on application start to populate the database with movies
    - avoid populating if already populated
- [ ] write the web application(front-back) to show all the movies and the add the ability to be rated
- [ ] add user authentication
- [ ] move the ability to rate movies only to authenticated users
- [ ] add a method to `fetch recommended movies` for a user.
    - fetch static set of movies for now
- [ ] write the script to populate database with dummy users and their ratings
- [ ] decide on which approach to follow to build the re
- [ ] write the re
- [ ] replace `fetch recommended movies` with the re

### Getting the data
- I used the [ml-latest-small](https://grouplens.org/datasets/movielens/latest/) dataset to get the links with genere.
- 20 movies from 10 generes
    - Extract 10 random generes
    - For earch of the 10 generes
    - extract id of 20 movies under that genere
    - {
        "comedy": ['223213123','2323'],
        "comedy": ['223213123','2323'],
        "comedy": ['223213123','2323'],
        "comedy": ['223213123','2323'],
      }
    - start the scrape



# Versions
- python: 3.7.0
- pip:
