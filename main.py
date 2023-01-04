from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.imdb.com/list/ls055592025/")
empire_website = request.text

soup = BeautifulSoup(empire_website, "html.parser")
movie_tag = soup.find_all(name="h3", class_="lister-item-header")
movie_list = []

with open("movies.txt", "w") as file:
    pass

for movie in movie_tag:
    movie_position = movie.find(class_="lister-item-index unbold text-primary").text.replace(".", ")")
    movie_name = movie.a.text
    movie_to_list = movie_position + " " + movie_name
    with open("movies.txt", "a") as file:
        file.truncate()
        file.write(movie_to_list)
        file.write('\n')
