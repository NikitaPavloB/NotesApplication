# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, 
# сохранять её, читать список заметок, редактировать заметку, удалять заметку.

import json
import os
import datetime


class Note:
    def __init__(self, id, title, body, created_at, updated_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at


class NotesApp:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.notes = []

        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                for note_data in data:
                    note = Note(**note_data)
                    self.notes.append(note)

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append({
                'id': note.id,
                'title': note.title,
                'body': note.body,
                'created_at': note.created_at,
                'updated_at': note.updated_at
            })

        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    def create_note(self, title, body):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(len(self.notes) + 1, title, body, timestamp, timestamp)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Created At: {note.created_at}")
            print(f"Updated At: {note.updated_at}")
            print("-" * 30)

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.updated_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                break

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()


def main():
    app = NotesApp('notes.json')

    while True:
        print("1. Читать заметки")
        print("2. Создать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            app.read_notes()
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            app.create_note(title, body)
        elif choice == '3':
            note_id = int(input("Введите ID заметки: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            app.edit_note(note_id, new_title, new_body)
        elif choice == '4':
            note_id = int(input("Введите ID заметки: "))
            app.delete_note(note_id)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
