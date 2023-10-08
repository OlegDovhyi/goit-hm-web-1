from task_11 import move_files
from pogoda import pogoda_in_city
from pathlib import Path
from prettytable import PrettyTable
from abc import ABC, abstractmethod
import AddressBookBot
import NoteBookBot
import time

class UserInterface(ABC):
    @abstractmethod
    def show_message(self):
        pass

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def get_input(self):
        pass

class PersonalHelper(UserInterface):
    @staticmethod
    def show_message():
        print("\nHello, this is Personal Helper")

    @staticmethod
    def show_menu():
        menu = PrettyTable(["Command", "Instruction"])
        menu.add_rows([
            ["1", "PhoneBook"],
            ["2", "NoteBook"],
            ["3", "SortFiles"],
            ["4", "Weather"],
            ["5", "Fun Game"],
            ["6", "Exit the program"]
        ])
        print("Personal Helper Menu:")
        print(menu)

    @staticmethod
    def get_input():
        PersonalHelper.show_message()
        while True:
            PersonalHelper.show_menu()
            vodim = input("Enter command: ")

            if vodim == '1':
                print('Start work in AddressBook:')
                AddressBookBot.main()

            elif vodim == '2':
                print('Start work in NoteBook:')
                NoteBookBot.main()

            elif vodim == '3':
                path = Path(input('Enter the path of the folder where you want to sort files: '))
                try:
                    move_files(path)
                except FileNotFoundError:
                    print('The specified folder was not found.')
                except Exception as e:
                    print(f'An error occurred: {e}')

            elif vodim == '4':
                pogoda_in_city()

            elif vodim == '5':
                print('The game will start in 3 seconds.')
                time.sleep(3)
                import mygame.main

            elif vodim == '6':
                print("Good bye!")
                break

            else:
                print('Invalid input. Please choose a number from the menu.')

if __name__ == '__main__':
    PersonalHelper.get_input()
