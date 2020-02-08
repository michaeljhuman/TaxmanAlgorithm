# TaxmanAlgorithm
Some taxman game algorithms compared.  Code is Python

I created a number of algorithms to play the "taxman game"

Taxman is a very simple game.  
You choose a number, with more than one factor besides itself, from a set of natural numbers 1 to N
You add that number to your score
The "taxman" gets all the factors of that number
When you can no longer choose valid numbers, the taxman gets the numbers not yet chosen

```
Sample:
Algorithm: tm3; n: 25
myChoice:  23
myChoice:  25
myChoice:  15
myChoice:  21
myChoice:  14
myChoice:  22
myChoice:  20
myChoice:  16
myChoice:  12
myChoice:  18
Player took:  [23, 25, 15, 21, 14, 22, 20, 16, 12, 18]
Taxman took:  [1, 5, 3, 7, 2, 11, 10, 4, 8, 6, 9, 13, 17, 19, 24]
MyScore: 186; Taxman: 139; Differences: 47
```
