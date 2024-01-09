def makeboard(prefix, remaining_digits, allboard):
    if remaining_digits == 0:
        kcheack(prefix, allboard)
        return
    
    for digit in range(3):
        new_prefix = prefix + str(digit)
        makeboard(new_prefix, remaining_digits - 1, allboard)
    
def kcheack(board, allboard):
    allboard[board] = True

def countpattern(n):
    allboard = {}
    
    makeboard("", n**2, allboard)
    
    is_new_patterns(allboard, n)

def is_new_patterns(boards, n):
    fullboard = []
    
    for board in boards.keys():
        flag = 0
        columns = n
        matrixboard = []
        for i in range(0, len(board), columns):
            row = board[i:i+columns]
            matrixboard.append(row)
        
        if check90(matrixboard, fullboard):
            if check180(matrixboard, fullboard):
                if check270(matrixboard, fullboard):
                    if checkv(matrixboard, fullboard):
                        if checkr45(matrixboard, fullboard):
                            if checkr45(matrixboard, fullboard):
                                fullboard.append(matrixboard)

                                print(len(fullboard))  # 修正: マトリックスボードを出力

def check90(matrixboard, allboards):
    board90 = [list(row) for row in zip(*matrixboard[::-1])]
    if not any(board90 == board for board in allboards):
        return True
    return False
     # 修正: 90度回転したボードを出力

def check180(matrixboard, allboards):
    board180 = ["".join(row[::-1]) for row in matrixboard[::-1]]
    if not any(board180 == board for board in allboards):
        return True
    return False
     # 修正: 180度回転したボードを出力

def check270(matrixboard, allboards):
    boardT = [list(row) for row in zip(*matrixboard[::-1])]
    board270 = ["".join(row[::-1]) for row in boardT[::-1]]
    if not any(board270 == board for board in allboards):
        return True
    return False
     # 修正: 270度回転したボードを出力

def checkv(matrixboard, allboards):
    boardV = matrixboard[::-1]
    if not any(boardV == board for board in allboards):
        return True
    return False
      # 修正: 垂直に反転したボードを出力

def checkr45(matrixboard, allboards):
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    boardT = transpose(matrixboard)
    boardr45 = ["".join(row[::-1]) for row in boardT]
    
    if not any(boardr45 == board for board in allboards):
        reversed_boardr45 = boardr45[::-1]
        if not any(reversed_boardr45 == board for board in allboards):
            return True
    
    return False



def checkr45(matrixboard, allboards):
    boardT = [list(row) for row in zip(*matrixboard)]
    boardr45 = ["".join(row[::-1]) for row in boardT]
    
    if not any(boardr45 == board for board in allboards):
        return True

    reversed_boardr45 = boardr45[::-1]
    if not any(reversed_boardr45 == board for board in allboards):
        return True
    
    return False


def check_horizontal_flip(matrixboard, allboards):
    flipped_board = matrixboard[::-1]
    if not any(flipped_board == board for board in allboards):
        return True
    return False


count = 0
n = int(input())
if n < 3:
    print("値が小さすぎます")
    exit()
countpattern(n)
