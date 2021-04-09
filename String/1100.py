chess_board = []
for _ in range(8):
    chess_board.append(input())

count = 0
for row in range(8):
    for col in range(8):
        if row % 2 == 0 and col % 2 == 0:  # 흰검흰검흰검흰검
            if 'F' in chess_board[row][col]:
                count += 1
        elif row % 2 == 1 and col % 2 == 1:  # 검흰검흰검흰검흰
            if 'F' in chess_board[row][col]:
                count += 1

print(count)