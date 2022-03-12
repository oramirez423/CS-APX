"""
CSAPX Project 1: Movies

A program that implements dictionaries to load in about 8 million movies and 1 million ratings from a datafile and
puts them in a dictionary with the key being a ttconst and the value being an object Movie or Rating.
Once the dictionaries are loaded in with the data, it reads input from a separate file and outputs the correct data.

The methods are:
    def printing_time_dict(filename: str, file: str):
      - It calls the read_movies_data(filename: str) and the read_ratings_data(file, movies_dict) to put it in
        a dictionary, return the dictionary, and print the total number of movies and ratings.

author: Omar Ramirez Chio
"""
import sys
from queries import *
from read_files import *
from timeit import default_timer as timer

def printing_time_dict(filename: str, file: str):
    """
    A method that takes in the files and returns dictionaries.
    :param filename: the movie datafile
    :param file: the rating datafile
    :return: both a movie and rating dictionary
    """
    start = timer()
    print("reading " + str(filename) + " into dict...")
    movies_dict = read_movies_data(filename)
    elapsed = timer() - start
    print("elapsed time (s): ", elapsed, "\n")

    start = timer()
    print("reading " + str(file) + " into dict...")
    ratings_dict = read_ratings_data(file, movies_dict)
    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")

    print('Total movies:', len(movies_dict))
    print('Total ratings:', len(ratings_dict), "\n")

    return movies_dict, ratings_dict

def main():
    """
    The main method is responsible for getting the command line argument and file,
    calling the printing_time_dict method,
    and deciding on which query method to call depending on the input from a separate file.
    :return: None
    """

    if len(sys.argv) == 1 or sys.argv[1] == "large":
        movie_file = 'data/title.basics.tsv'
        ratings_file = 'data/title.ratings.tsv'
    elif sys.argv[1] == "small":
        movie_file = "data/small.basics.tsv"
        ratings_file = "data/small.ratings.tsv"

    movies_dict, ratings_dict = printing_time_dict(movie_file, ratings_file)

    for line in sys.stdin:
        line = line.rstrip()
        line = line.split(" ")

        query = line[0]
        if query == "LOOKUP":
            identifier = line[1]
            lookup(movies_dict, ratings_dict, identifier)

        elif query == "CONTAINS":
            title_type = str(line[1])
            movie_name = line[2:]
            movie_name = ' '.join(map(str, movie_name))
            contains(movies_dict, title_type, movie_name)

        elif query == "YEAR_AND_GENRE":
            title_type = str(line[1])
            year = int(line[2])
            genre = line[3:]
            genre = ' '.join(map(str, genre))
            year_and_genre(movies_dict, title_type, year, genre)

        elif query == "RUNTIME":
            title_type = str(line[1])
            start = int(line[2])
            end = int(line[3])
            runtime(movies_dict, title_type, start, end)

        elif query == "MOST_VOTES":
            title_type = str(line[1])
            votes = int(line[2])
            most_votes(movies_dict, ratings_dict, title_type, votes)

        elif query == "TOP":
            title_type = str(line[1])
            number = int(line[2])
            lower = int(line[3])
            upper = int(line[4])
            top(movies_dict, ratings_dict, title_type, number, lower, upper)

        else:
            print("Not a query. :|")

if __name__ == '__main__':
    main()
