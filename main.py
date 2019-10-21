import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import csv
import ftplib
import os
import time

def index():

   
    file = 'frases_curtas'
    ini = 1#176
    fim = 176#176

    file = 'frases_de_motivacao'
    ini = 1#176
    fim = 1800#176
    

    with open(file + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)

        linha = ['Autor', 'Frase', 'Categoria']
        spamwriter.writerow(linha)

        for p in range(ini, fim):
            #url = ('https://www.pensador.com/frases_de_motivacao/' + str(p))
            url = ('https://www.pensador.com/' + file +'/' + str(p))
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            nodes = soup.find_all("div", class_="thought-card", href=False)
            
            print("page: " + str(p))

            for node in nodes:
                #encode('utf8').
                f = node.findChildren()[0].text.strip().replace('"','')
                a = node.findChildren()[2].text.strip()
                c = file

                if a is None:
                    a = 'Autor Desconhecido'
                    
                linha = [a, f, c]
                try:    
                    spamwriter.writerow(linha)
                except UnicodeEncodeError:
                    print("Erro: " + a + ", " + f)

if __name__ == "__main__":
    index()