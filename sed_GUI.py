#!/usr/bin/python3

import os , subprocess , tkinter
from tkinter import *

from tkinter import filedialog


def dizinSec():
    file_path_string = filedialog.askopenfiles()

    yol = str(file_path_string)

    print(yol)

    global liste, liste2
    liste = []
    liste2 = []

    for i in yol.split():
        liste.append(i)
    print(liste[1])

    for i in liste[1].split('='):
        liste2.append(i)
    print(liste2[1])

    kelime1 = esasKelime.get()
    kelime2 = sonHali.get()




    global kelime3, yedek ,sil ,yarat

    # kelime3 = "'sed '" + "'s/'" + kelime1 + "'/'" + kelime2 + "'/g'" + "' '" + liste2[1]
    yedek = "/home/aspa/Desktop/yedek.txt"
    kelime3 = 'sed ' + "'" + 's/' + kelime1 + '/' + kelime2 + '/g' + "'" + ' ' + liste2[1] + ' >' + yedek
    sil = 'rm ' + liste2[1]
    yarat = 'mv ' + yedek + ' ' + liste2[1]


def Degistir():

    try:
        degisim = subprocess.check_output([kelime3], shell=True)
        degisim.decode()

        siL = subprocess.check_output([sil], shell=True)
        siL.decode()

        yaraT = subprocess.check_output([yarat], shell=True)
        yaraT.decode()



        """
        rm
    dosya.txt
    mv
    dosya2.txt
    dosya.txt
    print(kelime3)
        """
    except:
        print(Exception)





pencere = Tk()
pencere.title("KELİME  DEDİSTİR")
pencere.geometry("570x150")
pencere.resizable(False, False)


etiket = Label(text="Değişecek kelime Gir  ", fg="magenta", bg="light green")
etiket.place(x=40, y=5, width=190, height=20)

etiket2 = Label(text="Değişmesini istediğin kelime Gir  ", fg="magenta", bg="light green")
etiket2.place(x=255, y=5, width=190, height=20)

esasKelime = Entry(pencere)
esasKelime.place(x=35, y=25, width=200, height=30)

sonHali = Entry(pencere)
sonHali.place(x=250, y=25, width=200, height=30)

dosyaSecBTN=Button(text="Dosya Sec ", bg="orange", fg="navy", command=dizinSec)
dosyaSecBTN.place(x=470, y=25 ,width=90, height=30)

btn = Button(text="DEGİSTİR ", bg="orange", fg="navy", command=Degistir)
btn.place(x=470, y=75 ,width=90, height=30)









mainloop()


