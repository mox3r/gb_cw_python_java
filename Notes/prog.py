import os
import datetime
import time

from controller import Controller
from modelJson import ModelJson
from note import Note
from view import View


def main():
    fname = r'NotesDB.json'
    ctrl = Controller(ModelJson(fname), View)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Программа \"Заметки\"')
        print('Выберите действие:\n' + '1 - Создать заметку\n' +
              '2 - Изменить заметку\n' + '3 - Удалить заметку\n' +
              '4 - Показать существующие заметки\n' + '0 или q - Выход')
        choice = input('Ваш выбор: ').lower()

        match choice.split():
            case ["1"]:
                ctrl.add(get_note())
                input('Нажмите ВВОД для продолжения...')
            case ["2"]:
                id = get_note_id()
                if ctrl.isIdExist(id):
                    ctrl.change(id, get_note())
                input('Нажмите ВВОД для продолжения...')
            case ["3"]:
                id = get_note_id()
                if ctrl.isIdExist(id):
                    ctrl.delete(id)
                input('Нажмите ВВОД для продолжения...')
            case ["4"]:
                ctrl.show_all_notes()
                input('Нажмите ВВОД для продолжения...')
            case ["0"]:
                break
            case ["q"]:
                break
            case _:
                print('Что это было?')
                time.sleep(1)


"""Returns note's body"""


def get_note():
    return Note(note_id=0,
                date=datetime.datetime.now(),
                title=input('Введите название заметки: '),
                text=input('Введите текст заметки: '))


"""Returns id num"""


def get_note_id():
    try:
        id = int(input('Введите номер заметки: '))
        if id > 0:
            return id
        else:
            print("Ожидается положительное число, попробуйте в следующий раз.")
            return -1
    except ValueError:
        print('Ожидалось число, попробуйте в следующий раз.')
        return -1
