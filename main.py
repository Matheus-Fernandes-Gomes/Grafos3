import os
import timeit
import numpy as np
import algoritimos
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
print('Os algoritimos seram executados:\n')
cond=True


selecao = input('\tAtenção o algoritimo só se incerrara com o final do tempo\n\tPressione enter para começar <-|')
algoritimos.algoritimos(arquivo,tempo)


