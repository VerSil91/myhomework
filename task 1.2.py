time = int(input("Введите время в секундах: "))
hrs = time // 3600
minutes = (time // 60) % 60
sec = time % 60
if minutes < 10:
    minutes = "0" + str(minutes)
if hrs < 10:
    hrs = "0" + str(hrs)
if sec < 10:
    sec = "0" + str(sec)
print(str(hrs) + ":" + str(minutes) + ":" + str(sec))
