#############################################################################
# Filename    : Rinomina_file.py
# Description : programma per rinominare i file mp3
# Author      : Andrea
# modification: 06/07/2020
# note        : Creata la parte del database
#               rende il programma eseguibile negli altri con la dicitura if __main__
########################################################################
# Importo le librerie che mi interessano
import os
import time
import sqlite3
from os.path import isfile

#definisco le funzioni che mi servono
def MettiSpazio(file):
    file_modifica_1 = file.replace('_', " ")
    return (file_modifica_1)


def splitnome(file_modifica_1):
    file_modifica_2 = file_modifica_1.split('-')
    artist = str(file_modifica_2[0])
    title = str(file_modifica_2[1])
    try:
        etichetta = str(file_modifica_2[2])
    except:
        etichetta = " "
    nome_provvisorio = artist+'-'+title
    return(nome_provvisorio, etichetta)


def Sostituiscifeat(file_modifica_1):
    file_modifica_2 = file_modifica_1.replace('feat.' or 'feat', "ft.")
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


def controllo_database(file_name):
    if not isfile (file_name):                                                                                          # controlla se il file esiste gia' o deve essere creato
        genera_file(file_name)
        genera_tabella(file_name)
        ID = 1
    else:
        print("Il file esiste gia'")
        #genera_tabella(file_name)
        ID = controllo_ID(file_name)
    return(ID)


def genera_tabella(file_name):                                                                                          # genera la tabella con la data corrente
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Lista etichette'"
    sql_cmd = '''CREATE TABLE IF NOT EXISTS {}
                    (ID TEXT PRIMARY KEY NOT NULL,
                     Etichetta TEXT NOT NULL)'''.format(Nome_Table)
    c.execute(sql_cmd)
    Data_Base.commit()
    Data_Base.close()
    print('Tabella creata')
    return


def genera_database(file_name, ID, etichetta):
    Data_Base = sqlite3.connect (file_name)                                                                             # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Lista etichette'"
    c.execute("INSERT INTO " + Nome_Table + 'VALUES (?, ?)', (ID, etichetta))
    Data_Base.commit()
    Data_Base.close()
    print('Data base creato')


def genera_file(file_name):                                                                                             # genera il file
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    Data_Base.commit()
    Data_Base.close()
    print('File creato')
    return


def controllo_ID(file_name):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Lista etichette'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        ID = int(row[0]) + 1
    return(ID)


def controllo_etichetta(file_name, etichetta):
    Data_Base = sqlite3.connect(file_name)                                                                              # apre il file il sqlite con il nome che gli ho dato
    c = Data_Base.cursor()
    Nome_Table = "'Lista etichette'"
    c.execute("SELECT * FROM" + Nome_Table)
    rows = c.fetchall()
    for row in rows:
        esistente_etichetta = row[1]
        if esistente_etichetta == etichetta:
            nuova_etichetta = "l'etichetta e' gia' presente nel database"
            break
        else:
            nuova_etichetta = etichetta
    return(nuova_etichetta)


#main proram
if __name__ == "__main__":
    start_time = time.time()
    path = '/Volumes/Dati/Andrea/Musica/Tracce da separare/'
    ls = os.listdir(path)
    file_name = 'List_Label.db'
    for a in ls:
        print(a)
        if a =='.DS_Store':
            print("il file c'é ma non posso cancellarlo")
        else:
            (file, ext) = os.path.splitext(a)                                                                               #splitta il nome dall'estensione
            file_modifica_1 = (MettiSpazio(file))                                                                           #rimuove gli underscore dal nome del file
            nome_provvisorio = splitnome(file_modifica_1)                                                                   #crea il nuovo nome
            etichetta = (nome_provvisorio[1])
            #print(etichetta)
            ID = controllo_database(file_name)
            nuova_etichetta = controllo_etichetta(file_name, etichetta)
            if nuova_etichetta != "l'etichetta e' gia' presente nel database":
                genera_database(file_name, ID, nuova_etichetta)
                ID = ID + 1
            file_modifica_2 = Sostituiscifeat(nome_provvisorio[0])                                                             #sostituisce feat. con ft.
            file_modifica_3 = SostituisciAmp(file_modifica_2)                                                               #sostituisce amp con &
            file_modifica_4 = OriginalMix(file_modifica_3)                                                                  #formato mix originale
            file_modifica_5 = ExtendedMix(file_modifica_4)                                                                  #formato extended mix
            file_modifica_6 = RadioEdit(file_modifica_5)                                                                    #formato radio edit
            file_modifica_7 = Apostrofo(file_modifica_6)                                                                    #aggiunge il carattere speciale '
            file_modifica_8 = InstrumentalMix(file_modifica_7)                                                              #formato instrumental mix
            #print(file_modifica_8)
            src = path + a                                                                                                  # crea la sorgente dove andare a rinominare il file
            dst = path + file_modifica_8+'.mp3'                                                                             # crea la destinazione con il nuovo nome del file
            os.rename(src, dst)                                                                                             # rinomina il file
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))
