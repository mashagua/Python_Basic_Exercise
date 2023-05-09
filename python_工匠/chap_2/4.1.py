import pandas as pd
from random import randint
import random
class Movie:
    def __init__(self,name,year,rating):
        self.name=name
        self.year=year
        self.rating=rating
    @property
    def rank(self):
        rating_num=float(self.rating)
        if rating_num>=8.5:
            return 'S'
        elif rating_num>=8:
            return 'A'
        elif rating_num>=7:
            return 'B'
        elif rating_num>=6:
            return 'C'
        else:
            return 'D'

def get_sorted_movies(movies,sorting_type):
    if sorting_type=="name":
        sorted_movies=sorted(movies,key=lambda movie:movie.name.lower())
    elif sorting_type=="rating":
        sorted_movies=sorted(movies,key=lambda movie:float(movie.rating),reverse=True)
    elif sorting_type=='year':
        sorted_movies=sorted(movies,key=lambda movie:movie.year,reverse=True)
    elif sorting_type=='random':
        sorted_movies=sorted(movies,key=lambda movie:random.random())
    else:
        raise RuntimeError(f"unknown sorting type:{sorting_type}")
    return sorted_movies

import bisect

class Movie:
    def __init__(self,name,year,rating):
        self.name=name
        self.year=year
        self.rating=rating
    @property
    def rank(self):
        rating_num=float(self.rating)
        breakpoints=(6,7,8,8.5)
        grades=("D","C","B","A","S")
        index=bisect.bisect(breakpoints,float(self.rating))
        return grades[index]