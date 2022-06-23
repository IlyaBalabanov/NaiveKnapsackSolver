class Solver:
    def __init__(self, costs, totalYears, yearsInUse,
                 costOfService, residualCost):
        self.W_cache = []
        self.costs = costs
        self.totalYears = totalYears
        self.yearsInUse = yearsInUse
        self.serviceCost = costOfService
        self.residualCost = residualCost

    def calculate(self):
        # оборудование и выбор на каждом шаге
        for i in range(self.totalYears):
            self.W_cache.append([-1, -1])
        # Фиктивный шаг
        self.W_cache.insert(0, [1, 0])

        # проходим по годам
        for stage in range(1, len(self.W_cache)):
            bestCost = None
            best_choice = None
            # проходим по вариантам выбора
            for state in range(len(self.costs)):
                # считаем стоимость замены
                currentCost = self.costs[state]
                # добавляем стоимость обслуживания
                if state == 0:
                    currentCost += self.serviceCost[self.W_cache[stage - 1][0] - 1][self.yearsInUse]
                else:
                    currentCost += self.serviceCost[state - 1][0]

                # вычитаем остаточную стоимость
                if state == 0:
                    currentCost -= self.residualCost[self.W_cache[stage - 1][0] - 1][
                        self.totalYears - stage + self.yearsInUse]
                else:
                    currentCost -= self.residualCost[state - 1][self.totalYears - stage]

                if bestCost is None or currentCost < bestCost:
                    bestCost = currentCost
                    best_choice = state

            # выбираем нужный тип оборудования
            best_equip = None
            if best_choice == 0:
                best_equip = self.W_cache[stage - 1][0]
            else:
                best_equip = best_choice

            self.W_cache[stage] = best_equip, best_choice

            # актуализируем возраст оборудования
            if best_choice == 0:
                self.yearsInUse += 1
            else:
                self.yearsInUse = 1

        return self.W_cache[1:]


rc1 = [0, 10800, 9720, 8748, 7000, 5598, 4478, 3583, 2866, 2800, 2800]
rc2 = [0, 8550, 7695, 5540, 4432, 3545, 2800, 2200, 2200, 2200, 2200]
residualCost = [rc1, rc2]
m1 = [400, 480, 576, 691, 829, 995, 1194, 1433, 1500, 1500, 1500]
m2 = [600, 720, 936, 1216, 1460, 1752, 2100, 2100, 2100, 2100, 2100]
costOfService = [m1, m2]
costs = [0, 12500 + 550, 10500 + 550]

myself = Solver(costs, 6, 2, costOfService, residualCost)
result = myself.calculate()

while Solver(costs, 6, 2, costOfService, residualCost).calculate() == result:
    # print(costs)
    costs[1] -= 1

costs[1] += 1

print(result)
print(costs)


