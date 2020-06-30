#############################################################################
# Filename    : Rinomina_file.py
# Description : programma per rinominare i file mp3
# Author      : Andrea
# modification: 27/04/2020
# note        : Test la R1 con i file che voglio, cambiato anche il percorso
#               aggiunto anche nuovi confronti sembra funzioni, il test continua
#               Buova revisione con la creazione di un database delle etichette discografiche
#               rende il programma eseguibile negli altri con la dicitura if __main__
########################################################################
# Importo le librerie che mi interessano
import os
import time


#definisco le funzioni che mi servono
def MettiSpazio(file):
    file_modifica_1 = file.replace('_', " ")
    return (file_modifica_1)


def splitnome(file_modifica_1):
    file_modifica_2 = file_modifica_1.split('-')
    artist = str(file_modifica_2[0])
    title = str(file_modifica_2[1])
    nome_provvisorio = artist+'-'+title
    return(nome_provvisorio)


def Sostituiscifeat(file_modifica_1):
    file_modifica_2 = file_modifica_1.replace('feat.', "ft.")
    return (file_modifica_2)


def SostituisciAmp(file_modifica_2):
    file_modifica_3 = file_modifica_2.replace('amp', "&")
    return (file_modifica_3)


def OriginalMix(file_modifica_3):
    file_modifica_4 = file_modifica_3.replace('  Original Mix  ', ' (Original Mix)')
    return(file_modifica_4)


def ExtendedMix(file_modifica_4):
    file_modifica_5 = file_modifica_4.replace('  Extended Mix  ', ' (Extended Mix)')
    return(file_modifica_5)


def RadioEdit(file_modifica_5):
    file_modifica_6 = file_modifica_5.replace(' Radio Edit  ', ' (Radio Edit)')
    return(file_modifica_6)


def Apostrofo(file_modifica_6):
    file_modifica_7 = file_modifica_6.replace('  039 ', "'")
    return(file_modifica_7)


def InstrumentalMix(file_modifica_7):
    file_modifica_8 = file_modifica_7.replace('  Instrumental Mix  ', ' (Instrumental Mix)')
    return(file_modifica_8)


#main proram
start_time = time.time()
path = '/Volumes/Dati/Andrea/Musica/Tracce da separare/'
ls = os.listdir(path)
for a in ls:
    print(a)
    if a =='.DS_Store':
        print('il file ce')
    else:
        (file, ext) = os.path.splitext(a)                                                                               #splitta il nome dall'estensione
        file_modifica_1 = (MettiSpazio(file))                                                                           #rimuove gli underscore dal nome del file
        nome_provvisorio = splitnome(file_modifica_1)                                                                   #crea il nuovo nome
        file_modifica_2 = Sostituiscifeat(nome_provvisorio)                                                             #sostituisce feat. con ft.
        file_modifica_3 = SostituisciAmp(file_modifica_2)                                                               #sostituisce amp con &
        file_modifica_4 = OriginalMix(file_modifica_3)                                                                  #formato mix originale
        file_modifica_5 = ExtendedMix(file_modifica_4)                                                                  #formato extended mix
        file_modifica_6 = RadioEdit(file_modifica_5)                                                                    #formato radio edit
        file_modifica_7 = Apostrofo(file_modifica_6)                                                                    #aggiunge il carattere speciale '
        file_modifica_8 = InstrumentalMix(file_modifica_7)                                                              #formato instrumental mix
        print(file_modifica_8)
        src = path + a                                                                                                  # crea la sorgente dove andare a rinominare il file
        dst = path + file_modifica_8+'.mp3'                                                                             # crea la destinazione con il nuovo nome del file
        os.rename(src, dst)                                                                                             # rinomina il file
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))
