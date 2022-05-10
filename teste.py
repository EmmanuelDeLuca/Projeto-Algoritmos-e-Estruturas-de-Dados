import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



class Capitais_Mundo:
    
  def __init__(self):
    self.distancia = {}
    self.infint = 9999999

  def buscando_paises(self, procura):
    with open('index.csv', 'r') as encontrar:
        for i in encontrar:
            a = i.split(',')
            if(a[0] == procura):
                return a[1]

  def dijkstra(self, grafo, inicio, chegada):
        predecessor = {}

        quantidade = grafo
        lista_aux = []
        for c in quantidade:
            self.distancia[c] = self.infint
        self.distancia[inicio] = 0

        while quantidade:
            menor_v = None
            for c in quantidade:
                if menor_v is None:
                    menor_v = c
                elif self.distancia[c] < self.distancia[menor_v]:
                    menor_v = c

            for childNode, weight in grafo[menor_v].items():
                if weight + self.distancia[menor_v] < self.distancia[childNode]:
                    self.distancia[childNode] = weight + self.distancia[menor_v]
                    predecessor[childNode] = menor_v
            quantidade.pop(menor_v)

        currentNode = chegada
        while currentNode != inicio:
            try:
                lista_aux.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Caminho não foi encontrado')
                break
        lista_aux.insert(0,inicio)
        if self.distancia[chegada] != self.infint:
            return lista_aux, self.distancia[chegada]


def main():
  st.set_page_config(page_title="Algoritmo de Dijkstra")

  st.title('Distância entre as capitais de cada país.')
  df = pd.DataFrame(
        np.random.randn(1,2)/[50,50] + [37.76, -122],
        columns=['lat', 'lon'])
  st.map(df)

  st.success("Paises e reus respectivos ID's")
  # df = pd.read_csv('index.csv')

  # st.dataframe(df, 200, 200)
  image = Image.open('foto.png')

  st.image(image, caption='Paises e reus respectivos ID')
  with st.sidebar:
    st.success("Nosso trabalho de algoritmos. \n distancia das capitais 🌍")
    st.success("O Algoritmo de Dijkstra (E.W. Dijkstra)\n é um dos algoritmos que calcula o caminho de custo mínimo entre vértices de um grafo. Escolhido um vértice como raiz da busca, este algoritmo calcula o custo mínimo deste vértice para todos os demais vértices do grafo.Ele é bastante simples e com um bom nível de performance.")
    

  
  
  st.text_input("Insira o ID do primeiro pais", key="loc1")
  st.text_input("Insira o ID do segundo pais", key="loc2")

  if st.button('Buscar'):
    cap_partida = st.session_state.loc1 # Definido pelas chaves no st.text_input
    cap_chegada = st.session_state.loc2 #'Definido pelas chaves no st.text_input
    ajuda = Capitais_Mundo()
    juncao_caminhos = ''
    #print('------- MENTOR DISTÂNCIA ENTRE 2 CAPITAIS -------')

    #IDEIA COLOCAR UMA TABELA COM OS CODIGOS DAS CAPITAIS #

    #cap_partida = input("Insira o codigo da capital de partida: ").strip()
    #cap_chegada = input("Insira o codigo da Capital que deseja desembacar: ").strip()

    inicio = cap_partida 
    fim = cap_chegada 


    with open('capitaisdist1.csv', 'r', encoding='utf-8') as leitor:
      lendo = leitor.readlines()
  
    codigo_cap =[]
    for i in lendo:
      aux = i.split(',')
      if codigo_cap.__contains__(aux[0]):
        pass
      else:
        codigo_cap.append(aux[0])
  
    dic = {}    
    for i in lendo:
      a = i.split(',')
      dic[a[0]] = {}
 
    for i in lendo:
      a = i.split(',')
      dic[a[0]][a[2]] = int(a[4])


    if not codigo_cap.__contains__(inicio) and not codigo_cap.__contains__(fim):
      print("Nenhum dos codigos inseridos existem no banco de dados.")
    elif not codigo_cap.__contains__(fim) and fim != "":
      print("A capital com codigo {}, não existe no banco de dados.".format(fim))
    elif not codigo_cap.__contains__(inicio) and inicio != "":
      print("A capital com codigo {}, não existe no banco de dados.".format(inicio))
    else:
      vertices, peso = ajuda.dijkstra(dic,inicio,fim)

      for i in range(len(vertices)):
        vertices[i] = ajuda.buscando_paises(vertices[i]).strip('\n')

      for i in range(len(vertices)):
        if(i != len(vertices) - 1):
          juncao_caminhos += vertices[i] + ' -> '
        else:
          juncao_caminhos += vertices[i]
        
    
      st.success("Distancia entre a capital do {} e a capital do {} é de {}km".format(ajuda.buscando_paises(inicio).strip('\n'), ajuda.buscando_paises(fim).strip('\n'), str(peso)))
      st.success("Capitais que serão visitadas: {}".format(juncao_caminhos))
  
if __name__ == '__main__':
    main()