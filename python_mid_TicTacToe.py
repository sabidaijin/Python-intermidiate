#!/usr/bin/env python3


import random


class TicTacToe:
    def __init__(self,n):
        # サイズは入力と同じ値にする。stringだと扱いにくいのでintに変換する。
        self.size = int(n)
        # 1回目のプレーヤーは1番だから、最初から２を入れておく
        self.next = 2
        # ゲームの進行中として0を入れておく
        self.state=0

        self.board_dict={}
        #リストを生成
        self.board_list=[]

        # 先生の方に合わせて一次元リストでやってみる
        # self.inner_list=[]
        # # これで二次元のリストができた
        # for i in range(self.size):
        #     self.inner_list.append(i)
        #     self.board_list.append(self.inner_list)

        # 辞書形式で生成
        # 辞書の指定個数は入力の二乗-1
        for i in range(0,self.size*2-1):
            self.board_dict[i]= None

        # 最初はwinnerを0に設定しておく、
        self.winner = 0
    
    def play(self,player, x, y=None):
        
        # 座標
        # もしも指定されたところがサイズよりも内側だったら
        if x<self.size & y< self.size:
            # どちらのプレーヤーなのか
            if player==1:
                self.board_list[x][y]="maru"
                self.board_dict[x*self.size+y]="maru"
            elif player==2:
                self.board_list[x][y]="batu"
                self.board_dict[x*self.size+y]="batu"
        else:
            # サイズよりも外を選択していたら
            print("再入力してください")
            pass
        

        # もしも、サイズと同じ数だけ並んでいたら勝ち
        #リスト側で判断させる。サイズの数だけ縦横斜めのチェックをさせる、
        
        for i in range(self.size-1):
            if self.board_list[x][y]==self.board_list[x][y+i]:
                print("上列win")
                self.state=2
                self.next=None
                print(f"{player}"+"が勝ち")
            elif self.board_list[x][y]==self.board_list[x][y-i]:
                print("下列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x+i][y]:
                print("みぎ列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x-i][y]:
                print("ひだり列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x+i][y+i]:
                print("右斜上列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x-i][y-i]:
                print("左斜め下斜列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x+i][y-i]:
                print("右斜め下斜列はOK")
                self.state=2
                self.next=None
            elif self.board_list[x][y]==self.board_list[x-i][y^i]:
                print("右斜め下斜列はOK")
                self.state=2
                self.next=None
            else:print("勝敗はまだ決まっていません")



        # もしも勝敗が決まったらnext=nonを代入
        # 同じくゲームの状況を１、もしくは２にする１は引き分け、２は勝敗があったということ
        

    def print_board(self):

        print("||")
        pass



print("gameサイズを選択してください")
n=input()
print(n)
game=TicTacToe(n)
print("プレイする人を教えてください")
player=input()
print("場所を選択してください、x,yの順でおしえて")
x=input()
y=input()
game.play(player,x,y)
