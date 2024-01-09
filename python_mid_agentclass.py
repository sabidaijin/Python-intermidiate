#!/usr/bin/env python3

from random import choice
from python_mid_tictactoe_revised import TicTacToe
from python_mid_abstractclass import agent

# エージェント側をクラスで作る。作ったクラスのインスタンスが前に作ったゲームで遊ぶようにする

    
class AIagent(agent):
# ランダムエージェントの実装
    def select(self,board):
        # 空いているマスのインデックスを取得する
        vacant=[]
        vacant=[index for index, value in enumerate(board) if value == 0]
        
        # 取得したインデックスからランダムに選ぶ
        selected = choice(vacant)

        return(selected)
    
        
class HUagent(agent):
# 人間用のエージェントの実装
    def select(self):
        print("マークを入れたいところインデックスで選択してください。x,y")
        selected=int(input())
        
        return(selected)


# if __name__ == '__main__':
#     print("gameサイズを選択してください")
#     n=int(input())
#     print(n)
#     game=TicTacToe(n)
#     AI=AIagent()
#     HU=HUagent()
#     # 人間vsCPU
#     while (game.state==0):
#         for i in range(1,3):
#             if i==1:
#                 game.play(i,AI.select(game.board))
#             if i==2:
#                     game.print_board()

#                     game.play(i,HU.select())
                    

#             if game.state == 1:
#                 print('Result: DRAW')
#                 break
#             elif game.state == 2:
#                 print('Result: Player %d (%s) WON' % (game.winner, game.get_mark(game.winner)))
#                 break


# # AIvsAI
# game=TicTacToe(randint(3,7))
# AI1=AIagent()
# AI2=AIagent()
# print("何回繰り返しますか?")
# count=int(input())
# k=1
# for k in range(count):
#     print(k)
#     print("回目です")
#     game=TicTacToe(randint(3,7))
#     while (game.state==0):
#             for i in range(1,3):
#                 if i==1:
#                     game.play(i,AI1.select(game.board))
#                     game.print_board()
#                 if i==2:
#                     game.play(i,AI2.select(game.board))
#                     game.print_board()
            
#             if game.state == 1:
#                     break
#             elif game.state == 2:
#                     print('Result: Player %d (%s) WON' % (game.winner(), game.get_mark(game.winner())))
#                     #勝ち負け帰るところを変えてない、arrayに突っ込んでreverseswapedフラッグ
#                     tenp=AI1
#                     AI1=AI2
#                     AI2=tenp
#                     print(k)
#                     print("回目です")
#                     break

