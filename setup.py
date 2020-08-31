#############################################################################
# Filename    : Template.py
# Description : File di template da usare tutte le volte che scrivo un programma
# Author      : Andrea
# Date        : 13-07-2020
# Revision    : R1
# note        : Aggiunto la parte relativa alle classi
########################################################################
# Importo le librerie che mi interessano

# Definisco le classi che mi servono

# Definisco le funzioni che mi servono


# Main proram
from setuptools import setup

APP = ['Main_Program.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)