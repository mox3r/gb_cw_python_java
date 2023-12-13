class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add(self, note):
        self.model.note_add(note)
        self.view.display_added()

    def change(self, note_id, note):
        self.model.note_change(note_id, note)
        self.view.display_note_changed(note_id)
        
    def delete(self, note_id):
        try:
            self.model.note_delete(note_id)
            self.view.display_note_deleted(note_id)
        except ValueError:
            self.view.display_idNotExist_msg()

    def show_all_notes(self):
        self.view.display_all(self.model.file_reader())

    def isIdExist(self, note_id):
        if note_id == -1:
            return False
        notes = self.model.file_reader()
        for i in notes:
            if i.note_id == note_id:
                return True
        self.view.display_idNotExist_msg()
        return False
