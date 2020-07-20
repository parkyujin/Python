# 다음의 결과가 나올 수 있도록 반복문을 활용.

'''
a   b   c   d   e   f   g   h
i   j   k   l   m   n   o   p
q   r   s   t   u   v   w   x
y   z
'''

for x in range(97, 123) :
    if x % 8 == 0 :
        print('{:<4}'.format(chr(x)))
    else :
        print('{:<4}'.format(chr(x)), end='')