"""
CSAPX Project 1: Movies

Creating a dataclass to represent a Rating object.

author: Omar Ramirez Chio
"""

from dataclasses import dataclass

@dataclass
class Rating:
    """
    A class to represent the rating of a movie
    tconst: the identifier
    averageRating: the average rating of a movie
    numberOfVotes: the total number of votes for the rating
    """
    tconst: str
    averageRating: float
    numberOfVotes: int
