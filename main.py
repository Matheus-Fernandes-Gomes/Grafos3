import os
import timeit
import numpy as np
import algoritimo_construtivo
#verifica e entra no arquivo do grafo
verificador = False
arquivo = ''
while not verificador:
    arquivo = input('\n Informe o Grafo: ')
    verificador = os.path.exists(arquivo)
    if not verificador:
        espera = input("\nArquivo não encontrado!\n Verifique o nome do arquivo e tente novamente!")
print('\n Arquivo encontrado!\n')
arquivo = open(arquivo, 'r')

#inserção e verificação de tempo de
cond=True
while (cond):
    tempo = int(input("Tempo limite (s):"))
    if (tempo<10)or(tempo>600):
        print("Informa um valor de tempo superior a 10 segundos e inferior a 10 minutos:")
    else:
        cond=False 

#seleção do algoritimo construtivo a ser executado
print('\tEscolha o algoritimo construtivo a ser executado:\nSendo:')
cond=True
while (cond):

    selecao = input('\t1 Algoritimo construtivo \n\t2 Algoritimo de refinamento\n-1 Para sair ')
    selecao = int(selecao)
    if ((selecao==1)or(selecao==2)or(selecao==-1)):
        if selecao == 1:       
            algoritimo_construtivo.algoritimo_construtivo(arquivo)           
            print("retorno")
        elif selecao ==2:
            print("bla")

        else:
            break;
            cond=False
        #Limpa a tela

        #os.system('cls') or None
    else:
        print('\n selecao invalida!')


