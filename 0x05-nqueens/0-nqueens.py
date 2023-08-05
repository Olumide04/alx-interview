#!/usr/bin/python3
<<<<<<< HEAD
"""N Queens"""
import sys


def print_board(board, n):
    """Print allocated positions to the queen"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def is_position_safe(board, i, j, r):
    """Checks if the position is safe for the queen"""
    return board[i] in (j, j - i + r, i - r + j)


def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if is_position_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
safe_positions(board, row, int(n))
=======
"""
The N Queens 
Show all possible ways to place N non-attacking Queens on an NxN board
"""

import sys
import math

solutions = []
can_place_count = [0]
nqueens_count = [0]

def can_place(board, row, col):
    """Checks if [row, col] is a safe position on the board"""
    can_place_count[0] += 1
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True


def nqueens(board, row, n):
    """O(n!) time, O(n) space"""
    nqueens_count[0] += 1
    if row == n:
        return solutions.append(board[:])
    for col in range(n):
        if can_place(board, row, col):
            board[row] = col
            nqueens(board, row + 1, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N") or exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number") or exit(1)
    if n < 4:
        print("N must be at least 4") or exit(1)
    nqueens([None] * n, 0, n)
    [print([[row, col] for row, col in enumerate(sol)]) for sol in solutions]
    print(n, can_place_count, nqueens_count, can_place_count[0]/nqueens_count[0], math.factorial(n), can_place_count[0]/(pow(2, n) + n))
>>>>>>> 598ac5dfd056f6fc6f8312889f7ee5bad299a592
