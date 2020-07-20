# for 구문으로 구구단 출력하기
for i in range(2, 10) :
    print()
    print("****", i ,"단****")
    for j in range(1, 10) :
        print("{} * {} = {}".format(i, j, i*j), end = '\n')

# while 문으로 구구단 출력하기
i = 2
while i < 10 :
    print()
    print("****", i ,"단****")
    j = 1
    while j < 10 :
        print("{} * {} = {}".format(i, j, i*j), end = "\n")
        j += 1
    i += 1