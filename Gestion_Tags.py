#############################################################################
# Filename    : Gestion_Tags.py
# Description : programma che mi permette di leggere i tag dei file MP3
# Author      : Andrea Grosso
# Date        : 5 Agosto 2020
# Revision    : R2
# note        : Uso le librerie mp3_tagger e mutagen
#             : ho trovato il metodo di copiare i file e di spostarli
#             : riesco anche a spostarli sull'hard disk
#             : Inizio ad aggiungere tutti i generi
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
path = '/Volumes/Dati/Download/File completi/Da vedere'
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
            try:
                Tags = (mutagen.File(path+'/'+a).tags.getall("GRP1"))
                mp3 = MP3File(path+'/'+a)
                mp3.set_version(VERSION_2)
                tags = mp3.get_tags()
                print(tags)
                if tags['genre'] == 'Deep House' or tags['genre'] == 'Deep House\x00':
                    # Dest = '/Volumes/Back up 2/Deep House'
                    Dest = '/Volumes/Dati/Deep House'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Tribal House' or tags['genre'] == 'Tribal House\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Tribal House'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'House music' or tags['genre'] == 'House music\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/House music'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Soulful House' or tags['genre'] == 'Soulful House\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Soulful House'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Tech House' or tags['genre'] == 'Tech House\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Tech House'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Nu Disco' or tags['genre'] == 'Nu Disco\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Nu Disco'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Old school House' or tags['genre'] == 'Old school House\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Old school House'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
                if tags['genre'] == 'Techno' or tags['genre'] == 'Techno\x00':
                    # Dest = '/Volumes/Back up 2/Tribal House'
                    Dest = '/Volumes/Dati/Techno'
                    # if Tags[0] == "Vocal" or Tags[0] == 'Instrumental':
                    shutil.move((path + '/' + a), Dest)
            except:
                print(a + 'Questo file ha qualche problema')
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))