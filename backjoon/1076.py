# https://www.acmicpc.net/problem/1076


colors = dict({
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 1_000],
    "yellow": [4, 10_000],
    "green": [5, 100_000],
    "blue": [6, 1_000_000],
    "violet": [7, 10_000_000],
    "grey": [8, 100_000_000],
    "white": [9, 1_000_000_000],
})

color1 = str(colors[input()][0])
color2 = str(colors[input()][0])
color3 = colors[input()][1]

print(int(color1 + color2) * color3)
