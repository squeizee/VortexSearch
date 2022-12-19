import random
import math
import numpy as np
import copy
import scipy.special as ss
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

import callFunction

# Algoritma Parametleri

func = callFunction.GetFunction(1)

print("Selected Function Name : ", func.name)

pSize = 50    # Çözüm sayısı
maxItr = 1e5  # Maksimum iterasyon
itr = maxItr  # İterasyon
dim = func.dim  # Boyut
upperLimit = func.upperLimit  # Üst limit
lowerLimit = func.lowerLimit  # Alt limit

# Popülasyon
population = []

xList = []
yList = []
rList = []


class Solution(object):
    def __init__(self):
        self.variables = []
        self.fitness = 0

    def function_objective(self):
        self.fitness = func.formula(self.variables)


Mu = .5 * (upperLimit + lowerLimit) * np.ones(dim)  # İlk merkez

x = .1
ginv = (1/x) * ss.gammaincinv(x, .999)
r = ginv * ((upperLimit - lowerLimit)/2)

globalBest = Solution()
globalBest.fitness = np.inf

def population_generator():
    for i in range(pSize):
        population.append(Solution())

def vortex_search():
    global r, ginv, Mu, globalBest, itr
    global xList, yList, rList

    for solution in population:
        C = r * np.random.randn()
        for dc in Mu:
            solution.variables.append(C + dc)


    for solution in population:
        for variable in solution.variables:
            if variable < lowerLimit or variable > upperLimit:
                variable = random.uniform(0, 1) * (upperLimit - lowerLimit) + lowerLimit


    for solution in population:
        solution.function_objective()

    population.sort(key=lambda x: x.fitness)

    if population[0].fitness < globalBest.fitness:
        globalBest = copy.deepcopy(population[0])

    xList.append(globalBest.variables[0])
    yList.append(globalBest.variables[1])
    rList.append(r)

    print(globalBest.variables, globalBest.fitness, r)

    Mu = copy.deepcopy(globalBest.variables)

    itr -= 1

    # Yarıçap azaltma
    a = itr / maxItr
    ginv = (1 / x) * ss.gammaincinv(x, a)
    r = ginv * ((upperLimit - lowerLimit) / 2)

    population.clear()


def main():
    for i in range(int(maxItr)):
        print("\nIterasyon %s\n" %i)
        population_generator()
        vortex_search()

    fig, ax = plt.subplots()

    ax.set_xlim((-750, 750))
    ax.set_ylim((-750, 750))

    for i in range(len(xList)):
        circle = plt.Circle((xList[i], yList[i]), rList[i], color=np.random.rand(3, ), fill=False)
        ax.add_artist(circle)
    plt.show()


main()
