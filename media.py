import webbrowser

class Movie():
    """ This class provides a way to store movie info """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        """Initialises Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date


    def show_trailer(self):
        """ Plays the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
