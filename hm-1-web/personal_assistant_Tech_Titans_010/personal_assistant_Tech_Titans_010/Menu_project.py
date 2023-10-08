from task_11 import move_files
from pogoda import pogoda_in_city
from pathlib import Path
from os import listdir
import AddressBookBot
import NoteBookBot
import time
 


def menu ():
    while  True:
       print(' 1 - PhoneBook;\n 2 - NoteBook;\n 3 - SortFail;\n 4 - Wether;\n 5 - fun game')
       vodim = input("enter command: ")
       
       if vodim == '1':
            print ('start work in AddressBook: ')
            AddressBookBot.main()
              
       elif  vodim == '2':
           print ('start work in NoteBook:')
           NoteBookBot.main()

              
       elif vodim == '3':
            while True:
                path = Path(input('Enter the path of the folder where you want to sort files\n("Введіть путь папки де потрібно зробити сортування файлів"): '))
                if len(str(path)) <= 1:
                    print ("--You didn't lead anything, try another path\n   ('ви нічого не вели, спробуй другой шляx')\n--------------------------------------")
                    break 
                else :      
                    try:
                        move_files (path)
                    except :
                        print ('The path to the folder was not found\n ("Путь к папке не знайден")\n ------------------------------------------------------------------ ')
                        break

       elif vodim == '4':
            pogoda_in_city()

       elif vodim == '5':
              print('the game will start in 3 seconds')
              time.sleep(3)
              import mygame.main
              mygame.main

       elif  vodim.lower()  == 'close' or vodim.lower()  == 'exit':
            print("Good bye!")
            break
       else :
           print('To start the project, select numbers from the menu')

 
if __name__ == '__main__':
 menu ()