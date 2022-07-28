from collections import deque
from typing import List, Dict


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def get_costs_of_skus(graph: List[List[int]], targets: List[Point], start: Point) -> Dict[Point, int]:
    queue = deque()
    queue.append(start)

    visited = [[False] * len(graph[0]) for _ in range(len(graph))]
    visited[start.row][start.col] = True

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    while queue:
        can_stop_iteration = True
        for target in targets:
            if not visited[target.row][target.col]:
                can_stop_iteration = False

        if can_stop_iteration:
            break

        point = queue.popleft()
        row = point.row
        col = point.col

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < len(graph) and 0 <= new_col < len(graph[0]):
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    graph[new_row][new_col] = graph[row][col] + 1
                    queue.append(Point(new_row, new_col))

    targets_costs: Dict[Point, int] = dict()
    for target in targets:
        targets_costs[target] = graph[target.row][target.col]

    return targets_costs


def get_cost_of_two_skus(graph: List[List[int]], start: Point, finish: Point) -> int:
    costs = get_costs_of_skus(graph, [finish], start)

    return costs[finish]


if __name__ == '__main__':
    graph = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    costs = get_costs_of_skus(graph, [Point(2, 2), Point(5, 6), Point(3, 11), Point(9, 6)], Point(0, 0))
    for cost in costs:
        print(f"{cost.row}, {cost.col} : {costs[cost]}")
