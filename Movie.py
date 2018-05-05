# -*- coding: utf-8 -*-
#pyhon2.7
#Sat 5 May
#progrming nawaf almansour
#  Create a Movie Website Project
#Content The page contains all of the required elements (title, box with art imagery, and trailer).
import webbrowser

class Movie ():

    VALID_RATINGS = ["G", "PG" , "PG-13" , "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #
        """
         the constructor method for a class.
         Booking space in memory for variables Create variables for
         the films of (name, story, picture and video trailer)
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url  = poster_image
        self.trailer_youtube_url = trailer_youtube

# function The webbrowser module includes functions to open URLs in interactive browser applications.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
