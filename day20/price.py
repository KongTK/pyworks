# 배송비 계산하기
# 조건 - 주문 상품 가격이 20,000원 미만이면 배송비(2,500원) 포함, 아니면 무료 배송

def price(unitprice, quantity):
    delivery_fee = 2500
    price = unitprice * quantity
    if price < 20000:
        price += delivery_fee
        return price
    else:
        return price
   
p1 = price(15000, 2)
print("상품 가격1은 " + format(p1, ',d') + "원입니다")
p2 = price(5000, 3)
print("상품 가격2는 " + str(p2) + "원입니다")
