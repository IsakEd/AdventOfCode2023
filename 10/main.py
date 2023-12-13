import itertools as it
import collections as cl

with open("10/input.txt") as f:
    lines = [list(line.rstrip()) for line in f]


class Seeker:
    position: tuple = ()
    S: tuple = ()
    symbol = ""
    matrix: list = []
    seen_S = 0
    seen = []
    steps_taken = 0
    instruction = "D"
    started = False

    def __init__(self, matrix) -> None:
        self.position = self.find_start(matrix)
        self.S = self.position
        self.matrix = matrix

    def find_start(self, matrix):
        for r, c in it.product(range(len(lines)), range(len(lines[0]))):
            if matrix[r][c] == "S":
                return (r, c)

    def get_neighbours(self):
        print(self.position)
        neighbours = []
        for i, j in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            pos = (self.position[0] + i, self.position[1] + j)
            if pos[0] in range(len(self.matrix)) and pos[1] in range(
                len(self.matrix[0])
            ):
                neighbours.append(pos)
        return neighbours

    def move(self, instruction):
        match instruction:
            case "U":
                self.position = (self.position[0] - 1, self.position[1])
            case "D":
                self.position = (self.position[0] + 1, self.position[1])
            case "L":
                self.position = (self.position[0], self.position[1] - 1)
            case "R":
                self.position = (self.position[0], self.position[1] + 1)
        self.steps_taken += 1
        print(f"Moving {instruction}")

    def next_instruction(self):
        self.symbol = self.matrix[self.position[0]][self.position[1]]
        print(f"reading {self.symbol}")
        match self.symbol:
            case "L":
                self.instruction = "U" if self.instruction == "L" else "R"
            case "J":
                self.instruction = "U" if self.instruction == "R" else "L"
            case "F":
                self.instruction = "R" if self.instruction == "U" else "D"
            case "7":
                self.instruction = "L" if self.instruction == "U" else "D"

    def traverse(self):
        while self.seen_S < 2:
            self.seen.append(self.position)
            print(f"Symbol is {self.symbol}")
            if self.symbol == "S":
                self.seen_S += 1
            self.next_instruction()
            self.move(self.instruction)
        print((self.steps_taken - 1) // 2)
        pass


seeker = Seeker(lines)
seeker.traverse()
maze_positions = set(seeker.seen)
rows = []
for row in range(len(lines)):
    rows.append([tup[1] for tup in maze_positions if tup[0] == row])

# P2


class FloodFill:
    inside = set()
    outside = set()
    maze = set()
    dots = set()
    mat = []

    def __init__(self, mat, maze_positions) -> None:
        self.dots = [
            (i, j)
            for i, j in it.product(range(len(mat)), range(len(mat[0])))
            if mat[i][j] == "."
        ]
        self.maze = maze_positions
        self.mat = mat

    def get_neighbours(self, position):
        print(position)
        neighbours = []
        for i, j in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            pos = (position[0] + i, position[1] + j)
            if pos[0] in range(len(self.mat)) and pos[1] in range(len(self.mat[0])):
                neighbours.append(pos)
        return neighbours

    def get_cluster(self, point, cluster=[]):
        cluster.append(point)
        nbs = self.get_neighbours(point)
        print(nbs)
        dot_nbs = []
        for n in nbs:
            point = self.mat[n[0]][n[1]]
            if point == "." and n not in cluster:
                dot_nbs.append(n)
        for dn in dot_nbs:
            self.get_cluster(dn, cluster)
        return cluster

    def solution(self):
        print(self.get_cluster(self.dots[6]))


ff = FloodFill(lines, maze_positions)
ff.solution()

"""
class FloodFill:
    maze = []
    enclosed = []
    free = []
    unseen = []
    TO_CLASSIFY = []  # dots
    matrix = []

    def __init__(self, seen, matrix) -> None:
        all_pos = [
            (i, j) for i, j in it.product(range(len(matrix)), range(len(matrix[0])))
        ]
        self.maze = seen
        self.unseen = [tup for tup in all_pos if not tup in seen]
        self.TO_CLASSIFY = [
            (i, j)
            for i, j in it.product(range(len(matrix)), range(len(matrix[0])))
            if matrix[i][j] == "."
        ]
        self.to_classify = self.TO_CLASSIFY.copy()
        print("hey" + str(self.TO_CLASSIFY))
        assert len(self.unseen) + len(seen) == len(all_pos)
        self.matrix = matrix

    def get_neighbours(self, position):
        print(position)
        neighbours = []
        for i, j in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            pos = (position[0] + i, position[1] + j)
            if pos[0] in range(len(self.matrix)) and pos[1] in range(
                len(self.matrix[0])
            ):
                neighbours.append(pos)
        return neighbours

    def flood(self, pos, cluster=[]):
        if (
            pos in self.maze
            or pos in self.free
            or pos in self.enclosed
            or pos in cluster
        ):
            print("Fatal refeed")
            exit()
        print(f"reading {pos} with cluster {cluster}")

        cluster.append(pos)
        nbs = self.get_neighbours(pos)
        print(f"neighbours are {nbs}")
        if len(nbs) < 4:
            print("removing cluster because edge was found")
            [self.free.append(c) for c in cluster]
            [self.to_classify.remove(c) for c in cluster]
            return

        unvisited = [nb for nb in nbs if nb in self.to_classify and nb not in cluster]
        if len(unvisited) == 0:
            print("removing cluster because all neighbours known")
            [self.enclosed.append(c) for c in cluster]
            [self.to_classify.remove(c) for c in cluster]
            return

        print(f"recursing with {unvisited}")
        self.flood(unvisited[0], cluster)

    def solve(self):
        # If all neighbours are either in cluster or maze

        print(self.to_classify)
        while self.to_classify:
            print(f"{len(self.to_classify)} remaining")
            print(f"sending in {self.to_classify[0]}")
            self.flood(self.to_classify[0], [])
        print(len(self.enclosed))
        print(self.enclosed)
        [print(self.matrix[p[0]][p[1]]) for p in self.enclosed]"""
