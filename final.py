note = {}

note['username'] = input('Имя пользователя: ')
note['title'] = input('Имя заголовка: ')
note['content'] = input('Содержимое заметки: ')
note['status'] = input('Статус заметки: ')
note['created_date'] = input('Дата создания заметки (день/месяц/год): ')
note['issue_date'] = input('Дата истечения заметки (день/месяц/год): ')

note['titles'] = []
for i in range(3):
    title = input(f'Введите имя заметки {i + 1} : ')
    note['titles'].append(title)

print('\nВся информация о заметки: ')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')


