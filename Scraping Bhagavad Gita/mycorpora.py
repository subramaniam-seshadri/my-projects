import requests
from bs4 import BeautifulSoup
from string import digits
import re
import codecs

def writeToCorpusFile(transliteration,translation,commentary,chapter,verse):
    chapter = str(chapter)
    verse = str(verse)
    print(translation)
    fileDetails = {"transliteration":transliteration,"translation":translation,"commentary":commentary}
    with codecs.open("Output//"+chapter+verse+".json", "w", "utf-8") as file:
        file.write(str(fileDetails))
        #file.write(transliteration+ u"\n")
        #file.write(translation+ u"\n")
        #file.write(commentary)
        file.close()


def scrape_data(url,chapter,verse):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    transliteration = ""
    commentary = ""
    translation = ""
    if(soup.find("div", {"id": "commentary"}) is not None):
        commentary = soup.find("div", {"id": "commentary"})
        commentary = commentary.find("p").text
    if(soup.find("div",{"id":"translation"}) is not None):
        translation = soup.find("div",{"id":"translation"})
        translation = translation.find("p").text
    if(soup.find("div",{"id":"transliteration"}) is not None):
        transliteration = soup.find("div",{"id":"transliteration"})
        transliteration = transliteration .find("p").text
    writeToCorpusFile(transliteration,translation,commentary,chapter,verse)

def main():
    chapVerseCountMapping = {1:47,2:72, 3:43,4:42,5:29,6:47,7:30,8:28,9:34,10:42,11:55,12:20,13:34,14:27,15:20,16:24,17:28,18:78}

    for chapter in sorted(chapVerseCountMapping):
        for verse in range(1,chapVerseCountMapping.get(chapter)+1):
            baseUrl = 'https://www.holy-bhagavad-gita.org/chapter/%d/verse/%d' % (chapter,verse)
            print(baseUrl)
            scrape_data(baseUrl,chapter,verse)

    #scrape_data('https://www.holy-bhagavad-gita.org/chapter/1/verse/1',1,1)
    print("Corpus creation succeeded")
if __name__ == '__main__': main()
