# import numpy as np
import pygame
import scipy 
import neat
import configparser, os
        
# s = "the dry lake"
# print(s[4:7])

class GalagaAI(object):
    
    def __init__(self):
        # config = configparser.ConfigParser()
                
        neat.Config(genome_type=neat.DefaultGenome,reproduction_type=neat.DefaultReproduction,species_set_type=neat.DefaultSpeciesSet, stagnation_type=neat.DefaultStagnation, filename='config.cfg')
        # self.showConfig(config)
    
    def showConfig(self, config): #Genome type, reproduction_type, species_set_type, stagnation_type
        return config
    
    
    #They should all be able to parse config file
    #Genome type - > Genome Interface 
    #Reproduction type -> Default Reproduction (from Interface)
    #Default Stagnation -> (class) 
G = GalagaAI()

G.__init__()

   
   
# truth = "beauty"
# index = 0
# letters = []
# while index < len(truth):
#     letters.append(truth[index])
#     index += 2

# letters = '-'.join(letters)
# print(letters)
