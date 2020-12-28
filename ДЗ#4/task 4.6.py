from itertools import count, cycle

for el in count(int(input(f'Для выхода введите "q" \nВведите стартовое число: '))):
    print(el, end='')
    quit = input()
    if quit == 'q':
        break


my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el, end='')
    quit = input()
    if quit == 'q':
        break
