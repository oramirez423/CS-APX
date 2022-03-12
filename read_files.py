"""
CSAPX Project 1: Movies

A program that takes in a filename and puts the contents of the file in a dictionary with the key
being the tconst, and the value being either a Movie or Rating object.

The methods are:
    def read_movies_data(filename: str) -> dict:
        -Given the filename, it will read in the data and put it in the movies dictionary.

    def read_ratings_data(filename: str) -> dict:
        -Given the filename, it will read in data and put it in the ratings dictionary.

author: Omar Ramirez Chio
"""
from movie_dataclass import Movie
from rating_dataclass import Rating

def read_movies_data(filename: str) -> dict:
    """
    Reads in a file and puts its content into a dictionary.
    :param filename: the file
    :return: the dictionary
    """
    movies = {}
    with open(filename, encoding='utf-8') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            line = line.split("\t")

            if line[4] == '1':
                continue
            else:
                if line[5] == "\\N":
                    line[5] = 0
                if line[6] == "\\N":
                    line[6] = 0
                if line[7] == "\\N":
                    line[7] = 0
                if line[8] == "\\N":
                    line[8] = None
                movies_list = [Movie(
                    tconst=str(line[0]),
                    titleType=str(line[1]),
                    primaryTitle=str(line[2]),
                    originalTitle=str(line[3]),
                    isAdult=int(line[4]),
                    startYear=int(line[5]),
                    endYear=int(line[6]),
                    runtimeMinutes=int(line[7]),
                    genres=str(line[8])
                )]
                movies[line[0]] = movies_list

    return movies

def read_ratings_data(filename: str, a_dict: {}) -> dict:
    """
    Reads in a file and puts the data in a dictionary.
    :param filename: the file being passed in
    :param a_dict: a dictionary of the movies
    :return: ratings dictionary
    """
    ratings = {}
    with open(filename, encoding='utf-8') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            line = line.split("\t")
            if line[0] in a_dict:
                rating_list = [Rating(
                    tconst=str(line[0]),
                    averageRating=float(line[1]),
                    numberOfVotes=int(line[2])
                )]
                ratings[line[0]] = rating_list
            else:
                continue

    return ratings



