#############################################################################
# Filename    : Gestion_Tags.py
# Description : programma che mi permette di leggere i tag dei file MP3
# Author      : Andrea Grosso
# Date        : 15 Luglio 2020
# Revision    : R1
# note        : Uso le librerie mp3_tagger e mutagen
#             : ho trovato il metodo di copiare i file e di spostarli
#             : riesco anche a spostarli sull'hard disk
########################################################################
# Importo le librerie che mi interessano
import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time
import eyed3
from mutagen.id3 import ID3, TIT2
import mutagen
import shutil
# Definisco le funzioni che mi servono


# Main proram
start_time = time.time()
path = '/Volumes/Dati/Download/File completi/Beatport Best New Tracks Afro House (4th June 2019)'
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
            Tags = (mutagen.File(path+'/'+a).tags.getall("GRP1"))
            mp3 = MP3File(path+'/'+a)
            mp3.set_version(VERSION_2)
            tags = mp3.get_tags()
            if tags['genre'] == 'Deep House' or tags['genre'] == 'Deep House\x00':
                Dest = '/Volumes/Back up 2/Deep House'
                if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                    #print(a)
                    #print(Tags[0])
                    #print(tags['genre'])
            if tags['genre'] == 'Tribal House' or tags['genre'] == 'Tribal House\x00':
                Dest = '/Volumes/Back up 2/Tribal House'
                if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                    #print(a)
                    #print(Tags[0])
                    #print(tags['genre'])
            #audiofile = eyed3.load(path+'/'+a)
            #print (audiofile.tag.)
            #mp3 = MP3File(path+'/'+a)
            #mp3.set_version(VERSION_1)
            #tags = mp3.get_tags()
            #print(tags)
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))