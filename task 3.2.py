"""
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
"""


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Ivanov', name='Ivan', year='1991', city='Moscow', email='123321@mail.ru',
              telephone='8-903-999-99-99'))