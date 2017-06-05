import fresh_tomatoes
import media

def init_movies():
    """ Creates 6 movies and init them with their movie data """
    
    shawshank_redemption = media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_QL50_SY1000_CR0,0,672,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco",
                        "1994")
    
    martian = media.Movie("The Martian",
                          "A man is stuck on Mars",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/"
                          "The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=lQqhfq87FgY",
                          "2015")

    god_father = media.Movie("The Godfather",
                      "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,704,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=sY1S34973zA",
                      "1972")
    sound_of_music = media.Movie("The Sound of Music",
                      "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BODIxNjhkYjEtYzUyMi00YTNjLWE1YjktNjAyY2I2MWNkNmNmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL50_SX705_CR0,0,705,999_AL_.jpg",
                      "https://www.youtube.com/watch?v=OyzzifE1YGs",
                      "1965")
    dark_knight = media.Movie("The Dark Knight",
                      "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                      "2008")    
    inception = media.Movie("Inception",
                      "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=8hP9D6kZseM",
                      "2010")

    # Store the Movie objects in a list.
    movies = [shawshank_redemption, martian, god_father, sound_of_music, dark_knight, inception]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)


init_movies()
