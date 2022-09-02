# Author: Ertuğrul Demir
# This application should use for https://yordle.pages.dev
from ast import Try
from distutils.log import error
from logging import exception
from unicodedata import name
from matplotlib.pyplot import show
import requests
from bs4 import BeautifulSoup

from champion import Champion
from letter import Letter

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
    inputValue = int(input("Enter the number of boxes  >"))
    Champions = short_by_len(Champions, inputValue)
    length = inputValue
    letters = []
    while(inputValue != "0" ):
        show_champions(Champions)
        
        while(True):
            inputValue , letterIndex , letterType  = input("(Enter ,, if want stop to enter letter) Enter color (green,yellow,gray) for type of letters and the letter with index. (Ex. >A,2,green) >").lower().split(",")
            if error_check( inputValue , int(letterIndex) , letterType, length):
                break
            if inputValue == "" :
                break
            letters.append(Letter(inputValue, int(letterIndex)-1, letterType)) #User enter the index 1,2,3 but we store 0,1,2
        
        inputValue = input("Enter 0 for exit")


if __name__ == '__main__':
    app()

