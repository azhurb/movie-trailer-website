import fresh_tomatoes
import media

# Create a data structure

alien = media.Movie("Alien",
    "During its return to the earth, commercial spaceship Nostromo intercepts a distress signal from a distant planet.",
    "https://image.tmdb.org/t/p/w640/2h00HrZs89SL3tXB4nbkiM7BKHs.jpg",
    "https://www.youtube.com/watch?v=jQ5lPt9edzQ")

matrix = media.Movie("The Matrix",
    "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
    "https://image.tmdb.org/t/p/w640/hEpWvX6Bp79eLxY1kX5ZZJcme5U.jpg",
    "https://www.youtube.com/watch?v=oZ1-M8O70zk")

interstellar  = media.Movie("Interstellar",
    "Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
    "https://image.tmdb.org/t/p/w640/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

prometheus  = media.Movie("Prometheus",
    "A team of explorers discover a clue to the origins of mankind on Earth, leading them on a journey to the darkest corners of the universe.",
    "https://image.tmdb.org/t/p/w640/ng8ALjSDhUmwLl7vtjUWIZNQSlt.jpg",
    "https://www.youtube.com/watch?v=r-EZC5zn2Fk")

edge  = media.Movie("Edge of Tomorrow",
    "Major Bill Cage is an officer who has never seen a day of combat when he is unceremoniously demoted and dropped into combat.",
    "https://image.tmdb.org/t/p/w640/tpoVEYvm6qcXueZrQYJNRLXL88s.jpg",
    "https://www.youtube.com/watch?v=fLe_qO4AE-M")

inception  = media.Movie("Inception",
    "Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets is offered a chance to regain his old life as payment for a task considered to be impossible: \"inception\", the implantation of another person's idea into a target's subconscious.",
    "https://image.tmdb.org/t/p/w640/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0")

movies = [alien, matrix, interstellar, prometheus, edge, inception]

# Run page generator

fresh_tomatoes.open_movies_page(movies)