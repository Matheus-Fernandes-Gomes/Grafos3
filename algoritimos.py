from os import SEEK_CUR
import numpy as np
import time
from random import randint
import copy




class algoritimos:
    # Inicializador
    def __init__(self, arquivo,tempo):
        # Classe com todos os atributos e metodos do algoritimo construtivo
        #self.morigem,self.mdestino,self.menor = self.menor(arquivo)
        #cria lista
        self.lista= []

        self.n_vertices=0
        inicio_tempo=time.time()
        self.lista,self.resu,matriz = self.constroi(arquivo)
        print("Algoritimo construtivo:")
        self.imprimi(self.lista,self.resu)
        #self.menor_no_vertice(arquivo,3)
        #2opt
        print("Algoritimo 2-OPT")
        
        caminho,menor_tamanho=self.refinamento_2opt((inicio_tempo+tempo),self.lista,matriz)
        self.imprimi(caminho,menor_tamanho)

    def imprimi(self,Lista,resu):
        print(resu)
        print(Lista)

    def constroi(self, arquivo):
        
        #lendo o cabeçalho
        header = arquivo.readline().rstrip()  
        self.n_vertices=int(header[0])
        info = header.split(' ')
        
        #percorre cada linha do arquivo
        #atribui infinito para menor 
        menor=float("inf")
        resu=0
        #partindo do menor
        vertice1,destino1,tamanho1=self.menor(arquivo)
        self.primeiro=vertice1
        resu=resu+tamanho1
        #print("ponnto1")
        #print(vertice1,destino1,tamanho1)
        self.lista.append(vertice1)
        
        while(len(self.lista)!=(self.n_vertices+1)):
            self.lista.append(destino1)
            m_destino,menor=self.menor_no_vertice(arquivo,destino1)
            #print("teste")
            #print(m_destino,menor)
            destino1=m_destino
            #resu=resu+menor
            #print("res",resu) 
        #print("***",resu)
        matriz=self.cria_matriz(arquivo)
        resu=self.custo_percuso(self.lista, matriz)
        '''
        i=0
        for i in range(5):
            print('i=',i)
            morigem,mdestino,menor=self.menor_no_vertice(arquivo,i)
            print("origem:   ",morigem,mdestino,menor)
            self.lista.append(mdestino)
            


       

        
        for header in arquivo:
            info = header.split(' ')
            origem = int(info[0])
            #testa para cada linha do vertice
            if(origem not in lista):
                morigem,mdestino,menor=self.menor_no_vertice(arquivo,origem)
                resu=resu+menor
                lista.append(morigem)'''
        return(self.lista,resu,matriz)
    

    def menor(self,arquivo):
        #atribuindo infinito a menor e garantindo que origem e destino estão vazias
        menor=float("inf")
        morigem=None
        mdestino=None
        #lendo o cabeçalho
        header = arquivo.readline()
        info = header.split(' ')
        #acha menor
        for header in arquivo:
            info = header.split(' ')
            peso = float(info[2])
            #encontra o menor
            if peso<menor:
                #substituindo pesos
                menor=peso
                #salvando o numero de vertices e arestas
                morigem=int(info[0])
                mdestino=int(info[1])
        #imprimi teste
        #print("ponto 4")
        #print(morigem,mdestino,menor)
        return (morigem,mdestino,menor)


    def menor_no_vertice(self,arquivo,vertice):
        #coloca o cursor no inicio do arquivo para
        arquivo.seek(0)
        #atribuindo infinito a menor p
        menor=float("inf")
        mdestino=0
        #lendo o cabeçalho
        header = arquivo.readline()
        info = header.split(' ')
        #acha menor
        for header in arquivo:
            info = header.split(' ')
            #salvando o numero de vertices e arestas
            origem = int(info[0])
            destino = int(info[1])
            peso = float(info[2])
            #verifica se o vertice está na listada
            if(destino not in self.lista):
                if(vertice == origem):
                    #enontra o menor 
                    if peso<menor:
                        menor=peso
                        
                        mdestino=destino
            elif(origem not in self.lista):
                if(vertice == destino):
                    if peso<menor:
                        menor=peso
                        mdestino=origem


            #print("***************")
            #print(morigem,mdestino,menor)
        if (menor ==float("inf")):
            (mdestino,menor)=self.first(arquivo,vertice)
                
        return (mdestino,menor)

    def first(self,arquivo,mdestino):
         #coloca o cursor no inicio do arquivo para
        arquivo.seek(0)
        #atribuindo infinito a menor 
        mdestino=0
        #lendo o cabeçalho
        header = arquivo.readline()
        info = header.split(' ')
        #primeiro na listada
        primeiro=self.lista[0]
        
        #acha menor
        for header in arquivo:
            info = header.split(' ')
            #salvando o numero de vertices
            origem = int(info[0])
            destino = int(info[1])
            peso = float(info[2])
            if(origem==mdestino):
                if(destino==primeiro):
                    #print("Primeiro na listada",peso)
                    return (primeiro,peso)
                    

            if(destino==mdestino):
                if(origem==primeiro):
                    #print("Primeiro na listada",peso)
                    return (primeiro,peso)
    #########################################################################################
    def cria_matriz(self,arquivo):
        #coloca o cursor na primeira linha
        arquivo.seek(0)
        #lendo o cabeçalho
        header = arquivo.readline().rstrip()
        info = header.split()
        #salvando vertices
        origem = int(info[0])
        destino = float(info[1])
        destino = int(destino)
        matriz = [[0 for _ in range(origem)] for _ in range(destino)]
        
        for i in range(0, destino):
            destino = arquivo.readline()
            destino = destino.split(" ")
            x = int(destino[0])
            y = int(destino[1])
            z = destino[2]
            if z[-2:] == "\n":
                z = destino[:-2]
            matriz[x][y] = float(z)
            matriz[y][x] = float(z)

        return matriz


    def refinamento_2opt(self,tempo, caminho, matriz):
        
        aux = []
        aux2 = 0
        tentativa = []
        fim=0
        menor_tamanho=self.custo_percuso(caminho, matriz)
        
        while(tempo>=fim):
            vertice = randint(1, len(caminho) - 2)
            vertice2 = randint(1, len(caminho) - 2)
            

            if vertice != vertice2 and (vertice, vertice2) not in tentativa:

                tentativa.append((vertice, vertice2))

                aux = copy.deepcopy(caminho)
                aux2 = aux[vertice]
                aux[vertice] = aux[vertice2]
                aux[vertice2] = aux2
                if self.custo_percuso(aux, matriz) < self.custo_percuso(caminho, matriz):
                    caminho = copy.deepcopy(aux)
                    menor_tamanho=self.custo_percuso(aux, matriz)
                    
                    #print(menor_tamanho)
                    tentativa = []
            fim = time.time()


            

        return caminho,menor_tamanho

    def custo_percuso(self,percurso, Matriz):
        tamanho = 0
        for i in range(len(percurso) - 1):
            x = percurso[i]
            y = percurso[i + 1]
            tamanho = tamanho + Matriz[x][y]
        return tamanho

                

