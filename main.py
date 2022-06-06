# Author: Ertuğrul Demir
# This application should use for https://yordle.pages.dev
from unicodedata import name
import requests
from bs4 import BeautifulSoup

class Champion:
    def __init__(self,name) -> None:
        self.__name = name
        self.__length = str(len(name))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def length(self) -> str:
        return self.__length
    
    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    @length.setter
    def length(self,new_length):
        self.__length = new_length
    
    @name.deleter
    def name(self):
        print("Deleted the name of"+self.name)
        del self.__name

    @length.deleter
    def length(self):
        print("Deleted the length of"+self.length)


def get_champs():
    champions=[]
    vgm_url = 'https://www.leagueoflegends.com/en-gb/champions/'
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    for link in soup.find_all('a'):
        oneLink = link.get('href')
        if '/en-gb/champions/' in oneLink:
            champ_name = oneLink.split("/")[-2]
            champ_name = champ_name.replace("-","")
            champions.append(Champion(champ_name))
    
    return champions

def app():
    Champions = get_champs()
    inputValue = ""
    print("Enter 0 if you want exit anytime")
    inputValue = input("Enter the number of boxes: ")
    

    while(True):
        if str(inputValue) == "0":
            break
        
        


if __name__ == '__main__':
    app()

