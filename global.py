import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Tutorial
# https://www.youtube.com/watch?v=XQgXKtPSzUI

# primeira urls (77,74,70 são filtros que colocamos no site paranao temos que filtrar aqui, por enquanto)
url_infojobs_1pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Campo=griddate&Orden=desc&isr=4"
url_infojobs_2pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Page=2&Campo=griddate&Orden=desc&isr=4"
url_infojobs_3pg = "https://www.infojobs.com.br/vagas-de-emprego-analistas.aspx?Categoria=77,74,70&Page=3&Campo=griddate&Orden=desc&isr=4"

#list_urls = pd.read_table("ignore.txt")

list_urls = [url_infojobs_1pg, url_infojobs_2pg, url_infojobs_3pg]

# csv
filename = "vagas.csv"
f = open(filename, "w")
# os titulos

headers = "vaga,empresa,area,data,cidade,estado,fonte,link\n"  # csv sao definidos pelo \n
f.write(headers)

for job in list_urls:
    # pagina 2 :

    # opening upconnection, grabbing the page
    uClient = uReq(job)
    page_html = uClient.read()
    uClient.close()  # fecha o pedido anterior qndo eu terminar

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs each vacancy
    containers = page_soup.findAll("div", {"class": "element-vaga"})

    for container in containers:
        # VAGA
        vaga_container = container.findAll("div", {"class": "vaga"})
        vaga = vaga_container[0].text.strip()

        # EMPRESA
        empresa_container = container.findAll("div", {"class": "vaga-company"})
        empresa = empresa_container[0].text.strip()

        # AREA
        area_container = container.findAll("p", {"class": "area"})
        area = area_container[0].text.strip()

        # DATA
        data_container = container.findAll("span", {"class": "data"})
        data = data_container[0].text.strip()
        data = data[0:5]

        # CIDADE
        cidade_container = container.findAll("p", {"class": "location2"})
        cidade = cidade_container[0].text.strip()
        cidade = cidade.replace("\n", "")
        cidade = cidade[-24:-6]

        # ESTADO
        estado_container = container.findAll("p", {"class": "location2"})
        estado = estado_container[0].text.strip()
        estado = estado.replace("\n", "")
        estado = estado[-3:-1]

        #  DESCRIÇÃO
        atividade_container = container.findAll("div", {"class": "vagaDesc"})
        atividade = atividade_container[0].text.strip()
        atividade = atividade.replace("\n", "")
        # list(set(atividade.split()))  #Isto gera uma lista com as unique words mas  nesse csv não vale a pena

        # LINK
        link_container = container.findAll("div", {"class": "vagaDesc"})
        link = link_container[0].a["href"]

        fonte = "INFOJOBS"

        print("Vaga: " + vaga)
        print("Empresa:" + empresa)
        print("Area: " + area)
        print("Data: " + data)
        print("Cidade: " + cidade)
        print("Estado: " + estado)
        print("Atividade: " + atividade)
        print("Link: " + link)

        f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",", "|") +
                "," + data + "," + cidade + "," + estado + "," + fonte + "," + link + "\n")
        # f.write(vaga + "," + empresa.replace(",", "|") + "," + area.replace(",","|") + "," + data + "," + local.replace("-",",") + "," + atividade.replace(",", "|") + "," + link + "\n")
f.close()

# PARA RODAR: abra um cmd faça o path usando cd PycharmProjects e depois escreva
# python real.py quando chegar na pasta
