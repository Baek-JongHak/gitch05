goods = input("어떤물건? a = 이로하스 b = 산토카 c = 피아니시모")

a = '이로하스'
b = '산토카'
c = '피아니시모'

price = 0

if goods == 'a' :
    print("이로하스를 선택하였습니다. 가격은 90엔입니다.")
    price = 90
elif goods == 'b' :
    print("산토카를 선택하였습니다. 가격은 300엔입니다.")
    price = 300
elif goods == 'c' :
    print("피아니시모를 선택하였습니다. 가격은 400엔입니다.")
    price = 400
    
if price > 200:
    print("200엔을 넘겼기 떄문에 부과세가 첨부됩니다.")
    price = price*1.2
    print("부과세 포함한 총 가격은" + str(price) + "엔 입니다")
else:
     print("총 가격은" + str(price) + "엔 입니다")
    