#!/usr/bin/env python3

import random
from python_mid_tictactoe_revised import TicTacToe
from python_mid_abstractclass import agent
class Qagent(agent):

    """

        qtableは縦列が状況、横列が選択肢、要素がそれが勝利に結びつく確率の表
        このプログラムではqtableを作る、qtableから状況に応じたアクションをランダムにさせる
        行動と行動の結果を記録し、それに基づいてqテーブルを更新するということを行う
        qテーブルの状況は三進数的に獲得
        行動は選択肢の数だけ用意する
        q値が一番高いものを選択するようにする

    """
    def __init__(self,size):
        
        self.size =size# ゲーム盤のサイズ
        self.qtable = {}  # Qテーブルを初期化
        self.statelist=[]
        self.qlist=[]
        self.qlists=[]    
        self.alpha = 0.1  # 学習率
        self.gamma = 0.9  # 割引率
        self.e = 0.1  # ε-greedy法のε
        self.selected=0 #選ばれたaction
        self.now_state=""
        self.qtable__init()
        


    def qtable__init(self):
        def generate_patterns_helper(prefix, remaining_digits):
                if remaining_digits == 0:
                    self.statelist.append(str(prefix))
                    
                    return 0
                for digit in range(3):
                    new_prefix = prefix + str(digit)
                    generate_patterns_helper(new_prefix, remaining_digits - 1)
                # これで現在のstateがわかる
                


        # そのためには、今この状態で次を選ぶべきかというqテーブルが必要。
        # qテーブルは、エージェントに学習させて都度書き込ませていく
        # まず全状態を数えてその分だけ二次元配列を作る
        # 3新数を利用して、インデックスを作る
        generate_patterns_helper("", self.size**2)
        
        k=0
        for k in range(len(self.statelist)):
            #リスト内包表記でpossibilitylist(qtableの要素)を作る。最初は全ての要素に0を入れる
            self.qlist = [0] * (self.size**2)
            self.qlists.append(self.qlist)
            k=k+1
        
        i=0
        # 状態：q値という形で辞書を作る
        for i in range(len(self.statelist)):
            self.qtable[self.statelist[i]] = self.qlists[i]
    

        # この時点でqtableには二次元配列の形でactionの数の要素が入ったq値が入っている
        # qtable[[0]
        #        [0]
        #         action0,action1,action2
        # state0 possibility[0],possibility[1],possibility[2]..
        # state1 possibility[size+1],possibility[size+2],possibility[size+3]....
        # state2
        # qtableは現在の状況、valueにこの盤面で選べる手段と、それを選んだ時に報酬が得られる確率を入れる

    def select(self,board):
        # 現在の状況を取得(毎回初期化)
        self.now_state=""
        for i in range(int(self.size**2)):
            n = board[i]
            self.now_state = str(self.now_state) + str(n)
            

        # listの中で一番q値が大きいものを選択する
        vacant=[]
        vacant=[index for index, value in enumerate(board) if value == 0]  

        if random.random() < self.e:
            # 取得した未選択インデックスからランダムに選ぶ(0~9とかが帰ってくる)
            self.selected = random.choice(vacant)
        else:
            # 最大のQ値を持つアクションのリストを取得
            max_q_indices = [i for i, q in enumerate(self.qtable[self.now_state]) if i in vacant and q == max(self.qtable[self.now_state])]
            
            if max_q_indices:
                self.selected = random.choice(max_q_indices)
            else:
                self.selected = random.choice(vacant)

        return self.selected
    
    def update(self,board,winner_idx) :

    #    """フィードバックを得るタイミングは問題ない。ただ、フィードバック対象が最終局面だけになっていて、
    #    フィードバックをヒストリーにするという実装ができていない。だから学習が悪いはず。
    #    ランダムが入っておいた状態のタイミングでフィードバックをする。勝ち負けが確定した時ではなく、ランダムが売った後にフィードバックを実行する
    #    qが買った時、もしくはrが売った後にフィードバックを実行する
    #    どうフィードバックするっていうのは遡って[盤面[アクション]にフィードバックする。どうにかして、終端に達した時に
        # それまでのヒストリーにもフィードバックできるように実装する"""
        

        # 選ばれたq値はqtableのnow_stateのインデックス番号から取得する。
        # selectedはそのまま、playのx値であり、かつqtableのある状態a内の行動インデックス番号でもある
        actionlist=[]
        actionlist= self.qtable[self.now_state]
        chosenq=actionlist[self.selected]
        # qtableの更新のために選択後の状況を取得（毎回初期化)
        next_state=""
        for i in range(self.size**2):
            n = board[i]
            next_state = next_state + str(n)
                
        # もしも次の一手を打った時に負けていたら、Q値は全部-1にしておく、そしたら選ばれなくなる
        # また、逆に次の一手を打つ時に勝っていたら、その前に打ったやつは全部1にしておく、そしたら選ばれやすくなる
        if winner_idx==1:
            reward= 1
            newvalue = [1] * (self.size**2)
            self.qtable[next_state]=newvalue
       
        elif winner_idx==2:
            reward= -1
            newvalue = [-1] * (self.size**2)
            
            self.qtable[next_state]=newvalue

        # 場合分け、勝ち負け決まらなかった時と決まった時で分ける
        
        
        # qtableの更新のために次の状態でのq値の最大値を取得する
        next_max_q= max(self.qtable[next_state])
               

        # qtableを更新する
        updated_q = (1 - self.alpha) * chosenq + self.alpha * (reward + self.gamma * next_max_q)
        # now_state配列のchosenqという値をupdate_qに置き換える
        self.qtable[self.now_state][self.selected] = updated_q

        # logging.basicConfig(filename="qtable.log",level=logging.INFO,format='%(asctime)s - %(levelname)s:%(message)s')
        # logging.info(self.qtable)
        # 更新した時だけに書き込む
        # フィードバッグで得た入力とqtableの変更したところだけ、計算式があってれば

        


