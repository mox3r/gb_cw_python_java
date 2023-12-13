import json
import os
from view import View
from note import Note


class ModelJson(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.notes = list()

    """Create note"""

    def note_add(self, note):
        self.notes = self.file_reader()

        id = 0
        for item in self.notes:
            if item.note_id > id:
                id = item.note_id
        id = id + 1
        note.note_id = id

        self.notes.append(note)
        self.file_writer(self.notes)

    """Changer"""

    def note_change(self, note_id, note):
        self.notes = self.file_reader()
        for item in self.notes:
            if item.note_id == note_id:
                item.date = note.date
                item.title = note.title
                item.text = note.text
        self.file_writer(self.notes)

    """Deleter"""

    def note_delete(self, note_id):
        msg = input(
            f'Вы собрались удалить заметку #{note_id}. Вы уверены? (Да/Нет): '
        ).lower()
        if msg == 'да':
            self.notes = self.file_reader()
            for i, note in enumerate(self.notes):
                if note.note_id == note_id:
                    del self.notes[i]
            self.file_writer(self.notes)
        elif msg == 'нет':
            View.display_cancel_msg()

    """Writer"""

    def file_writer(self, notes):
        str_list = list()
        for note in notes:
            str_list.append({
                'id': note.note_id,
                'date': note.date,
                'title': note.title,
                'text': note.text
            })

        notes_list = json.dumps(str_list,
                                indent=4,
                                ensure_ascii=False,
                                sort_keys=False,
                                default=str)

        with open(self.fileName, "w", encoding='utf-8') as fout:
            fout.write(notes_list)
            fout.close()

    """Reader"""

    def file_reader(self):
        #проверка на существование и создание, если файла нет
        if not os.path.isfile(self.fileName):
            fp = open(self.fileName, "x")
            fp.close()
        notes_list = list()
        try:
            with open(self.fileName, "r", encoding="utf-8") as fin:
                notes_json = fin.read()
                fin.close()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(
                    Note(item['id'], item['date'], item['title'],
                         item['text']))

            return notes_list
        except ValueError:
            return self.notes
