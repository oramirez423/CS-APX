"""
CSAPX Project 1: Movies

The queries file receives the call for the method to use from the main file and
will access the dictionaries, printing the right output based on the parameters.

The methods are:
    def print_formatted_movie(mov_list: list) -> None:
        - Based on a passed in list made of movies, it will print the attributes of the movie at the given index.

    def print_formatted_rating(rat_list: list) -> None:
        - Based on a passed in list made of ratings, it will print the attributes of the ratings at the given index.

    def lookup(m_dictionary: {}, r_dictionary: {}, tconst: str) -> None:
        - Determines if a movie given its key is in both the movie and rating dictionary.
        - If it is: it will print the formatted movie and rating of the list of movies accordingly.

    def contains(m_dictionary: {}, titletype: str, name: str) -> None:
        - Creates a list of movies and will add movies to the list if they have the:
            - Correct titleType and primaryTitle contains the passed in name
        - Will then print all of the movies in the list in the correct formatting.

    def year_and_genre(m_dictionary: {}, titletype: str, year: int, genre: str):
        - Creates a list of movies and will add movies to the list if they:
            - Contain the correct titleType, and startYear and Genre matches.
        - Prints all of the movies in the list in correct formatting.

    def runtime(m_dictionary: {}, titletype: str, lower: int, upper: int):
        - Creates a list of movies and will add movies to the list if they:
            - Contains the correct titleType, and are within the range of the runtime minutes.
        _ Prints all of the movies in the list in correct formatting sorted by descending runtime and alphabetically.

    def most_votes(m_dictionary: {}, r_dictionary: {}, titletype: str, top: int):
        - Creates a list of movies and a list of ratings and will add to the lists if the movies:
            - Contain the correct titleType
        - Prints out the top number of movies specified by the user in terms of number of votes.
            - Movies are sorted in descending number of votes, and ascending alphabetically by primary title

    def top(m_dictionary: {}, r_dictionary: {}, titletype: str, number: int, lower: int, upper: int):
        - Creates a list of movies and a list of ratings and will add to the lists if the movies:
            - Contain the correct titleType and are within the range of the years given.
        - Prints out the top number of movies specified by the user in terms of ratings and number of votes.
            -Movies are sorted in increasing order of years, have to have at least 1000 votes, descending rating,
             descending number of votes, and ascending alphabetically by title.

author: Omar Ramirez Chio
"""
from timeit import default_timer as timer
import operator

def print_formatted_movie(mov_list: list) -> None:
    """
    Prints out movies in correct formatting.
    :param mov_list: the list of movies to be printed
    :return: None
    """
    print("\tIdentifier: " + str(mov_list.tconst) +
          ", Title: " + str(mov_list.primaryTitle) +
          ", Type: " + str(mov_list.titleType) +
          ", Year: " + str(mov_list.startYear) +
          ", Runtime: " + str(mov_list.runtimeMinutes) +
          ", Genres: " + str(mov_list.genres)
          )

def print_formatted_rating(rat_list: list) -> None:
    """
    Prints out ratings in correct formatting.
    :param rat_list: the list of ratings to be printed
    :return: None
    """
    print("\tIdentifier: " + str(rat_list.tconst) +
          ", Rating: " + str(rat_list.averageRating) +
          ", Votes: " + str(rat_list.numberOfVotes)
          )

def lookup(m_dictionary: {}, r_dictionary: {}, tconst: str) -> None:
    """
    Looks up movie by tconst and prints out the movie and matching rating.
    :param m_dictionary: dictionary of movies
    :param r_dictionary: dictionary of ratings
    :param tconst: the identifier for the movie and its rating
    :return: None
    """
    start = timer()
    print("processing: LOOKUP " + tconst)
    if tconst in m_dictionary and tconst in r_dictionary:
        movie = m_dictionary[tconst]
        rating = r_dictionary[tconst]
        elapsed = timer() - start
        print("\tMOVIE:", end='')
        print_formatted_movie(movie[0])
        print("\tRATING:", end='')
        print_formatted_rating(rating[0])

    else:
        print("\tMovie not found!")
        print("\tRating not found!")
        elapsed = timer() - start

    print("elapsed time (s): ", elapsed, "\n")

def contains(m_dictionary: {}, titletype: str, name: str) -> None:
    """
    Looks up a movie by its titleType and name, will append to list and print list.
    :param m_dictionary: dictionary of movies
    :param titletype: dictionary of ratings
    :param name: words in title
    :return: None
    """

    print("processing: CONTAINS", titletype, name)
    found = False
    my_list = []
    start = timer()
    for movies in m_dictionary.values():
        if titletype == movies[0].titleType and name in movies[0].primaryTitle:
            my_list.append(movies[0])
            found = True

    elapsed = timer() - start

    if found is False:
        print("\tNo match found!")

    else:
        for movie in my_list:
            print_formatted_movie(movie)
    print("elapsed time (s): ", elapsed, "\n")


def year_and_genre(m_dictionary: {}, titletype: str, year: int, genre: str) -> None:
    """
    Looks up a movie by its titleType, year, and genre and adds it to a list.
    :param m_dictionary: dictionary of movies
    :param titletype: type of title of movie
    :param year: startYear of movie
    :param genre: genre of movie
    :return: None
    """
    start = timer()
    print("processing: YEAR_AND_GENRE ", titletype, year, genre)
    found = False
    my_list = []
    for movies in m_dictionary.values():
        if titletype == movies[0].titleType:
            if year == movies[0].startYear and genre in movies[0].genres:
                my_list.append(movies[0])
                found = True

    elapsed = timer() - start
    if found is False:
        print("\tNo match found!")

    my_list.sort(key=operator.attrgetter('primaryTitle'))
    for movie in my_list:
        print_formatted_movie(movie)

    print("elapsed time (s): ", elapsed, "\n")

def runtime(m_dictionary: {}, titletype: str, lower: int, upper: int) -> None:
    """
    Looks up movies by titleType and within range of runtime minutes.
    :param m_dictionary: dictionary of movies
    :param titletype: type of title
    :param lower: lower bounds of runtime minutes
    :param upper: upper bounds of runtime minutes
    :return: None
    """
    start = timer()
    print("processing: RUNTIME ", titletype, lower, upper)
    found = False
    my_list = []
    for movies in m_dictionary.values():
        if titletype == movies[0].titleType and lower <= movies[0].runtimeMinutes <= upper:
            my_list.append(movies[0])
            found = True

    elapsed = timer() - start
    if found is False:
        print("\tNo match found!")

    my_list.sort(key=operator.attrgetter('primaryTitle'))
    my_list.sort(key=operator.attrgetter('runtimeMinutes'), reverse=True)
    for movie in my_list:
        print_formatted_movie(movie)

    print("elapsed time (s): ", elapsed, "\n")

def most_votes(m_dictionary: {}, r_dictionary: {}, titletype: str, top: int) -> None:
    """
    Looks up a movie by titleType and as well its corresponding rating. Will print out top number of movies.
    :param m_dictionary: dictionary of movies
    :param r_dictionary: dictionary of ratings
    :param titletype: type of title
    :param top: the value dictating how many of the top movies are printed
    :return: None
    """
    start = timer()
    print("processing: MOST_VOTES ", titletype, top)
    found = False
    my_list = []
    ratings_list = []
    for movies in m_dictionary.values():
        if titletype == movies[0].titleType and movies[0].tconst in r_dictionary:
            my_list.append(movies[0])
            ratings_list.append(r_dictionary.get(movies[0].tconst)[0])
            found = True

    elapsed = timer() - start
    if found is False:
        print("\tNo match found!")

    else:
        my_list.sort(key=operator.attrgetter('primaryTitle'))
        ratings_list.sort(key=operator.attrgetter('numberOfVotes'), reverse=True)

        if top > len(my_list):
            top = len(my_list)

        for i in range(top):
            print('\t\t' + str(i+1) + ". VOTES: " + str(ratings_list[i].numberOfVotes) + ", MOVIE: ", end="")
            key = ratings_list[i].tconst
            print_formatted_movie(m_dictionary[key][0])

    print("elapsed time (s): ", elapsed, "\n")

def top(m_dictionary: {}, r_dictionary: {}, titletype: str, number: int, lower: int, upper: int) -> None:
    """
    Looks up a movie by its titleType and its corresponding rating within a given range of years.
    Prints top movies of the year.
    :param m_dictionary: dictionary of movies
    :param r_dictionary: dictionary of ratings
    :param titletype: type of movie
    :param number: the number of top movies that will be printed
    :param lower: the lower bounds of the startYear of movies
    :param upper: the upper bounds of the startYear of movies
    :return:
    """
    start = timer()
    print("processing: TOP", titletype, number, lower, upper)
    movies_list = []
    for movies in m_dictionary.values():
        if titletype == movies[0].titleType and lower <= movies[0].startYear <= upper:
            if movies[0].tconst in r_dictionary:
                movies_list.append(movies[0])

    movies_list.sort(key=operator.attrgetter('primaryTitle'))
    movies_list.sort(key=operator.attrgetter('startYear'))

    while lower <= upper:
        print("\tYEAR: " + str(lower))
        ratings_list = []
        for movies in movies_list:
            if movies.startYear == lower and r_dictionary[movies.tconst][0].numberOfVotes >= 1000:
                ratings_list.append(r_dictionary[movies.tconst][0])

        if len(ratings_list) == 0:
            print("\t\tNo match found!")
            lower+=1
            elapsed = timer() - start

        else:
            ratings_list.sort(key=operator.attrgetter('numberOfVotes'), reverse=True)
            ratings_list.sort(key=operator.attrgetter('averageRating'), reverse=True)

            list_length = number
            if list_length > len(ratings_list):
                list_length = len(ratings_list)

            elapsed = timer() - start
            for i in range(list_length):
                key = ratings_list[i].tconst
                print('\t\t' + str(i + 1) + ". RATING: " + str(ratings_list[i].averageRating) + ", VOTES: " +
                      str(ratings_list[i].numberOfVotes) + ", MOVIE:", end="")
                print_formatted_movie(m_dictionary[key][0])
            lower += 1

    print("elapsed time (s): ", elapsed, "\n")
