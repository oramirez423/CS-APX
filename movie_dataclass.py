"""
CSAPX Project 1: Movies

Creating a dataclass to represent a movie object.

author: Omar Ramirez Chio
"""

from dataclasses import dataclass

@dataclass
class Movie:
    """
    A class to represent a movie.
    tconst: the identifier
    titleType: movie/video game
    primaryTitle: the name
    originalTitle: the original name
    isAdult: determines whether movie is adult or not
    startYear: when the movie was first released
    endYear: when the movie stopped being released
    runtimeMinutes: length of the movie in minutes
    genres: genre of the movie
    """
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    isAdult: int
    startYear: int
    endYear: int
    runtimeMinutes: int
    genres: str
