"""
Fundir PDF,Alarme, Código fonte de site
"""

# Alarme:
from tkinter import * #Responsavel pela criação da interface, importamos todas funções
import datetime
import time
from playsound import playsound #Responsavel pelo sinal sonoro #pip install playsound

root = Tk() #Definição do objeto da interface
root.geometry('500x250') #Definição do tamanho do objeto

def alarme(): #Função para impressão da hora atual e hora do alarme
    while True:
        fixar_tempo_alarme = f"{hora.get()}:{minuto.get()}:{segundo.get()}"  #Tempo escolhido pelo usuario, o get serve para reconhecer a hora escolhida
        tempo_atual = datetime.datetime.now().strftime("%H:%M:%S") #Tempo atual
        time.sleep(1) #Delay para melhorar imprimir de 1 em 1 segundos a contagem
        print(tempo_atual,fixar_tempo_alarme) #Impressao dos tempos
        if tempo_atual == fixar_tempo_alarme: #Caso chegue a hora do alarme
            print("Alarme Ativado") #Aviso
            playsound('som_alarme.mp3') #Ativa o sinal sonoro e para o loop
            break

Label(root,text='Alarme',font=('Arial',25),fg='Gray').place(x=200,y=0) #Armazenando um texto na interface com fonte e cor, o place serve para fixar as coordenadas q estarao o texto
Label(root,text='Defina o tempo que o alarme irá tocar:',font=('Arial',12),fg='Red').place(x=125,y=50)

hora=StringVar(root) #Criação das variaveis strings na interface
horas =['00','01','02','03','04','05','06','07','08','09','10','11','12',
        '13','14','15','16','17','18','19','20','21','22','23','24'] #Armazenando opções
hora.set(horas[0]) #Definindo a primeira opção como a primeira posição da tupla
h = OptionMenu(root,hora,*horas) #Armazenando no menu de opções todas as horas
h.place(x=125,y=100) #Fixando a localização do botao

minuto=StringVar(root)
minutos =('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
          '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41',
          '42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
minuto.set(horas[0])
m = OptionMenu(root,minuto,*minutos)
m.place(x=230,y=100)

segundo=StringVar(root)
segundos =('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
          '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41',
          '42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
segundo.set(segundos[0])
s = OptionMenu(root,segundo,*segundos)
s.place(x=330,y=100)

Button(root,text='Confirmar',font=('Arial',12),fg='green',command=alarme).place(x = 210,y=150) #Definição do botao de confirmação
root.mainloop() #Manter o alarme ativado

#aquirindo código fonte de um site:
import urllib.request
print(urllib.request.urlopen("https://www.youtube.com/").read())

#Fundir PDF's:
from PyPDF2 import PdfFileReader, PdfFileMerger #pip install PyPDF2

arq1 = PdfFileReader("Arquivo1.pdf")
arq2 = PdfFileReader("Arquivo2.pdf")

mesclando = PdfFileMerger()
print(mesclando)
mesclando.append(arq1)
mesclando.append(arq2)

mesclando.write("Arquivo3.pdf")

