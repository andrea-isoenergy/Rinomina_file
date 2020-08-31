#############################################################################
# Filename    : Main_Program.R0.py
# Description : Main program per la gestione dei miei file mp3
# Author      : Andrea Grosso
# Date        : 31 Agosto 2020
# Revision    : R4
# note        : questo programma mi fornisce l'interfaccia utente per il mio
#               programma per la gestione dei mie file mp3
########################################################################
# Importo le librerie che mi interessano
import Gestion_Tags
import Rinomina_files

#definisco le funzioni che mi servono



#main proram


if __name__ == '__main__':
    print('Buongiorno Andrea, cosa vuoi fare? \n')
    while True:
        azione = input('Scegli tra queste due opzioni: Rinomina o Sposta \n')
        if azione.capitalize() == 'Rinomina':
            Rinomina_files.Rinomina()
        elif azione.capitalize() == 'Sposta':
            Gestion_Tags.ControlloSposto()
        else:
            print("L'azione che hai richiesto non e' valida")
        Continuo = input('Finito o no?(Y/N)\n')
        if Continuo.upper() == 'Y':
            break
