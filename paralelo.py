from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from time import time

inicio = time()

def scrape(url):
    resp = requests.get(url)
    tags = BeautifulSoup(resp.text, "html5lib")
    title = tags.find("title")
    print(title.text)

if __name__=='__main__':
    
    url_list = [
        "https://harrypotter.fandom.com/pt-br/wiki/Harry_Potter",
        "https://harrypotter.fandom.com/pt-br/wiki/Hermione_Granger",
        "https://harrypotter.fandom.com/pt-br/wiki/Ronald_Weasley",
        "https://harrypotter.fandom.com/pt-br/wiki/Ginevra_Weasley",
        "https://harrypotter.fandom.com/pt-br/wiki/Sirius_Black",
        "https://harrypotter.fandom.com/pt-br/wiki/Alvo_Dumbledore",
        "https://harrypotter.fandom.com/pt-br/wiki/R%C3%BAbeo_Hagrid",
        "https://harrypotter.fandom.com/pt-br/wiki/Minerva_McGonagall",
        "https://harrypotter.fandom.com/pt-br/wiki/Tom_Riddle",
        "https://harrypotter.fandom.com/pt-br/wiki/Belatriz_Lestrange"
    ]


    p = Pool(2)
    p.map(scrape, url_list)
    p.terminate()
    p.join()

    print(f"Tempo total: {time() - inicio}")