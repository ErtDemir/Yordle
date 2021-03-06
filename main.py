# Author: Ertuğrul Demir
# This application should use for https://yordle.pages.dev
from ast import Try
from distutils.log import error
from logging import exception
from unicodedata import name
from matplotlib.pyplot import show
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

class Letter:
    def __init__(self,letter,index,type) -> None:
        self.letter = letter
        self.index = index
        self.type = type


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

def short_by_len(champions,length):
    lenSuitableChamps = []

    if length != "0":
        for Champ in champions:
            if Champ.length == length:
                lenSuitableChamps.append(Champ)
    return lenSuitableChamps



def eliminate_by_letters(champions,letters): #TODO
    newChampions = []
    for letter in letters:
        for champ in champions:
            a = 0


    return champions

def show_champions(champions):
    for champ in champions:
        print(champ.name)

def error_check( inputValue , letterIndex , letterType,length):
    if letterIndex >= length+1: 
        print("Enter invalid index")
        return True
    if letterType not in ["green","yellow","gray"]:
        print("Enter invalid color")
        return True

    

def app():
    Champions = get_champs()

    print("Enter 0 if you want exit ")
    inputValue = input("Enter the number of boxes  >")
    Champions = short_by_len(Champions, inputValue)
    length = inputValue
    letters = []
    while(inputValue != "0" ):
        show_champions(Champions)
        
        while(True):
            str_input = "(Enter ,, if want stop to enter letter) Enter color (green,yellow,gray) for type of letters and the letter with index. (Ex. >A,2,green) >"
            inputValue , letterIndex , letterType  = input(str_input).lower().split(",")
            if error_check( inputValue , letterIndex , letterType, length):
                break
            if inputValue == "" :
                break
            letters.append(Letter(inputValue, int(letterIndex)-1, letterType)) #User enter the index 1,2,3 but we store 0,1,2
        
        inputValue = input("Enter 0 for exit")


if __name__ == '__main__':
    app()

