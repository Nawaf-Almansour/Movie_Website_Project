import fresh_tomatoes # call class fresh_tomatoes
import Movie # call class Movie

#Add information to movies
toy_story = Movie.Movie("Toy Stoury",
                       "A story of a boy and hid toys",
                       "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie.Movie("avatar",
                       "A story of a boy and hid toys",
                       "http://www.labartravenna.com/wp-content/uploads/2017/08/avatar-locandina.jpg",
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = Movie.Movie("school of rock",
                       "chool of Rock is a 2003 comedy film",
                       "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                       "https://www.youtube.com/watch?v=3PsUJFEBC74")


school_of_rock = Movie.Movie("school of rock",
                       "chool of Rock is a 2003 comedy film",
                       "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                       "https://www.youtube.com/watch?v=3PsUJFEBC74")



#print(toy_story.storyline)
#toy_story.show_trailer()

#list movies
movies = [toy_story , avatar , school_of_rock ]
fresh_tomatoes.open_movies_page(movies)
