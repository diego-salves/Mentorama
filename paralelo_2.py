from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from time import time

inicio = time()

url = ["https://harrypotter.fandom.com/pt-br/wiki/Categoria:Personagens"]

def scrape(url):
    resp = requests.get(url)
    tags = BeautifulSoup(resp.text, "html5lib")
    findClass = tags.find_all("a", attrs = {"class" : "category-page__member-link"})
    names = [a["title"] for a in findClass]
    print(names)

if __name__=='__main__':
    
    p = Pool(2)
    p.map(scrape, url)
    p.terminate()
    p.join()

    print(f"Tempo total: {time() - inicio}")