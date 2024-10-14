# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

letter = input("Введите первую букву:")
ages_filter = int(input("Введите минимальный возрастной порог для сортировки:"))
group_name = input("Введите группу:")

# users_list = [user['login'] for user in users if user['login'].startswith(letter)]

users_list = []
ages_list = []
groups_list = []

for user in users:

    if user['login'].startswith(letter):
        users_list.append(user['login'])
        # print(f'Имена: {users_list}')

    if user['age'] > ages_filter:
        ages_list.append(user['age'])
        # print(f'Возраст: {ages_list}')

    if group_name == user['group']:
        groups_list.append(user['group'])
        # print(f'Группа: {groups_list}')

# ages_filter = int(input("Введите минимальный возрастной порог для сортировки:"))
# # ages_list = [user['age'] for user in users if user['age'] > ages_filter]
# ages_list = []
# for user in users:
#     if user['age'] > ages_filter:
#         ages_list.append(user['age'])

# group_name = input("Введите группу:")
# groups_list = [user['group'] for user in users if group_name == user['group']]

print(f"Имена:{users_list}\nВозраст:{ages_list}\nГруппы:{groups_list}")





# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"



