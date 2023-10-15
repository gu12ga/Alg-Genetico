import numpy as np

def chance(c):
  if np.random.randint(0, 100) <= c:
    return True
  else:
    return False
  
genes = 5
chromosomes = 4
lb = -10
ub = 10
populationSize = (chromosomes, 1)
generations = 5

#Population initialization
population = np.random.uniform(lb, ub, populationSize)


population_bin_aux = [format(int(num), '05b') for num in population.flatten()]
population_bin = []

for i in range(4):
    binary_str = ""
    if population_bin_aux[i][0] == '-':
        for j in range(1,5):
            binary_str += population_bin_aux[i][j]
        population_bin.append("1" + binary_str)
    else:
        for j in range(1,5):
            binary_str += population_bin_aux[i][j]
        population_bin.append("0" + binary_str)


print(population_bin)
print(population)

for generation in range(generations):

  print(("Generation:", generation + 1))
  fitness = []

  for c in population:
    cf = float(c[0])
    fitness.append(
        eval("cf**2 - 3*cf + 4"))  #np.sum(population*population, axis=1)

  # Following statement will create an empty two dimensional array to store parents
  parents = []

  # A loop to extract one parent in each iteration
  ultimo = ""
  penultimo = ""
  for p in range(0,4):
    # Finding index of fittest chromosome in the population
    fittestIndex = np.where(fitness == np.max(fitness))
    
    if p == 3:
      ultimo = population_bin[fittestIndex[0][0]]
    if p == 2:
      penultimo = population_bin[fittestIndex[0][0]]
    # Extracting index of fittest chromosome
    fittestIndex = fittestIndex[0][0]

   
    # Copying fittest chromosome into parents array
    parents.append(population_bin[fittestIndex])

    # Changing fitness of fittest chromosome to avoid reselection of that chromosome
    fitness[fittestIndex] = -1

  # Following statement will create an empty two dimensional array to store offspring
  if chance(70):

    crossoverPoint = 3

    # Index of the first parent.
    parent1Index = 0

    # Index of the second.
    parent2Index = 1

    offspring = ''
    
    # Extracting first half of the offspring
    offspring += parents[parent1Index][0:crossoverPoint]

    # Extracting second half of the offspring
    offspring += parents[parent2Index][crossoverPoint:]

    for i in range(0, 4):
      
      if int(population_bin[i], 2) == int(ultimo, 2):
        population_bin[i] = offspring
        break
      
    offspring = ''
    offspring += parents[parent2Index][0:crossoverPoint]
    offspring += parents[parent1Index][crossoverPoint:]
    for i in range(0,4):
     if int(population_bin[i], 2) == int(penultimo, 2):
          population_bin[i] = offspring
       
  if chance(50):

    randomIndexG = 0
    randomIndexC = np.random.randint(0, chromosomes - 1)
    
    if population_bin[randomIndexC][1] == '0':
        
        randomIndexG = np.random.randint(0, genes-2)
        
        if randomIndexG != 0:
            randomIndexG += 1
    
    else:
        
        aux = []
        
        for i in range(0, len(population_bin[randomIndexC])):
            
            if i == 1:
                continue
            elif population_bin[randomIndexC][i] == '1':
                aux.append(i)
                
        if len(aux) == 0:
            
            for i in range(0,5):
                aux.append(i)
        
        randomIndexG = np.random.choice(aux)
        print(population_bin[randomIndexC])
        print(randomIndexG)         

    if population_bin[randomIndexC][randomIndexG] == '0':
      mutated_c = population_bin[
          randomIndexC][:randomIndexG] + '1' + population_bin[randomIndexC][
              randomIndexG + 1:]
    else:
      mutated_c = population_bin[
          randomIndexC][:randomIndexG] + '0' + population_bin[randomIndexC][
              randomIndexG + 1:]

    population_bin[randomIndexC] = mutated_c


  # Converting population_bin into population
  binary_str = ""
  population = []
  for j in range(0,4):
      if population_bin[j][0] == '1':     
        for i in range(1,5):
          binary_str += population_bin[j][i]
        population.append([-int(binary_str,2)])
        binary_str = ""
         
      else:
        for i in range(1,5):
          binary_str += population_bin[j][i]
        population.append([int(binary_str,2)])
        binary_str = ""
  np.array(population)
  print(population)
