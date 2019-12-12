# CIIC5019 Project: NEAT Space Invaders
## Team Members

* María Cordero 
* Julio Aguilar
* Gabriel Huertas 
* Joshua Bonilla

### [Video Demo]
### [Presentation](https://docs.google.com/presentation/d/1K5FDjyiViDXawv6-YCb1B24nYeiwqAAlZtIuki3g7xc/edit?usp=sharing)
### [Report](https://docs.google.com/document/d/1RxljvcU4XT58aBntkjlcyxbxRdsjee1NB3b9SNrv-jg/edit?usp=sharing)

## Abstract
This corresponds to the final examination of the group project for the High Performance Computing class. It presents an example of how Neuroevolution of Augmenting Topologies (NEAT) algorithm, can be trained to play a modified version of the classic game Space Invaders. Also it will give an overview of how these neural networks work, and how they evolve to get better at playing the game. The results of the NEAT algorithm will then be discussed, finding ways to improve training and run time.


## Description
The main objective of this project is to train a neural network using a Neuroevolution of Augmenting Topologies (NEAT) algorithm to play Space Invaders using a reward system. Instead of relying on a fixed structure for a neural network, NEAT allows it to evolve through a genetic algorithm. This model will be trained so its decision making process gets it closer to beating the game, in other words, get the highest score possible. Although the game does continue for infinity, getting 500,000 points is a benchmark at which you beat the game.


## Neuroevolution Of Augmenting Topologies Algorithm
Neuroevolution (NE) searches through the space of behaviors for a network that performs well at a given task. This approach to solving complex control problems represents an alternative to statistical techniques that attempt to estimate the utility of particular actions in particular states of the world [5].  NEAT is designed to take advantage of structure as a way of minimizing the dimensionality of the search space of connection weights and, if done right, evolving structure along with connection weights can significantly enhance the performance of NE.The real gain in performance with this approach is through the evolution of the structure. If the structure is evolved such that topologies are minimized and grown incrementally, significant gains in learning speed result. Improved efficiency results from topologies being minimized throughout evolution, rather than only at the very end.


## References
1. ClassicGaming.cc. “Space Invaders: Resources, Images and Material from the Classic Arcade Game.” Space Invaders | Resources, Images and Material from the Classic Arcade Game, www.classicgaming.cc/classics/space-invaders/history.php.
2. Heidenreich, Hunter. “NEAT: An Awesome Approach to NeuroEvolution.” Medium, Towards Data Science, 10 Jan. 2019, towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f.


-----

*neat-in-space-invaders created by Lairson Melo Filho and Onildo João Costa

