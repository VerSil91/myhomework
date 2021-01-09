subj = {}

with open('file_6.txt', 'r', encoding="utf-8") as init_f:
    for line in init_f:
     name, status = line.split(':')
     name_sum = sum(map(int, "".join([i for i in status if i == ' ' or '9' >= i >= '0']).split()))
     subj[name] = name_sum
print(f"{subj}")
