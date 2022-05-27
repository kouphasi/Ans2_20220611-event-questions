from ast import While


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    next_array = sorted_array

    counter = 0#

    while True:
        if len(next_array) >= 1:
            center_index = len(next_array)//2 #真ん中のindexを取得
            if next_array[center_index] == target_number:#一致した場合
                return center_index + counter#出力
            elif next_array[center_index] > target_number:#小さかった時の場合
                next_array = [next_array[i] for i in range(center_index)]
            else:
                counter += center_index#大きかった時にその数を記録する
                next_array = [next_array[i] for i in range(int(center_index),len(next_array)) ]
        else:
            break


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()