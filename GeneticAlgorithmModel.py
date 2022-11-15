import random
from datetime import datetime


class GeneticAlgorithmModel:

    
    def __init__(self, population_size, number_of_flags, fitness_function, mutate_percentage = 100) :

        self.population_size = population_size
        self.population = []
        self.population_fitness = []
        self.number_of_flags = number_of_flags
        self.best_fitness = 0
        self.best_state = []
        self.fitness_function = fitness_function
        self.mutate_percentage = mutate_percentage
        self.__generate_initial_population()

    def __update_best_model(func):
        
        def inner(self):
            func(self)
            for i in range(self.population_size):
                if self.population_fitness[i] > self.best_fitness :
                    self.best_fitness = self.population_fitness[i]
                    self.best_state = self.population[i]
        return inner

    @__update_best_model
    def __generate_initial_population(self):
        '''
        Method to populate intial set of states
        Each state is a boolean assignment to the flags
        if number_of_flags = 5 and population_size = 3
        population[[]] = [
            [T,T,T,F,F]
            [F,T,F,T,T]
            [T,F,F,T,T]
        ]
        '''
        population = [[]] * self.population_size
        population_fitness = [[]] * self.population_size

        for i in range(self.population_size) :
            state = [False] * self.number_of_flags
            for j in range(1, self.number_of_flags):
                state[j] = True if random.choice(range(2)) == 0 else False
            population[i] = state
            population_fitness[i] = self.__get_state_fitness(state)
        
        self.population = population
        self.population_fitness = population_fitness
       
    
    def __reproduce(self, parent1 : list, parent2 : list)  :
        '''
            Method to create two children state from two parent states
            Two point crossover method is used to create two children
            One bit of both the children states are then mutated (flipped) by a certain probability bit to add randomness (evolution)
            
        '''
        cps = random.choices(range(1, self.number_of_flags), k = 2) # two crossover points
        cps.sort()

        cp1, cp2 = cps[0], cps[1]

        child_state1 = parent1[ : cp1] + parent2[cp1 : cp2] + parent1[cp2 : ]
        child_state2 = parent2[ : cp1] + parent1[cp1 : cp2] + parent2[cp2 : ]

        child_state1 = self.__mutate_state(child_state1)
        child_state2 = self.__mutate_state(child_state2) 
        return [child_state1, child_state2]
       
    def __mutate_state(self, state):
        '''
            Method to mutate one location in state with small independent probability
        '''
        if (random.randint(0,99) < self.mutate_percentage):  #mutation probability
            pos = random.randint(0,self.number_of_flags - 1) # 0 indexing
            state[pos] = False if state[pos] == True else True 
           
        return state
    
    def __get_state_fitness(self, state) :
        return self.fitness_function(state) 

    @__update_best_model
    def generate_new_population(self):
        '''
            Method to produce next generation of States from previous States
            based on Fitness Function
        '''
        newPopulation = [[]] * self.population_size
        newFitness = [0] * self.population_size

        for i in range(self.population_size) :
            [parent1, parent2] = random.choices(self.population, weights = self.population_fitness, k = 2)
            [child1, child2] = self.__reproduce(parent1=parent1, parent2=parent2)

            child1_fitness, child2_fitness = self.__get_state_fitness(child1), self.__get_state_fitness(child2)

            newPopulation[i], newFitness[i] = (child1, child1_fitness) if child1_fitness > child2_fitness else (child2, child2_fitness)
           
        self.population = newPopulation
        self.population_fitness = newFitness

    
    def fit(self, time_limit, seed = -1):
        '''
            Method to execute the Genetic Algorithm Model
            Crossing Over keeps on taking place untill state with 100% fitness is produced 
            or execution time exceeds the TimeLimit provided 
        '''

        if time_limit<1:
            raise Exception("Time Limit has to be greater than or equal to 1 second")
        
        if seed != -1:
            random.seed(seed)   

        start_time = datetime.utcnow()
        
        while (datetime.utcnow() - start_time).total_seconds() < time_limit :
            print("Best state " , self.best_state)
            print("Best Fitness " , self.best_fitness)
            if self.best_fitness == 1 : 
                print("Early terminating as best case already reached")
                break
            else :
                self.generate_new_population()
                
        print(" \n\n\n \t\t ==== RESULT ====")

        print("Best state observed : ", self.best_state)
        print("Fitness Value : ", self.best_fitness)
        return self.best_state


