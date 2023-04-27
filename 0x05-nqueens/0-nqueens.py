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
    place_next_queen(board, row):
        Try to place a queen on the next row of the board at a valid position.
    solve_nqueens(board, solutions=[]):
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
    """Check if a position is valid for placing a queen on the board.

    Args:
        board (list[list[int]]): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if the position is valid, False otherwise.
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


def place_next_queen(board, row):
    """Place a queen on the next row of the board at a valid position.

    Args:
        board (list[list[int]]): The current state of the board.
        row (int): The current row to place the queen.

    Returns:
        bool: True if a valid position was found and a queen was placed, False
              otherwise.
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


def solve_nqueens(board, solutions=[]):
    """Solve the N-Queens problem for a given board.

    Args:
        board (list[list[int]]): The current state of the board.
        solutions (list[list[tuple[int, int]]], optional):
        The list of solutions.
            Defaults to [].

    Returns:
        list[list[tuple[int, int]]]: The list of solutions.
    """
    b_size = len(board)
    if sum([sum(row) for row in board]) == b_size:
        solution = [(i, row.index(1)) for i, row in enumerate(board)]
        solutions.append(solution)
        return solutions

    for i in range(b_size):
        if place_next_queen(board, i):
            solve_nqueens(board, solutions)
            board[i] = [0 for col in range(b_size)]

    return solutions


def find_solutions(n):
    """Run the N-Queens solver for a given board size.

    Args:
        n (int): The size of the board.

    Returns:
        list[list[tuple[int, int]]]: The list of solutions.
    """
    if n < 1:
        print("Please enter a positive integer.")
        return

    board = [[0 for col in range(n)] for row in range(n)]
    solutions = solve_nqueens(board)
    print(f"Found {len(solutions)} solution(s):\n")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}\n")

    return solutions


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    find_solutions(n)
