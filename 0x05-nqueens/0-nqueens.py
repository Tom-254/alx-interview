#!/usr/bin/python3
"""A program that solves the N-Queens puzzle.

The N-Queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard.

Usage:
    python nqueens.py N

where N must be an integer greater or equal to 4.

If the user called the program with the wrong number of arguments, print Usage:
nqueens N, followed by a new line, and exit with the status 1.

If N is not an integer, print N must be a number, followed by a new line, and
exit with the status 1.

If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1.

The program should return an array of every possible solution to the problem.
"""

import sys


def nqueens(n):
    """Solve the N-Queens puzzle and return an
    array of every possible solution.

    Args:
        n (int): The size of the board and the number of queens to place.

    Raises:
        SystemExit: If N is not an integer, or if N is smaller than 4.

    Returns:
        List[List[int]]: A list of every possible
        solution to the N-Queens puzzle.
    """
    # Check that n is an integer greater or equal to 4
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    # Recursive function to place queens
    def place_queen(row, col):
        """Recursively place queens on the board.

        Args:
            row (int): The row to place the queen in.
            col (int): The column to place the queen in.
        """
        # Check if this position is attacked by any previous queens
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - row + i >= 0 and board[i][col - row + i] == 'Q':
                return False
            if col + row - i < n and board[i][col + row - i] == 'Q':
                return False

        # Place the queen
        board[row][col] = 'Q'

        # If this is the last row, add the solution to the list
        if row == n - 1:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        solution.append([i, j])
            solutions.append(solution)
        else:
            # Try placing a queen in the next row
            for i in range(n):
                place_queen(row + 1, i)

        # Remove the queen
        board[row][col] = '.'

    # Try placing a queen in each column of the first row
    for i in range(n):
        place_queen(0, i)

    return solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solutions = nqueens(n)
for solution in solutions:
    print(solution)
