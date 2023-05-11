from bs4 import BeautifulSoup  


with open("Day 45\\website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.find_all(name="p"))