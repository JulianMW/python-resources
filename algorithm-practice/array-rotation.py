"""

A left rotation operation on an array of size shifts each of the array's elements unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of integers and a number, , perform left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of (the number of integers) and (the number of left rotations you must perform).
The second line contains space-separated integers describing the respective elements of the array's initial state.

Constraints
1<=n<=10**5
1<=d<=n
a[i] <=10**6

Output Format

Print a single line of space-separated integers denoting the final state of the array after performing left rotations.

Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4

Explanation

When we perform 1 left rotations, the array undergoes the following sequence of changes:

[1,2,3,4,5] --> [5,1,2,3,4]

"""



def array_left_rotation(a, n, k):
    end = a[k:]
    start = a[:k]
    out = end+start
    return out
