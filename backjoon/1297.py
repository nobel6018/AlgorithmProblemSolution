# https://www.acmicpc.net/problem/1297

import math

(D, H, W) = map(int, input().split(" "))

n = math.sqrt(D ** 2 / (W ** 2 + H ** 2))
height = math.floor(n * H)
width = math.floor(n * W)

print(height, width)
