# Value Iteration, Policy Evaluation:

In this assignment, we wanted to apply value iteration algorithm of Dynamic programming on several probelms and see how the convergence is achieved.

##MAZE PROBLEM

We have written a program, that given the starting point and goal point in a maze of arbitrary size, by value iteartion we find a path from starting to goal point.

Maze
-------------------------
In the following, you will see the execution on maze 5*5. We have listed each iteartion and it has taken 9 iteration for convergence.  
We have printed in each cell first the value (which is the estimated distance from the goal) and the action (depicted by arrow ) on that cell of maze:(The starting point is [1,1] location of maze. The goal is [5,5] location of maze)

Size Of Maze: 5*5
-------------------------
iteration: 1


|| -1 : ← || -1 : → || -1 : → || -1 : → || -1 : → || 

|| -1 : ← || -1 : → || -1 : → || -1 : → || -1 : → || 

|| -1 : ← || -1 : → || -1 : → || -1 : → || -1 : → || 

|| -1 : ← || -1 : → || -1 : → || -1 : → || -1 : → || 

|| -1 : ← || -1 : → || -1 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 2


|| -2 : ← || -2 : → || -2 : → || -2 : → || -2 : → || 

|| -2 : ← || -2 : → || -2 : → || -2 : → || -2 : → || 

|| -2 : ← || -2 : → || -2 : → || -2 : → || -2 : → || 

|| -2 : ← || -2 : → || -2 : → || -2 : → || -1 : ↓ || 

|| -2 : ← || -2 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 3


|| -3 : ← || -3 : → || -3 : → || -3 : → || -3 : → || 

|| -3 : ← || -3 : → || -3 : → || -3 : → || -3 : → || 

|| -3 : ← || -3 : → || -3 : → || -3 : → || -2 : ↓ || 

|| -3 : ← || -3 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -3 : ← || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 4


|| -4 : ← || -4 : → || -4 : → || -4 : → || -4 : → || 

|| -4 : ← || -4 : → || -4 : → || -4 : → || -3 : ↓ || 

|| -4 : ← || -4 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -4 : ← || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : ← || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 5


|| -5 : ← || -5 : → || -5 : → || -5 : → || -4 : ↓ || 

|| -5 : ← || -5 : → || -5 : → || -4 : → || -3 : ↓ || 

|| -5 : ← || -5 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -5 : ← || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : → || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 6


|| -6 : ← || -6 : → || -6 : → || -5 : → || -4 : ↓ || 

|| -6 : ← || -6 : → || -5 : → || -4 : → || -3 : ↓ || 

|| -6 : ← || -5 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -5 : → || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : → || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 7


|| -7 : ← || -7 : → || -6 : → || -5 : → || -4 : ↓ || 

|| -7 : ← || -6 : → || -5 : → || -4 : → || -3 : ↓ || 

|| -6 : → || -5 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -5 : → || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : → || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 8


|| -8 : ← || -7 : → || -6 : → || -5 : → || -4 : ↓ || 

|| -7 : → || -6 : → || -5 : → || -4 : → || -3 : ↓ || 

|| -6 : → || -5 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -5 : → || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : → || -3 : → || -2 : → || -1 : → || 0 : ← || 

-------------------------
iteration: 9


|| -8 : → || -7 : → || -6 : → || -5 : → || -4 : ↓ || 

|| -7 : → || -6 : → || -5 : → || -4 : → || -3 : ↓ || 

|| -6 : → || -5 : → || -4 : → || -3 : → || -2 : ↓ || 

|| -5 : → || -4 : → || -3 : → || -2 : → || -1 : ↓ || 

|| -4 : → || -3 : → || -2 : → || -1 : → || 0 : ← || 


As it can be seen, it took just 9 iteration to reach convergence.
If we increase the size of the maze, it can be seen that it take more time for convergence the log file consist of different maze size.



GAMBLING PROBLEM:
-------------------


Problem: A gambler bets on the outcomes of a sequence of coin flips. If the coin comes up heads, he wins as many dollars as he has staked on that flip; if it is tails, he loses his stake. The game ends when the gambler wins by reaching his goal of $100, or loses by running out of money. On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars. By value function we find optimal action of amount of betting based on the capital of gambler.

This is the result of action that should be taken based on capital for p=0.4:

![figure_1444](https://cloud.githubusercontent.com/assets/5707322/24595298/5a689706-1803-11e7-9911-8a319739c971.png)



