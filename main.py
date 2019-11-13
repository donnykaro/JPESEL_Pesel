import sys

correct_range_of_nums = 11
max_number_of_cases = 100


def check_pesel(p):
    if len(p) < correct_range_of_nums:
        return 'N'

    wynik = int(p[0]) + (int(p[1]) * 3) + (int(p[2]) * 7) + (int(p[3]) * 9) + int(p[4]) + (int(p[5]) * 3) + \
            (int(p[6]) * 7) + (int(p[7]) * 9) + int(p[8]) +(int(p[9]) * 3) + int(p[10])

    if wynik < 0:
        return 'N'

    if str(wynik)[-1] == '0':
        return 'D'
    else:
        return 'N'


pesels = []
num_of_cases = int(input())
if num_of_cases > max_number_of_cases:
    sys.exit(0)
for i in range(1, num_of_cases+1):
    pesel = input()
    pesels.append([pesel, check_pesel(pesel)])


for p in pesels:
    print(p[1])
