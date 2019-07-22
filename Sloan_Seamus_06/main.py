from constant import POPULATION_SIZE
from constant import BEST_POSSIBLE_FIT
from constant import BEST_POSSIBLE_X
from constant import WORST_POSSIBLE_FIT
from constant import WORST_POSSIBLE_X
from belief_space import Belief
from population_space import Population


def quick_sort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0].fitness
        for value in arr:
            if value.fitness < pivot:
                less.append(value)
            elif value.fitness == pivot:
                equal.append(value)
            elif value.fitness > pivot:
                greater.append(value)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return arr


def declare_elite(arr):
    temp = []
    for i in range(int(POPULATION_SIZE / 5), 0, -1):
        temp.append(arr[-i])
    return temp


current_population = []
current_elite_population = []
current_belief = None

"""Create the population"""
for i in range(50):
    temp = Population()
    current_population.append(temp)

"""Sort the current population and declare the elites of the population"""
current_population = quick_sort(current_population)
current_elite_population = declare_elite(current_population)

"""Update the beliefs based on the generated population"""
current_belief = Belief()
current_belief.update_situational(current_elite_population)
current_belief.update_normative(current_population[0], current_population[POPULATION_SIZE - 1])

if current_elite_population[POPULATION_SIZE - 1].x == BEST_POSSIBLE_X:
    quit()

for solution in current_population:
    print(solution.x, solution.fitness)

print("\n\n\nSituational: ", current_belief.situational_knowledge)
print("Norm_Min: ", current_belief.normative_knowledge_min)
print("Norm_Max: ", current_belief.normative_knowledge_max)

