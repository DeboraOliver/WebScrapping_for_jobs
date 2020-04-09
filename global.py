"""This script intended to scrape for jobs in a few specific job pages in Brazil.
    It was my very first scrape projects and I had the chance to learn quite a lot"""

# title: Web scrapping for job. Created: February/2020. São Paulo - Brazil


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime


class WebScrapJob:
    def __init__(self, url):
        print (url)
        self.url = url

        self.uClient = uReq (self.url)
        self.page_html = self.uClient.read ()
        self.uClient.close ()  # fecha o pedido anterior qndo eu terminar

        # html parsing
        self.page_soup = soup (self.page_html, "html.parser")

        # grabs each vacancy
        self.containers = self.page_soup.findAll ("div", {"class": "element-vaga"})
        self.save ()

    def save(self):
        # csv
        self.filename = 'teste.csv'
        self.f = open (self.filename, "w")

        headers = "vaga,empresa,area,data,cidade,estado,fonte,link\n"  # csv sao definidos pelo \n
        self.f.write (headers)
        self.jobs ()


    def jobs(self):
        for container in self.containers:
            # VAGA
            self.vaga_container = container.findAll ("div", {"class": "vaga"})
            self.vaga = self.vaga_container[0].text.strip ()

            # EMPRESA
            self.empresa_container = container.findAll ("div", {"class": "vaga-company"})
            self.empresa = self.empresa_container[0].text.strip ()

            # AREA
            self.area_container = container.findAll ("p", {"class": "area"})
            self.area = self.area_container[0].text.strip ()

            # DATA
            self.data_container = container.findAll ("span", {"class": "data"})
            self.data = self.data_container[0].text.strip ()
            self.data = self.data[0:5]

            # CIDADE
            self.cidade_container = container.findAll ("p", {"class": "location2"})
            self.cidade = self.cidade_container[0].text.strip ()
            self.cidade = self.cidade.replace ("\n", "")
            self.cidade = self.cidade[-24:-6]

            # ESTADO
            self.estado_container = container.findAll ("p", {"class": "location2"})
            self.estado = self.estado_container[0].text.strip ()
            self.estado = self.estado.replace ("\n", "")
            self.estado = self.estado[-3:-1]

            #  DESCRIÇÃO
            self.atividade_container = container.findAll ("div", {"class": "vagaDesc"})
            self.atividade = self.atividade_container[0].text.strip ()
            self.atividade = self.atividade.replace ("\n", "")
            # list(set(atividade.split()))  #Isto gera uma lista com as unique words mas  nesse csv não vale a pena

            # LINK
            self.link_container = container.findAll ("div", {"class": "vagaDesc"})
            self.link = self.link_container[0].a["href"]

            fonte = "INFOJOBS"

            print ("Vaga: " + self.vaga)
            print ("Empresa:" + self.empresa)
            print ("Area: " + self.area)
            print ("Data: " + self.data)
            print ("Cidade: " + self.cidade)
            print ("Estado: " + self.estado)
            print ("Atividade: " + self.atividade)
            print ("Link: " + self.link)

            self.f.write (self.vaga + "," + self.empresa.replace (",", "|") + "," + self.area.replace (",", "|") +
                          "," + self.data + "," + self.cidade + "," + self.estado + "," + fonte + "," + self.link + "\n")
            # f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",","|") + "," + data + "," + local.replace("-",",") + "," + atividade.replace(",", "|") + "," + link + "\n")

        self.f.close ()


url = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Campo=griddate&Orden=desc&isr=4"
vagas = WebScrapJob(url)

# Tutorial
# https://www.youtube.com/watch?v=XQgXKtPSzUI
