# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split(" "))

lowest_package_price = 9999
lowest_single_price = 9999

for _ in range(m):
    package_price, single_price = map(int, input().split(" "))
    if lowest_package_price > package_price:
        lowest_package_price = package_price
    if lowest_single_price > single_price:
        lowest_single_price = single_price

price = 0
while n > 0:
    temp_count = 6 if n >= 6 else n
    if lowest_package_price < lowest_single_price * temp_count:
        price += lowest_package_price
        n -= 6
    else:
        price += lowest_single_price * temp_count
        n -= temp_count
print(price)
