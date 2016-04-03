import heapq

# Referenced from http://www.redblobgames.com/pathfinding/a-star/implementation.html

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    path = []
    current = goal
    while current != start:
        next = came_from[current]

        horizontal = next[0] - current[0]
        vertical   = next[1] - current[1]

        if horizontal > 0:
            direction = 0
        elif horizontal < 0:
            direction = 1
        elif vertical > 0:
            direction = 2
        elif vertical < 0:
            direction = 3

        path.insert(0, [current, direction])

        current = next

    return path
