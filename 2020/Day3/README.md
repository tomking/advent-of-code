# Day Three

#### Challenge Overview
[2020's first challenge](https://adventofcode.com/2020/day/1) was quite simple. 
Part One: Given a list of numbers, find the product of the two entries that sum to 2020.
Part Two: Given the same list, find the product of the three entries that sum to 2020.

#### Input
My input for this puzzle can be found [here](./input.txt). An excerpt from it is as follows:
>   1778
    1845
    1813
    1889
    1939
#### Solution
My initial thought for this challenge was to take the most apparent route and iterate over my puzzle input with nested `for` loops. I decided to use this approach for both puzzles.

As visible in [my solution](./sol.py), I created two independent functions for each part of the puzzle. The first part's function checks the sum of an initial variable with each other variable until it finds a pair that sums to 2020, it then multiplies the pair and returns that value which my driver code prints to the console. The second part's function works in a very similar way with one extra loop layered into it in order to find the triplet that sums to 2020 rather than the pair.

#### Thoughts and Conclusions
I felt that this puzzle was simple enough that some nested `for` loops did it justice. Cleaning up the code a bit by abstracting each solution process into its own function seemed to make everything a bit neater. There are probably "better" ways to do this, but I don't see the need for them given the length of the puzzle input and the complexity of the code.