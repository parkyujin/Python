# 랜덤 로또 번호

from random import randint
cnt = 0
lot = ''
for x in range(100) :
    rand = '{:02}'.format(randint(1,45))
    if rand + ' ' not in lot :
        lot = lot + rand + ' '
        cnt = cnt + 1
    if cnt == 6:
        print(lot)
        break

        