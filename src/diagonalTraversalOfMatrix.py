'''
Diagonal Traversal of Matrix
Given a 2D matrix of size NxN, print the sum of the elements of all its diagonals.

Input Format

First line of input contains T - number of test cases. First line of each test case contains N - size of the matrix. Each of the next N lines contains N integers - the elements of the matrix.

Constraints

1 <= T <= 100
1 <= N <= 100
-100 <= ar[i][j] <= 100

Output Format

For each test case, print the sum of the elements of all the diagonals, separated by newline. Refer samples for more clarity.

Sample Input 0

4
3
-5 0 4 
2 8 -6 
3 7 1 
1
-4 
2
5 -2 
-4 1 
6
-2 -3 -6 -5 50 3 
8 7 10 -5 -3 30 
6 3 70 9 -20 -7 
-9 9 -6 7 3 2 
-1 7 7 6 -4 3 
8 5 6 -9 40 8 
Sample Output 0

4 -6 4 9 3 
-4 
-2 6 -4 
3 80 -15 -29 22 86 51 13 4 4 8 
Explanation 0

Test Case 1
Sum of the elements of the 1st diagonal: 4
Sum of the elements of the 2nd diagonal: 0 + -6 = -6
Sum of the elements of the 3rd diagonal: -5 + 8 + 1 = 4
Sum of the elements of the 4th diagonal: 2 + 7 = 9
Sum of the elements of the 5th diagonal: 3

Test Case 2
Sum of the elements of the 1st and only diagonal: -4

Test Case 3
Sum of the elements of the 1st diagonal: -2
Sum of the elements of the 2nd diagonal: 5 + 1 = 6
Sum of the elements of the 3rd diagonal: -4
'''

def diagonalTraversalOfMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                print(matrix[i][j], end = " ")
    print()
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                print(matrix[i][j], end = " ")
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        diagonalTraversalOfMatrix(matrix)
