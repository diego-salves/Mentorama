from bs4 import BeautifulSoup
import asyncio
from asyncio import get_event_loop
from requests import get
import nest_asyncio
from time import time

nest_asyncio.apply()

inicio = time()

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

def web_scrape():
        loop = get_event_loop()
        scrape_list = [loop.run_in_executor(None, get, url) for url in url_list]
        for scrape in scrape_list:
            resp = yield from scrape
            tags = BeautifulSoup(resp.text, "html5lib")
            title = tags.find("title")
            print(title.text)

async def main():
    loop = get_event_loop()
    loop.run_until_complete(web_scrape())

asyncio.run(main())

print(f"Total: {time() - inicio}")