import numpy as np
# Parameter initialization
genes = 5
chromosomes = 4
mattingPoolSize = 3
offspringSize = chromosomes - mattingPoolSize
lb = -10
ub = 10
populationSize = (chromosomes, 1)
generations = 5

#Population initialization
population = np.random.uniform(lb, ub, populationSize)
print("population", population)

population_bin = [np.base_repr(int(c), base=2).zfill(5) if c >= 0 else '0' + np.base_repr(int(c), base=2)[1:].zfill(4) for c in population.flatten()]

print(population_bin)

for generation in range(generations):
    
    print(("Generation:", generation+1))
    fitness = []

    for c in population:
        fitness.append(eval("c**2 - 3*c + 4")[0])#np.sum(population*population, axis=1)

    print("\npopulation")
    print(population)
    print("\nfitness calcuation")
    print(fitness)
    # Following statement will create an empty two dimensional array to store parents
    parents = []

    # A loop to extract one parent in each iteration
    for p in range(mattingPoolSize):
        # Finding index of fittest chromosome in the population
        fittestIndex = np.where(fitness == np.max(fitness))
        # Extracting index of fittest chromosome
        fittestIndex = fittestIndex[0][0]
        # Copying fittest chromosome into parents array
        parents.append(population_bin[fittestIndex])
        
        # Changing fitness of fittest chromosome to avoid reselection of that chromosome
        fitness[fittestIndex] = -1
        print("\nParents:")
        print(parents)

    # Following statement will create an empty two dimensional array to store offspring
    offsprings = []
    
    for k in range(offspringSize):
        #Determining the crossover point
        crossoverPoint = np.random.randint(0,genes)
        print(f'crossoverPoint: {crossoverPoint}')

        # Index of the first parent.
        parent1Index = k%len(parents)

        # Index of the second.
        parent2Index = (k+1)%len(parents)
        
        offspring = ''

        # Extracting first half of the offspring
        offspring += parents[parent1Index][0: crossoverPoint]

        # Extracting second half of the offspring
        offspring += parents[parent2Index][crossoverPoint:]
        
        offsprings.append(offspring)
        
    print("\nOffspring after crossover:")
    print(offsprings)

    # Implementation of random initialization mutation.
    for index in range(offspring.shape[0]):
        randomIndex = np.random.randint(1,genes)
        randomValue = np.random.uniform(lb, ub, 1)
        offspring [index, randomIndex] = offspring [index, randomIndex] + randomValue
        print("\n Offspring after Mutation")
        print(offspring)

    population[0:parents.shape[0], :] = parents
    population[parents.shape[0]:, :] = offspring
    print("\nNew Population for next generation:")
    print(population)