from os import SEEK_CUR
import numpy as np
import timeit
class algoritimo_construtivo:
    # Inicializador
    def __init__(self, arquivo):
        # Classe com todos os atributos e metodos do algoritimo construtivo
        #self.morigem,self.mdestino,self.menor = self.menor(arquivo)
        #cria lista
        self.lista= []
        self.n_vertices=0
        self.lista,self.resu = self.constroi(arquivo)
        self.imprimi(self.lista,self.resu)
        #self.menor_no_vertice(arquivo,3)

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
            resu=resu+menor 

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
        return(self.lista,resu)
    

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
            #salvando o numero de vertices e arestas
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
                    
                

