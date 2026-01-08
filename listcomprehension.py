'''Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of
i + j + k is not equal to n. Here, 0 ≤ i ≤ æ; 0 ≤ j ≤ y; 0 ≤ k ≤ 2. Please use list comprehensions rather than multiple loops, as a learning exercise.

Example

y=1
z=2
n=3

All permutations of [i, j, k] are:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].
Print an array of the elements that do not sum to n. = 3.
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
Input Format

Four integers a, y, z and n, each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 
O

1

1

2

Sample Output O

[[O. 0, 0]. [0, 0, 1. [0, 1, 0]. [1, 0, O]. [1, 1, 1]]

Explanation O

Each variable z, y and z will have values of 0 or 1. All permutations of lists in the form [1, j, k] - [[0, 0, 0], [0, 0, 1], [0, 1, 0],[0, 1, 1], [1, 0, o], [1, 0, 1], [1,1,0], [1,1,1]].
Remove all arrays that sum to n. = 2 to leave only the valid permutations.

Sample Input 1

223

2

Sample Output 1

(IO. 0. 0]. [0. 0, 1]. [0, 1, 0]. [0. 1, 2]. [0, 2, 1]. [0. 2, 2]. [1, 0. 0]. [1, 0. 2]. [1, 1, 1]. [1, 1, 2]. [1, 2, O]. [1, 2, 1]. [1, 2, 2]. [2, 0, 1]. [2, 0. 2]. [2, 1, O]. [2, 1, 1], [2, 1, 2], [2, 2, O], [2, 2, 1], [2, 2, 2]]'''

#code:

 x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result=[[i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i+j+k!=n]
    print(result)