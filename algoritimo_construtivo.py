import numpy as np
import timeit
class algoritimo_construtivo:
    # Inicializador
    def __init__(self, arquivo):
        # Classe com todos os atributos e metodos do algoritimo construtivo
        #self.morigem,self.mdestino,self.menor = self.menor(arquivo)
        self.lista,self.resu = self.constroi(arquivo)
        self.imprimi(self.lista,self.resu)

    def imprimi(self,Lista,resu):
        print(resu)
        print(Lista)

    def constroi(self, arquivo):
        
        #lendo o cabeçalho
        header = arquivo.readline()
        info = header.split(' ')
        
        #cria lista
        lista = []
        #percorre cada linha do arquivo
        #atribui infinito para menor 
        menor=float("inf")
        resu=0
        #partindo do menor
        vertice1,destino1,tamanho1=self.menor(arquivo)
        print("ponnto1")
        print(vertice1,destino1,tamanho1)
        lista.append(vertice1)
        morigem,mdestino1,menor=self.menor_no_vertice(arquivo,vertice1)
        print("ponto 2")
        print(vertice1,destino1,menor)
        lista.append(morigem)
        morigem1,mdestino,menor=self.menor_no_vertice(arquivo,mdestino1)
        print("ponto3")
        print(vertice1,destino1,menor)
        lista.append(morigem1)

            



        
        '''for header in arquivo:
            info = header.split(' ')
            origem = int(info[0])
            #testa para cada linha do vertice
            if(origem not in lista):
                morigem,mdestino,menor=self.menor_no_vertice(arquivo,origem)
                resu=resu+menor
                lista.append(morigem)'''
        return(lista,resu)
    

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
        print("ponto 4")
        print(morigem,mdestino,menor)
        return (morigem,mdestino,menor)


    def menor_no_vertice(self,arquivo,vertice):
        #atribuindo infinito a menor p
        menor=float("inf")
        morigem=0
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
            #verifica se os vertices são iguais
            if(vertice == origem):
                #enontra o menor 
                if peso<menor:
                    menor=peso
                    morigem=origem
                    mdestino=destino
            print("***************")
            print(morigem,mdestino,menor)
        return (morigem,mdestino,menor)
