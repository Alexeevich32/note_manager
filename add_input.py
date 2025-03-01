username = input('Имя пользователя: ')
title = input('Имя заголовка: ')
content = input('Содержимое заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки (день/месяц/год): ')
issue_date = input('Дата истечения заметки (день/месяц/год): ')

title_0 = input('Введите имя заметки: ')
title_1 = input('Введите имя заметки: ')
title_2 = input('Введите имя заметки: ')
titles = [title_0, title_1, title_2]

print('\nВы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Заголовок заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)