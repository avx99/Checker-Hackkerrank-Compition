# Hackkerrank-Competion-OS-Days

# Description
BattleCode Coding Competition is a coding competition which is organized
With the collaboration of the ENSA KHOURIBGA and  Competitive programming CLub (CPC) 1337 School.
Do participate to have a lot of fun! You are having a chance to win exciting prizes!


# Scoring
- Each challenge has a pre-determined score.
- A participant’s score depends on the answer, best answer got heighest score.
- If a participant submits more than one solution per challenge, then the participant’s score will reflect the highest score achieved.
- Participants are ranked by score. If two or more participants achieve the same score, then the tie is broken by the total time taken to submit the last solution resulting in a higher score

# the problem :
Mustapha wants to water his land using water sprinklers, he went to the market to buy the water sprinklers and he discovered that there are three types of water sprinklers:
- the type A: this type has one sprinkler
- the type B: this type has two sprinklers
- the type C: this type has three sprinklers
The farmer found a lot of problems to distribute those water sprinklers because he has a lot of areas with different shapes.
He decided to solve those issues using programming and he wants your helps, then he sent you a brief description of the problem:

The problem is to find a good distribution of water sprinklers in an area of (n*p) m² dimension given only some information about the number of sprinklers in every row and column.
To visualize the problem, we represent the area as a matrix with a dimension of (n,p) (n rows and p columns), this matrix contains only 0 or 1:

- 0 refers to the ground.
- 1 refers to a sprinkler:
  - If the type of the water sprinkler is A, we will have only 1.
  - If it’s B, we will have 1,1.
  - If it’s C, we will have 1,1,1.

## Input Format

- Argument 1: list of the number of sprinklers in every row (the length of this list is n).
- Argument 2: list of the number of sprinklers in every column (the length of this list is p):

```
1 3 1 0 4 1
4 0 1 3 1 1
```

## Constraints

- Water sprinklers can only be placed horizontally or vertically, they can only be made of the shape (1 row, x columns) or (x rows, 1 column), where 0 < x < 4.
- At least one horizontal or vertical cell separates two water sprinklers, a water sprinklers should be surrounded by the ground (that’s mean a water sprinklers should be surrounded by the ground).
- 0 < n < 500
- 0 < p < 500
