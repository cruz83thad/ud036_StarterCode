import fresh_tomatoes
import media

# Please add your favorite movie instances for fresh_tomatoes to display

braveheart = media.Movie(
    "Braveheart",
    "When his secret bride is executed for assaulting "
    "an English soldier who tried to rape her, "
    "Sir William Wallace begins a revolt against King Edward I of England. ",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOGQ0MmEwZDMtZGM1"
    "ZC00OWRkLTllNTMtNmFmNjBlMDc0N2I3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
    "https://www.youtube.com/watch?v=nBpe_qznB2M"
    )

# Gladiator Instance
gladiator = media.Movie(
    "Gladiator",
    "When a Roman General is betrayed, and his family murdered by an "
    "emperor's corrupt son, he comes to Rome as a gladiator to seek "
    "revenge.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEt"
    "ODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0O"
    "TQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=w5rVtxWTq8w"
    )

# Goonies Instance
goonies = media.Movie(
    "The Goonies",
    "80s hit movie about Pirate Treasure",
    "http://48tx1q1rrcysi4t7l687xbtt.wpengine.netdna-cdn.com/"
    "wp-content/uploads/2016/08/Goonies_Spotlight.jpg",
    "https://www.youtube.com/watch?v=_AiKf0YfJPo"
    )

movies = [braveheart, gladiator, goonies]
fresh_tomatoes.open_movies_page(movies)

# Any __doc__ for your reading pleasure
print(media.Movie.__doc__)
