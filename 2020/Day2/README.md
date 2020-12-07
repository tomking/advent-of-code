# Day Two

#### Challenge Overview
[The second challenge of 2020](https://adventofcode.com/2020/day/2) kept things simple. 
Part One: Given passwords and character requirements, verify that each password contains the specified character a number of times that falls in the given range.

Part Two: Given passwords and character requirements, verify that each password contains the specified character in one of the two given spots.

#### Input
My input for this puzzle can be found [here](./input.txt). An excerpt from it is as follows:
>   1-2 x: xpxc
    1-5 b: bwlbbbbcq
    3-5 v: qvjjdhvl
    9-12 t: ttfjvvtgxtctrntnhtt
    3-4 r: rqjw
#### Solution
My approach to this problem was pretty simple. I created three functions, one takes in a raw line of input and returns a dictionary representing the line. The other two take in one of these parsed input dictionaries and returns a bool representing whether or not the given dictionary is valid for the problem part that the functions corresponds to. `eval_parsed_password_policy1` is _very_ simple. It counts the number of occurrences of the specified character and return whether this count falls in the given range. `eval_parsed_password_policy2` has a boolean for each specified position. These bools show whether the character is present in each position and the return is therefore just the result of an `XOR` of them.

#### Thoughts and Conclusions
This was another simple problem that I found easy to approach. My solution as always could be more elegant, but it gets the job done. I found this challenge fine, not outstanding but certainly not disappointing.

#### (Specific) Things to Improve
- I don't love the names I used for the functions
