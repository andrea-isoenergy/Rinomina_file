#############################################################################
# Filename    : Rinomina_file.py
# Description : programma per rinominare i file mp3
# Author      : Andrea
# modification: 27/04/2020
########################################################################
# Importo le librerie che mi interessano
import os
import shutil
from mutagen.mp3 import MP3


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


def OriginalMix(file_modifica_2):
    file_modifica_3 = file_modifica_2.replace('  Original Mix  ', ' (Original Mix)')
    return(file_modifica_3)


def ExtendedMix(file_modifica_3):
    file_modifica_4 = file_modifica_3.replace('  Extended Mix  ', ' (Extended Mix)')
    return(file_modifica_4)





#main proram
path = '/Users/andreagrosso/Dropbox/Pythons/Software/Python/Rinomina file/MP3/'
ls = os.listdir(path)
for a in ls:
    #print(a)
    (file, ext) = os.path.splitext(a)                                                                                   #splitta il nome dall'estensione
    #print("Filename without extension =", file)
    file_modifica_1 = (MettiSpazio(file))                                                                               #rimuove gli underscore dal nome del file
    #print(file_modifica_1)
    nome_provvisorio = splitnome(file_modifica_1)                                                                        #crea il nuovo nome
    file_modifica_2 = Sostituiscifeat(nome_provvisorio)                                                                 #sostituisce feat. con ft.
    #print(file_modifica_2)
    file_modifica_3 = OriginalMix(file_modifica_2)                                                                      #formato mix originale
    file_modifica_4 = ExtendedMix(file_modifica_3)                                                                      #formato extended mix
    #print(file_modifica_4)
    #file_modifica_4 = splitnome(file_modifica_3)
    #print((str(file_modifica_4[0:1])) + ' _ ' + (str(file_modifica_4[1:2])))
    src = path + a
    print(src)
    dst = path + file_modifica_4+'.mp3'
    print(dst)
    os.rename(src, dst)









        #print("Extension =", ext)

#filename = os.path.basename(path)
# Use splitext() to get filename and extension separately.
#(file, ext) = os.path.splitext(filename)

# Print outcome.
#print("Filename without extension =", file)
#print("Extension =", ext)