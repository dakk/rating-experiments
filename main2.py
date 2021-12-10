import pygad
import numpy
import utils
import random
import math

data = utils.dataToList(utils.loadData())

def getPar(boat):
    loa = boat['boat']['sizes']['loa']
    beam = boat['boat']['sizes']['beam']
    draft = boat['boat']['sizes']['draft']
    displacement = boat['boat']['sizes']['displacement']
    genoa = boat['boat']['sizes']['genoa']
    main = boat['boat']['sizes']['main']
    age = 2022 - boat['boat']['year']
    return [loa, beam, draft, displacement, genoa, main, age]

def evalute(sol, boat):
    p = getPar(boat)
    return p[0] * sol[0] + p[1] * sol[1] + p[2] * sol[2] + p[3] * sol[3] + p[4] * sol[4] + p[5] * sol[5] + p[6] * sol[6] + sol[7]

def fitness_func(solution, solution_idx, boat=None):
    if boat is None:
        rboat = random.choice(data)
    else:
        rboat = boat
        
    try:
        output = evalute(solution, rboat)
        #print(output, rboat['rating']['gph'])
        fitness = 1. / numpy.abs(output - rboat['rating']['gph'])
        if fitness > 1.0:
            fitness = 1.0
        return fitness
    except Exception as e:
        return 0.0

def fitness_func2(solution, solution_idx):
    fit = 0.0
    n = 0
    for x in range(100):
        try:
            f = fitness_func(solution, solution_idx)
            fit += f
            n+=1
        except:
            f = 0.0

    ff = fit * 1. / float(n)
    if ff > 1:
        print(ff)
    return ff 


def fitness_func3(solution, solution_idx):
    fit = 0.0
    n = 0
    for x in data:
        try:
            f = fitness_func(solution, solution_idx, boat=x)
            fit += f
            n+=1
        except:
            f = 0.0

    ff = fit * 1. / float(n)
    if ff > 1:
        print(ff)
    return ff 
    

last_fitness = 0
def callback_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed), 
        "\tFitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]),
        "\tChange     = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))
    last_fitness = ga_instance.best_solution()[1]

    # b = random.choice(data)
    # prediction = evalute(ga_instance.best_solution()[0], b)
    # desider = b['rating']['gph']
    # print("Predicted output based on the best solution : {prediction} (desidered {desider})".format(prediction=prediction, desider=desider))


ga_instance = pygad.GA(num_generations=1000,
                       fitness_func=fitness_func3,
                       num_parents_mating=10,
                       sol_per_pop=20,
                       num_genes=8,
                       init_range_low=-4,
                       init_range_high=4,
                       mutation_type="adaptive",
                       parent_selection_type="sss",
                       crossover_type="scattered",
                       mutation_probability=(0.35, 0.17),
                    #    random_mutation_min_val=-16.0,
                    #    random_mutation_max_val=16.0,
                       on_generation=callback_generation,
                    #    mutation_num_genes=4
                       )

# Running the GA to optimize the parameters of the function.
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

b = random.choice(data)
prediction = evalute(solution, b)
desider = b['rating']['gph']
print("Predicted output based on the best solution : {prediction} (desidered {desider})".format(prediction=prediction, desider=desider))


ga_instance.plot_fitness(title="PyGAD with Adaptive Mutation", linewidth=5)
