import math
import numpy as np
import matplotlib.pyplot as creed
import random

'''Função que armazena e retorna a soma de cada jogada de dois dados com 6 faces'''
def jogar_dados(jogadas):
    jogo = np.int(jogadas) ##variável que recebe o numero de jogadas na função
    jogou=np.zeros(jogo) ##vetor que armazena cada valor jogado
    for i in range(len(jogou)):
        jogou[i] = random.randint(1,7) + random.randint(1,7)
    
    return jogou

'''Função que calcula a média dos jogos'''
def media_jogo(jogou):
    median = 0
    for i in range(len(jogou)):
        median = jogou[i] + median
        
    median = median/len(jogou)
    
    return median

'''Função que retorna o desvio das jogadas'''
def desv_jogo(jogou, median):
    dev =0
    for i in range(len(jogou)):
        dev = (jogou[i]-median)**2 + dev
        
    dev = np.sqrt(dev/len(jogou))
    
    return dev

jogadas = input("Oi, entre o o número de jogadas que queres \n")
jogada_dados = jogar_dados(jogadas)
a_media = media_jogo(jogada_dados)
desvio_jogo = desv_jogo(jogada_dados, a_media)

arquivo = open('media_desvio_de_100.dat', 'w')
arquivo.write('media ='+str(a_media)+' desvio padrão ='+str(desvio_jogo)+'')
arquivo.close()