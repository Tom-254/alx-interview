#!/usr/bin/python3
"""
N-Queens Solver

This module provides a function for solving the
N-Queens problem, which involves
placing N queens on an NxN chessboard such that no two queens threaten each
other. The function takes an integer N as input
and returns a list of solutions,
where each solution is a list of (row, column) pairs.

Functions:
    is_valid_position(board, row, col):
        Check if a position is valid for placing a queen on the board.
    put_next_queen(board, row):
        Try to place a queen on the next row of the board at a valid position.
    find_nqueens_solution(board, solutions=[]):
        Solve the N-Queens problem for a given
        board and append the solutions to
        the given list.
    find_solutions(n):
        Run the N-Queens solver for a given board size.

Example:
    To solve the N-Queens problem for a board of size 8, run the script as
    follows: $ python3 nqueens.py 8
"""

import sys


def is_valid_position(board, row, col):
    """check for validity of the queens position
    """
    b_size = len(board)
    if sum(board[row]) or sum([board[i][col] for i in range(b_size)]) != 0:
        return False

    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r, c = r + i, c + j
            if board[r][c]:
                return False
    return True


def put_next_queen(board, row):
    """Makes sure a queen is placed at a valid position
    """
    st, end = 0, len(board)
    if sum(board[row]) == 1:
        st = board[row].index(1) + 1
        board[row] = [0 for col in range(end)]

    for col in range(st, end):
        if is_valid_position(board, row, col):
            board[row][col] = 1
            return True
    return False


def find_nqueens_solution(board, solutions=[]):
    """Solves the nqueens problem

    Args:
        n (int): size of board
    """
    n = len(board)
    row = 0
    while row < n:
        if put_next_queen(board, row):
            row += 1
        else:
            if row - 1 < 0:
                break
            row -= 1
        if row == n:
            solutions.append([[row, board[row].index(1)] for row in range(n)])
            row -= 1

    if row == 0:
        return

    solutions.append([[row, board[row].index(1)] for row in range(n)])
    idx = board[0].index(1)
    if idx > -1:
        board = [[0 for _ in range(n)] for row in range(n)]
        board[0][idx] = 1
        find_nqueens_solution(board, solutions)


def find_solutions(n):
    """Find each solution and prints them
    """
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    find_nqueens_solution(board, solutions)
    for row in solutions:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        find_solutions(n)

    except ValueError:
        print('N must be a number')
        sys.exit(1)
