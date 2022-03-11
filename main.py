# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
from pprint import pprint

import requests



class Superhero:
    pre_href = "https://superheroapi.com/api/2619421814940190/"
    def __init__(self, name):
        self.name = name
        self.get_id()


    def get_id(self):
        method = "search/"
        href = self.pre_href + method + self.name
        response = requests.get(href)
        res =  response.json()
        #print(type(res))

        self.id = res["results"][0]["id"]

        #print(res["results"][0]["powerstats"]["intelligence"])
        self.int = res["results"][0]["powerstats"]["intelligence"]

    def get_int(self): #Необязательная функция. Создана для тренировки requests
        method = "/powerstats/"
        href = self.pre_href + self.id +method
        #print(href)
        response = requests.get(href)
        res =  response.json()
        self.int = res["intelligence"]
    def __repr__(self):
        return self.name + " " + self.int

    # def __lt__(self, other_superhero): #сравнение супергероев по интеллекту
    #     return self.int < other_superhero.int





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    superheroes_names = ["Hulk", "Captain America", "Thanos"]
    superheroes = [Superhero(i) for i in superheroes_names]
    print(superheroes)
    super_clever = min(superheroes, key=lambda x: x.int) #max() почему-то выдавл Халка с мин интеллектом
    print(super_clever)
    #thanos = Superhero("Thanos")
    #superheroes.append(thanos)

    #thanos.get_id()
    #thanos.get_int()

    #superheroes





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
