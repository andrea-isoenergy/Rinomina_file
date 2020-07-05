#############################################################################
# Filename    : Gestion_Tags.py
# Description : programma che mi permette di leggere i tag dei file MP3
# Author      : Andrea Grosso
# Date        : 5 Luglio 2020
# Revision    : R0
# note        : ho installato la libreria mp3_tagger e la libreria mutagen e la libreria eyed3
#               al momento mutagen e' quella che mi convince di meno
########################################################################
# Importo le librerie che mi interessano
import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time
import eyed3
from mutagen.id3 import ID3, TIT2
import mutagen
# Definisco le funzioni che mi servono


# Main proram
start_time = time.time()
path = '/Volumes/Dati/Download/File completi/Beatport Top 100 Deep House (10th June 2019)'
ls = os.listdir(path)
#mp3 = MP3File(path)
for a in ls:
    print(a)
    if a =='.DS_Store':
        print("il file c'é ma non posso cancellarlo")
    else:
        (file, ext) = os.path.splitext(a)
        #print(file)
        #print(ext)
        if ext == '.wav':
            pass
        else:
            #print(mutagen.File(path+'/'+a).tags.getall("TXXX"))
            audiofile = eyed3.load(path+'/'+a)
            print (audiofile.tag.)
            #mp3 = MP3File(path+'/'+a)
            #mp3.set_version(VERSION_2)
            #tags = mp3.get_tags()
            #print(tags)
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))