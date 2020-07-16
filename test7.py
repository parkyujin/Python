환율 = float(input("현재 환율 : "))
won = int(input("교환 : "))
dollars = int(won)/float(환율)
print("원 대비 달러는 {:.2f} 달러 입니다.".format(dollars))