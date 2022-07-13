# https://www.acmicpc.net/problem/1246

n, m = map(int, input().split())

prices = []
for _ in range(m):
    prices.append(int(input()))
prices = sorted(prices, reverse=True)

answer_sales = 0
answer_price = 0
for i in range(m):
    price = prices[i]
    sales = min(n, i + 1) * price

    if answer_sales <= sales:
        answer_sales = sales
        answer_price = price

print(answer_price, answer_sales)
