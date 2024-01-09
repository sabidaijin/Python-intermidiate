"""文字列で作って、それを二次元配列にして、形を整えて、それがlistにあるかどうかチェックするという
順序で作った。難しかったのは、チェックする手順を実装できなかった。全部作ってることになっていて意味ない。"""

# チェックするのはなんて目のグループかという中だけでいい。fulllistは二次元配列にして[k][0000000]って感じだ

def makeboard(new_prefix, remaining_digits,k):
    # boardを作る
    
    if remaining_digits == 0:
       print(new_prefix)
       return kcheack(new_prefix,k)           
    
    for digit in range(3):
        new_prefix =  + str(digit)
        makeboard(new_prefix, remaining_digits - 1)
    # これで現在のstateがわかる
 
                

def kcheack(board,k):
    boardlist=[]
    for i in range(0,len(board)):
        count=n**2#例えば9ますだったら、0が一つもない=９手目を実行した後ということになる。
        if board[i]==0:
            count=count-1
        if count==k:
            boardlist.append(board)
        if count>k:
            return boardlist
    return boardlist

    

def countpattern(n): 
    allboard=[]
    # kは手数
    # iはその手数目で現れるパターンのインデックス
    for k in range(1,n**2):
        for i in range(0,n**2-k):
            # k手目の状況を全て作る(全てというのはn**2-1)
            # k手目の状況をチェックさせる
            list=makeboard("", n**2,k)
            print(list)
            is_new_patterns(list[i],n,allboard)
            # makeboardでboardを作ってもらってそれを配列型で返してもらう
            # 配列の中身を一つずつ渡していってパターンをチェックしてもらう
    return count;

def is_new_patterns(board,n,allboards):
    
    flag=0
    # 文字列を２次元配列に
    columns = n
    matrixboard=[]
    for i in range(0, len(board), columns):
        row = board[i:i+columns]
        matrixboard.append(row)

    # 作ったものが新しいパターンかどうかを確認する。
    check90(matrixboard, allboards)
    check180(matrixboard, allboards)
    check270(matrixboard, allboards)
    checkv(matrixboard, allboards)
    check45(matrixboard, allboards)
    checkr45(matrixboard, allboards)

    # 全部チェック完了してこれが新しいパターンだと認識させれたらリストに足していく
    if flag==0:
        return 
    else:
        allboards.append(board)
            
    def check90(matrixboard, allboards):
        # 90度傾ける
       

    def check180(matrixboard, allboards):
        board180 = ["".join(row[::-1]) for row in matrixboard[::-1]]
        if any(board180 == board for board in allboards):
            global flag
            flag = 1

    def check270(matrixboard, allboards):
        # 270度傾ける→90度傾けたものを90度傾けてそれを90度傾ける

    def checkv(matrixboard, allboards):
        # 水平に折る→下の値と上の値を入れ替える
        boardV = matrixboard[::-1]
        if any(boardV == board for board in allboards):
            global flag
            flag = 1
    
    def check45(matrixboard, allboards):
        # 行列を転置させることで45度変換したものを作りそれがリストにあるか調査
        board45=[]
        for i in range(len(matrixboard)):
            board45_row = [row[i] for row in matrixboard]
            board45.append(board45_row)
        if any(board45 == board for board in allboards):
            global flag
            flag = 1

    def checkr45(matrixboard, allboards):
        boardr45=[]
        for i in range(len(matrixboard)):
            boardr45_row = [row[i] for row in matrixboard]
            boardr45.append(boardr45_row)
        if any(boardr45 == board for board in allboards):
            global flag
            flag = 1

            


n=int(input())
if n<3:
    print("値が小さすぎます")
    exit()
count=countpattern(n)
print(count)