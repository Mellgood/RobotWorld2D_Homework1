# Intelligent System Lab

## Homelab 1: 2D robot AI
This repo contains the code delivered for the Homelab 1 of the course held by professor De Gasperis @ UNIVAQ

## Project specs: (copy-paste from prof requirements)

Write an Object Oriented Python (3.6.X) program that:

* Simulates a 2D world made by a rectangular matrix of cells, containing walls, robots, or energy food.
* Each cell can contain: 0 : nothing,  RX : a robot indexed by  X, # : a wall section, o : energy food.
* Robots can wander around only through Nord, South, Est, West directions.
* A robot can only enter an empty cell or a cell with energy food.
* Each robot has a SENSE-THINK-ACT controller software architecture. Each robot may have its own THINK algorithm, different from the others.
* When a robot finds energy food in a cell were it enters, the simulator increases its score, the food is deleted and the cell is only occupied by the incoming robot.
* At each simulation step , record and print an ordered list of high scores of robots.
* When the food is all taken the simulation is ended.

## Even little projects need to be designed..
This is my very first project in Python and even if I don't like it at all, it doesn't mean I wrote some random lines of code hoping they will work.. :P
The Design work I did before writing any line of code saved me hours of headaches. The code is structured to delegate responsability deep to the correct classes in order to produce some system state advancement and give back to the main layer results.
I used the *Strategy Pattern* to make my code ready to the change introduced by different think algorithms. This way I have kept decoupled the Robot class from its think behaviour. The same thing may be done for the sense and the act algorithms but it was out of specifications request and it would not have been a good tradeoff to invest some time imlpementing Design Patterns on that stuffs.

The use of the Strategy Pattern allow to add more think behaviours respecting the *Open-Closed* and the *Liskov Substitution* Principles improving the general code quality.

## Conclusions
Using Python has been a nice challenge but I still do not feel confident with this language... I will continue to chose other languages in absence of some kind of constrain ;)


CC
