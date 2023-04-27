#!/usr/bin/python3
"""This module solves the N queens puzzle."""
import sys


def isdigit(n):
    """checks if a str is a digit"""
    for c in n:
        if not (ord(c) >= 48 and ord(c) <= 57):
            return False
    return True


def getSolutions(board):
    """get all solutions from board"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                solution.append([row, col])
    return solution


def optimalSolution(solutions):
    """returns the optional solution from all possible solutions"""
    optimals = []
    optimal = solutions[0]

    for solution in solutions:
        if len(solution) > len(optimal):
            optimal = solution
            optimals = [solution]
        elif len(solution) == len(optimal):
            optimals.append(solution)
    return optimals


def restrict(board, row, col):
    """restict areas covered by queen"""

    # horizontal
    for i in range(len(board[row])):
        if board[row][i] == 0:
            board[row][i] = -1

    # vertical
    for i in board:
        if i[col] == 0:
            i[col] = -1

    # right diagnoal
    j = col
    for i in range(row, len(board)):
        if j < len(board):
            if board[i][j] == 0:
                board[i][j] = -1
        j += 1

    # left diagonal
    j = col
    for i in range(row, len(board)):
        if j >= 0:
            if board[i][j] == 0:
                board[i][j] = -1
        j -= 1


def placeQueen(board, row):
    """place queen on a given row"""
    for col, d in enumerate(board[row]):
        if d == 0:
            board[row][col] = 1
            restrict(board, row, col)
            break


def nQueens(board):
    """solves the nqueens problem"""
    for row in range(len(board)):
        placeQueen(board, row)


def main():
    """Program entry point"""
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    if not isdigit(N):
        print("N must be a number")
        sys.exit(1)

    n = int(N)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    for i in range(n):
        board = [[0 for col in range(0, n)] for row in range(0, n)]
        board[0][i] = 1
        restrict(board, 0, i)
        nQueens(board)
        solutions.append(getSolutions(board))
    for optimal in optimalSolution(solutions):
        print(optimal)


if __name__ == "__main__":
    main()
