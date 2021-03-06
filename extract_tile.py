from html.parser import HTMLParser
from html.entities import name2codepoint
import sys


class Oppitunti(object):

    id = 0

    def __init__(self):
        self.__id = Oppitunti.id
        self.data = []
        Oppitunti.id += 1

    def organizeData(self):
        # print(self)
        # print(self.data)
        # self.nimi_lyhyt = self.data[0].split(' ')[0]
        # self.nimi_pitkä = self.data[0].split(' ')[1]
        self.opettaja = self.data[len(self.data) - 2]
        self.sijainti = self.data[len(self.data) - 1]
        # del self.data

    def printAttrs(self):

        for key, value in self.__dict__.items():
            print('{}: {}'.format(key, value))

    def getData(self, tag, attrs):
        self.data.append(attrs['title'])

    def getWeekday(self, tag, attrs):
        self.viikonpäivä = attrs['data-weekday']

    def ajat(self, data):
        lista = data.split(': ')
        self.alkamisaika = lista[1][11:16]
        self.päättymisaika = lista[1][29:34]
        self.nimi_lyhyt = lista[2]


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        temp = {}
        # print(attrs)
        for i in range(len(attrs)):
            temp[attrs[i][0]] = attrs[i][1]
        # print(temp)
        attrs = temp


        # viikonpäivä
        if tag == 'div' and 'data-weekday' in attrs:
            self.instance.getWeekday(tag, attrs)

        #  tunnin nimi

        if tag == 'a' and 'title' in attrs and 'class' in attrs and 'normal teachers profile-link no-underline-link' not in attrs:
            # print('asd\n\n')
            self.instance.getData(tag, attrs)

    def handle_data(self, data):
        lista = data.split(': ')

        if lista[0].lower() in ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']:
            self.instance.ajat(data)




strings = [input() for i in range(int(input()))]

objektit = [Oppitunti() for i in range(len(strings))]

for i in range(len(strings)):
    testi = Oppitunti()
    parsaaja = MyHTMLParser()

    parsaaja.instance = objektit[i]

    parsaaja.feed(strings[i])

    objektit[i].organizeData()
    objektit[i].printAttrs()

    print('\n')
