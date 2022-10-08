from bs4 import BeautifulSoup
import requests
response=requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data=response.text
moviesfile=[]

soup=BeautifulSoup(data,'html.parser')
movies=soup.select(selector='div h3 ')
for moviename in movies:
    moviesfile.append(moviename.getText())
moviesfile=moviesfile[::-1]

with open('movies.txt',mode='w') as file:
    for movies in moviesfile:
        file.write(f'{movies}\n')






