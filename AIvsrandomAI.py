#!/usr/bin/env python3

from python_mid_tictactoe_revised import TicTacToe
from python_mid_agentclass import AIagent
from python_mid_qagent import Qagent

class Statistician():
    """
    qagentとAIagentを戦わせる
    args:   m(int):ボードサイズ(デフォルト3)
    match_count(int):対戦回数
    attributes: 
                None
    methods:
                doit:指定回数の対戦を実施して結果を出力させる
    """

    def __init__(self, n: int = 3, match_count: int = 2):
         
        self.size = n
        self.match_count = match_count
        self.winner_idx=0

    def doit(self):

        """
        戦わせるメソッド
        args:
            None
        Returns:
            result(list):引き分けの回数,aの勝利数,bの勝利数
        """
        a = AIagent()
        b = Qagent(self.size)
        players = [a, b]

        swapped = False							# for rule #2
        result  = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]		# [rule][draw, p1win. p2win]
        
        print('RESULT の順番は [引分, #R勝, #A勝]')
        for rule in range(3):
            print(rule)
            print(f'RULE #{rule+1}: {["先手後手固定(R先手)", "先手後手固定(Q先手)","勝者が後手"][rule]}')
            # もしルールが１(2つ目のやつ)だったらswappedをtrueにする。
            if rule==1:
                players.reverse()
                # swappedフラッグを使って順番交代していることを明記

                swapped=True
            for i in range(1, self.match_count+1):
                game = TicTacToe(self.size)
                
                # gameをしている間
                while game.state==0:
                    next_action = players[game.next - 1].select(game.board)
                    game.play(game.next, next_action)
                    
                    if game.state == 1:
                        # 引き分けになったらresultの引き分けに+1する
                        result[rule][0] += 1
                    
                    elif game.state == 2:
                        # swappedがtrueだったら3から引くことで入れ替えれる
                        if swapped:
                            winner_idx = 3 - game.winner
                        else: winner_idx=game.winner
            
                        result[rule][winner_idx] += 1
                        # もし勝ったのがQだったらrewardを増やす次の環境っていうのは相手が行動した後らしい。更新するのは相手の選択後、相手が選択して相手が勝ったら-1、次のターンで勝てたら1
                    
                    # 現状はupdateタイミング、勝利タイミング？になっており、しかも勝利状況のみしかqtableの更新をしていない。
                    if game.next==2 and i>1:
                        b.update(game.board,winner_idx)

                        if rule==2 and game.winner==1:
                            players.reverse()
                            swapped = not swapped
                       

            # 進行状況を表す部分を追加（必要に応じて修正）
            game.print_board(stat=True)
           
        return result, [[n/self.match_count for n in result[0]], [n/self.match_count for n in result[1]],[n/self.match_count for n in result[2]]]



N = 3
M = 100
s = Statistician(n=N, match_count=M)
ret = s.doit()
print(ret)
