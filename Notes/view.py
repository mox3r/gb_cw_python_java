class View(object):

    @staticmethod
    def display_added():
        print("Заметка успешно добавлена.")

    @staticmethod
    def display_all(notes):
        print('-----------------------------------------------')
        for x in notes:
            print(x)
            print('-----------------------------------------------')
            
    @staticmethod
    def display_note_changed(note_id):
        print(f'Заметка #{note_id} успешно изменена')
        
    @staticmethod
    def display_note_deleted(note_id):
        print(f'Заметка #{note_id} успешно удалена.')
        
    @staticmethod
    def display_idNotExist_msg():
        print('Заметка не найдена, попробуйте ещё раз')
    @staticmethod
    def display_cancel_msg():
        print('Отменено.')