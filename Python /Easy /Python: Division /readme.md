https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example


The result of the integer division .
The result of the float division is .
Print:

0
0.6
Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
Language
Python 3
More
12345678
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    integer_division = a//b
    float_division =a/b
    print(integer_division)
    print(float_division)

Line: 8 Col: 1

Test against custom input