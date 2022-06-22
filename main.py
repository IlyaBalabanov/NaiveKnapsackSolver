class NaiveKnapsackSolver:
    def __init__(self, mark, years, total):
        self.q1 = years
        self.q2 = mark
        self.p = total

    def W(self, stage, way):
        if stage > self.p:
            return 0, way

        best_w = None
        best_u = None
        best_way = None
        for u in range(3):
            if u == 0:
                self.q1 += 1

                wi = -1 * (self.q2 - 2) * m1[self.q1] + (self.q2 - 1) * m2[self.q1] + self.W(stage + 1, way + [0])[0]
                w = self.W(stage + 1, way + [0])[1]
                if printprom:
                  print(u, wi, self.q1, self.q2)
            elif u == 1:
                oldq1 = self.q1
                oldq2 = self.q2
                self.q1 = 0
                self.q2 = 1
                wi = m1[0] + zamena[0] - ostatok[oldq1][oldq2 - 1] + 550*(oldq2-1) + self.W(stage + 1, way + [1])[0]
                w = self.W(stage + 1, way + [1])[1]
                if printprom:
                  print(u, wi, self.q1, self.q2)
            elif u == 2:
                oldq1 = self.q1
                oldq2 = self.q2
                self.q1 = 0
                self.q2 = 2
                wi = m2[0] + zamena[1] - ostatok[oldq1][oldq2 - 1] - 550*(oldq2 - 2) + self.W(stage + 1, way + [2])[0]
                w = self.W(stage + 1, way + [2])[1]
                if printprom:
                  print(u, wi, self.q1, self.q2)
            if stage == self.p:
                    wi -= ostatok[self.q1][self.q2-1]
            if best_w is None or wi < best_w:
                best_w = wi
                best_u = u
                best_way = w
            #print(best_u)
        return best_w, best_way

    def solve(self):
        return self.W(0, [])

printprom = False
ostatok = [[0, 0], [10800, 8550], [9720, 7695], [8748, 5540], [7000, 4432], [5598, 3545],
           [4478, 2800], [3583, 2200], [2866, 2200], [2800, 2200], [2800, 2200]]
m1 = [400, 480, 576, 691, 829, 995, 1194, 1433, 1500, 1500, 1500]
m2 = [600, 720, 936, 1216, 1460, 1752, 2100, 2100, 2100, 2100, 2100]
zamena = [12500, 10500]

myself = NaiveKnapsackSolver(1, 2, 6)
solve = myself.solve()

oldvar = solve[1]
while myself.solve()[1] == oldvar:
  print(zamena)
  zamena[0] -= 10

print(solve)
print(zamena[0] + 1)