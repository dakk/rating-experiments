import pygad
import numpy
import utils
import random
import math

data = utils.dataToList(utils.loadData())

# Operators
ADD = 1
SUB = 2
MUL = 3
DIV = 4
PARO = 5
PARC = 6
SQRTO = 14
SQRTC = 15

# LOA, BEAM, DRAFT, DISPLACEMENT, GENOA, MAIN, AGE
LOA = 7
BEAM = 8
DRAFT = 9
DISPLACEMENT = 10
GENOA = 11
MAIN = 12
AGE = 13

def evalute(sol, boat):
    loa = boat['boat']['sizes']['loa']
    beam = boat['boat']['sizes']['beam']
    draft = boat['boat']['sizes']['draft']
    displacement = boat['boat']['sizes']['displacement']
    genoa = boat['boat']['sizes']['genoa']
    main = boat['boat']['sizes']['main']
    age = 2022 - boat['boat']['year']

    fu = '1+'
    lastIsOp = True
    lastIsNum = False

    for xx in sol:
        x = int(xx)
        
        if x == PARO:
            if lastIsNum:
                continue
            fu += '('
            lastIsNum = False
            lastIsOp = True
        elif x == PARC:
            if lastIsNum:
                continue
            fu += ')'
            lastIsNum = True
            lastIsOp = False
        elif x == ADD:
            if lastIsOp:
                continue
            fu += '+'
            lastIsOp = True
            lastIsNum = False
        elif x == SUB:
            if lastIsOp:
                continue
            fu += '-'
            lastIsOp = True
            lastIsNum = False
        elif x == MUL:
            if lastIsOp:
                continue
            fu += '*'
            lastIsOp = True
            lastIsNum = False
        elif x == DIV:
            if lastIsOp:
                continue
            fu += '/'
            lastIsOp = True
            lastIsNum = False
        elif x == SQRTO:
            if lastIsNum:
                continue
            fu += 'math.sqrt('

        elif x == SQRTC:
            fu += ')'
        elif x == LOA:
            if lastIsNum:
                continue
            fu += 'loa'
            lastIsNum = True
            lastIsOp = False
        elif x == BEAM:
            if lastIsNum:
                continue
            fu += 'beam'
            lastIsNum = True
            lastIsOp = False
        elif x == DRAFT:
            if lastIsNum:
                continue
            fu += 'draft'
            lastIsNum = True
            lastIsOp = False
        elif x == DISPLACEMENT:
            if lastIsNum:
                continue
            fu += 'displacement'
            lastIsNum = True
            lastIsOp = False
        elif x == GENOA:
            if lastIsNum:
                continue
            fu +=   'genoa'
            lastIsNum = True
            lastIsOp = False
        elif x == MAIN:
            if lastIsNum:
                continue
            fu += 'main'
            lastIsNum = True
            lastIsOp = False
        elif x == AGE:
            if lastIsNum:
                continue
            fu += 'age'
            lastIsNum = True
            lastIsOp = False
        elif x < 0 and x > -4:
            if lastIsNum:
                continue
            fu += str(math.fabs(xx))
            lastIsNum = True
            lastIsOp = False
        else:
            pass # NOP
        fu += ' '
    
    # print(fu)
    return fu, eval(fu)


def fitness_func(solution, solution_idx):
    # Get a random element of data
    fitness = 0
    n = 10.
    for x in range(int(n)):
        rboat = random.choice(data)

        # Get the distance between the solution and the random element
        try:
            f, output = evalute(solution, rboat)
            print(f, output, rboat['rating']['gph'])
            fitness += numpy.abs(output - rboat['rating']['gph'])
        except Exception as e:
            fitness += 0.0
    
    if fitness == 0:
        return 0.0
    return 1./(fitness/n)



ga_instance = pygad.GA(num_generations=600,
                       fitness_func=fitness_func,
                       num_parents_mating=10,
                       sol_per_pop=40,
                       num_genes=100,
                       gene_type=int,
                       random_mutation_min_val=-10,
                       random_mutation_max_val=20,
                       #    initial_population=ipop,
                       gene_space = {"low": -3, "high": 20, "step": 1},
                       mutation_type="random",
                       mutation_num_genes=6)

# Running the GA to optimize the parameters of the function.
ga_instance.run()

ga_instance.plot_fitness(title="PyGAD with Adaptive Mutation", linewidth=5)
