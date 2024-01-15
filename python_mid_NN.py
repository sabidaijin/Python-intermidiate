# 以下は、3層の一般的な MLP で、各層のノード数を 3, 5, 4として、ウェイトとバイアスを以下のように設定した場合の順伝播の計算例です。必要な方は、計算結果の確認の参考にしてください。

# 𝑾1=⎛⎝⎜⎜−1.011.11−1.211.03−1.131.23−1.051.15−1.251.07−1.171.27−1.091.19−1.29⎞⎠⎟⎟

# 𝑩1=(−1.31−1.331.35−1.371.39)

# 𝑾2=⎛⎝⎜⎜⎜⎜⎜−2.02−2.1−2.18−2.26−2.342.042.122.22.282.36−2.06−2.14−2.22−2.3−2.382.082.162.242.322.4⎞⎠⎟⎟⎟⎟⎟

# 𝑩2=(−2.422.44−2.462.48)


# 入力: (2, 1, 3)

# 出力
# 活性化関数無し:
# (4.9118, -4.9588, 5.0058, -5.0528)

# シグモイド関数:
# (0.00105447, 0.999008, 0.000934061, 0.999121)

# ReLU:
# (0, 17.1896, 0, 17.4976)

# 順伝播の計算を実装する（バックプロパテーションはスコープアウト)
# 
import math


def sigmoid(x):
    """シグモイド関数"""
    return 1.0/ (1 + math.exp(-x))

def relu(x):
    """ReLU関数"""
    return max(0, x)

def forward_propagation(input_data, flag):
    """順伝播の計算を行う"""
    W1 = [
        [-1.01, 1.03, -1.05, 1.07, -1.09],
        [1.11, -1.13, 1.15, -1.17, 1.19],
        [-1.21, 1.23, -1.25, 1.27, -1.29]
    ]

    B1 = [-1.31, -1.33, 1.35, -1.37, 1.39]

    W2 = [
        [2.02, 2.04, -2.06, 2.08],
        [-2.1, 2.12, -2.14, 2.16],
        [-2.18, 2.2, -2.22, 2.24],
        [-2.26, 2.28, -2.3, 2.32],
        [-2.34, 2.36, -2.38, 2.4]
    ]

    B2 = [-2.42, 2.44, -2.46, 2.48]


    if flag == 0:
        activation_function = sigmoid
    elif flag == 1:
        activation_function = relu
    else:
        activation_function = lambda x: x

    # 圧縮されて配列になる
    layer1_output = []
    # 第一層の出力を計算
    # iが横の列、jが縦の列
    
    for i in range(len(W1[0])):
        # layer1=x*W1+B1
        weighted_sum = 0
        for j in range(len(input_data)):
            #行列の掛け算は、転置を使う
            weighted_sum += input_data[j] * W1[j][i] 
        layer1_output.append(activation_function(weighted_sum+ B1[i]))


    layer2_output = []
    # 第二層の出力を計算
    for i in range(len(W2[0])):
        # layer2=layer1_output*W2+B2
        weighted_sum = 0
        
        for j in range(len(layer1_output)):
            #行列の掛け算は、転置を使う
            weighted_sum += layer1_output[j] * W2[j][i] 
        layer2_output.append(activation_function(weighted_sum+ B2[i]))

    return layer2_output



# 入力データ: (2, 1, 3)
input_data = [2, 1, 3]

# フラグ 0 シグモイド関数 1 ReLU関数 2 活性化関数無し
flag = 0
output = forward_propagation(input_data, flag)
print("出力:", output)
