username = input('Имя пользователя: ')
title = input('Имя заголовка: ')
content = input('Содержимое заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки (день/месяц/год): ')
issue_date = input('Дата истечения заметки (день/месяц/год): ')

titles = []
for i in range(3):
    title = input(f'Введите имя заметки {i + 1} : ')
    titles.append(title)

print('\nВы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Заголовок заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)