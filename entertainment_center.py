import media
# Calls the media.py that contains the class Movie that will be used to create the instances.
import fresh_tomatoes


forrest_gump = media.Movie("Forrest Gump",
                         "A story of an extraordinary man that never forgot his childhood love",
                         "http://static.tvtropes.org/pmwiki/pub/images/Forrest_Gump_on_a_bench_4829.jpg",
                         "https://www.youtube.com/watch?v=bLvqoHBptjg")


great_gatsby = media.Movie("The Great Gatsby",
                          "A man that is drawn into the captivating world of the wealthy and witness illusions and deceits",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcRHjdRa754KlBw3wFJaa8pxGHbESpYGpN2Pt0A63Wgseu2f42Jd",
                          "https://www.youtube.com/watch?v=rARN6agiW7o")

sword_fish = media.Movie("Swordfish",
                        "A world beneath what we call cyberspace",
                        "http://www.gstatic.com/tv/thumb/movieposters/27850/p27850_p_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=mfLizCqjz18")


black_hawk = media.Movie ("Black Hawk Down",
                         "A battle between forces of the United States and Somali militia fighters",
                         "https://cdn.traileraddict.com/content/columbia-pictures/blackhawkdown-3.jpg",
                         "https://www.youtube.com/watch?v=AUJ6cxWdZwA")

constantine = media.Movie("Constantine",
                          "A suicide survivor that had been to hell and back",
                          "http://www.gstatic.com/tv/thumb/movieposters/35545/p35545_p_v8_ad.jpg",
                          "https://www.youtube.com/watch?v=DEa508Xmmio")

Inception = media.Movie("Inception",
                        "A thief with the ability to enter people's dreams and steal their secrets",
                        "https://s-media-cache-ak0.pinimg.com/736x/ff/39/f4/ff39f498bc72f9368a92630b680c195b--minion-movie-minions-despicable-me.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


movies = [forrest_gump, great_gatsby, sword_fish, black_hawk, constantine, Inception]
# List of movie instances.
fresh_tomatoes.open_movies_page(movies)
# Open browser and shows the list movies.


