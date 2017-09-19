class MazeEnvironmentV1:

    def __init__(self):
        self.width = 20
        self.height = 10
        self.walls = set({
            (2,0), (2,1), (2,2), (2,3), (2,4), (2,5)
        })
        self.start_pos = (0,0)
        self.end_pos = (19,9)

        self.x = 0
        self.y = 0

    def reset(self):
        self.x = 0
        self.y = 0

    def step(self, action):
        dx, dy = [(0,-1),(1,0),(0,1),(-1,0)][action]
        if self._is_inside(self.x+dx, self.y+dy) and not self._is_wall(self.x+dx, self.y+dy):
            self.x += dx
            self.y += dy

    def is_end(self):
        end_x, end_y = self.end_pos
        return self.x == end_x and self.y == end_y

    def render(self):
        BLOCK = 'X'
        res = BLOCK * (self.width+2) + '\n'
        for y in range(self.height):
            res += BLOCK
            for x in range(self.width):
                if self._is_wall(x,y):
                    res += 'X'
                elif self.x == x and self.y == y:
                    res += 'P'
                elif x == self.end_pos[0] and y == self.end_pos[1]:
                    res += 'E'
                else:
                    res += '.'
            res += BLOCK + '\n'
        res += BLOCK * (self.width+2)
        print(res)

    def _is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def _is_wall(self, x, y):
        return (x,y) in self.walls
