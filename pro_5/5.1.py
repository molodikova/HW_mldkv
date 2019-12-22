from pyeasyga.pyeasyga.pyeasyga import GeneticAlgorithm
import io
import json


# setup data
file_name = '10.txt'
data = []
with io.open(file_name) as f:
    for line in f:
        items = line.split(' ')
        if len(items) < 3:
            optimalWeight = int(items[0])
            optimalVolume = int(items[1])
        else:
            data.append([int(items[0]), float(items[1]), int(items[2])])

ga = GeneticAlgorithm(data,
                      population_size=200,
                      generations=20,
                      crossover_probability=0.8,
                      mutation_probability=0.05, elitism=True, maximise_fitness=True)  # initialise the GA with data


# define a fitness function
def fitness(individual, data):
    weight, volume, price = 0, 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > optimalWeight or volume > optimalVolume:
        price = 0

    return price


ga.fitness_function = fitness   # set the GA's fitness function
ga.run()                        # run the GA
ga_best = ga.best_individual()  # print the GA's best solution

select_best = [data[index] for index, bit in enumerate(ga_best[1]) if bit == 1]

output = {
    'Оптимальный объем': sum([item[0] for item in select_best]),
    'Оптимальный вес': round(sum([item[1] for item in select_best]), 2),
    'Оптимальная ценность': ga_best[0],
    'Список вещей': [' '.join(map(str, item)) for item in select_best]
}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)