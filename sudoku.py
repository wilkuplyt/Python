import random

def is_valid(board, row, col, num, N):
    # Check the row
    for i in range(N):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(N):
        if board[i][col] == num:
            return False

    # Check the sub-grid
    sqrt_N = int(N ** 0.5)
    start_row = row - row % sqrt_N
    start_col = col - col % sqrt_N
    for i in range(sqrt_N):
        for j in range(sqrt_N):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board, N):
    empty = find_empty_location(board, N)
    if not empty:
        return True
    row, col = empty

    for num in range(1, N+1):
        if is_valid(board, row, col, num, N):
            board[row][col] = num
            if solve_sudoku(board, N):
                return True
            board[row][col] = 0

    return False

def find_empty_location(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if random.random() < 0.3:  
                num = random.randint(1, N)
                if is_valid(board, i, j, num, N):
                    board[i][j] = num
    
    return board

def print_board(board, N):
    sqrt_N = int(N ** 0.5)
    for i in range(N):
        if i % sqrt_N == 0 and i != 0:
            print("-" * (N * 2 + sqrt_N - 1))
        for j in range(N):
            if j % sqrt_N == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def play_sudoku():
    N = int(input("Enter the size of the Sudoku square (e.g. 9 for a 9x9 grid): "))
    
    board = generate_sudoku(N)
    print("Generated Sudoku board:")
    print_board(board, N)
    
    see_solution = input("Do you want to see the solution? (yes/no): ").lower()

    if see_solution == "yes":
        if solve_sudoku(board, N):
            print("Sudoku solution:")
            print_board(board, N)
        else:
            print("Could not solve the Sudoku.")
    else:
        print("You can try solving the Sudoku on your own!")
    
if __name__ == "__main__":
    play_sudoku()
