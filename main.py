
from klee_for_cigar import Klee
from GeneticAlgorithmModel import GeneticAlgorithmModel

if __name__ == "__main__" :

    FLAG_COUNT = 8 # Number of flags present in super mutant file
    REFERENCE_SOLUTION = "reference_solution.c"
    SUPER_MUTANT = "super_mutant.c"
    KLEE_TIME_LIMIT = 20
    LEARNING_TIME_LIMIT = 200
    POPULATION_SIZE = 5

    klee = Klee("solve", "int", " -max-time="+str(KLEE_TIME_LIMIT)+"s ")
    def fitness_function(state):
        counter_example_count = klee.get_fitness(REFERENCE_SOLUTION, SUPER_MUTANT, state)
        fitness_value =  1 / (1 + counter_example_count )
        print(f"State {state} : Fitness Value : {fitness_value}")
        return  fitness_value ## Weight inversely proportional to total number of counter examples obtained

    model = GeneticAlgorithmModel(POPULATION_SIZE, FLAG_COUNT, fitness_function=fitness_function)
    model.fit(LEARNING_TIME_LIMIT)