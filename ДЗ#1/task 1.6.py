start = int(input("Результат в 1-ый день (в км): "))
finish = int(input("Необходимо достигнуть (в км): "))
day = 1
while True:
    if start > finish:
        break
    start *= 1.1
    day += 1
print(f"на {day}-й день спортсмен достиг результата — не менее {finish} км.")
