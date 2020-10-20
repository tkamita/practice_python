# リスト変数を使うと１つの箱の中に複数の値を入れることができる


list_a = [1,2,3,4]
list_b = []
print(list_a)
print(list_a[0])
print(list_a[-1])

list_a = [1, [1,2,'apple'], 3, 'banana']
print(list_a[1][2]) #appleが表示される

list_a[1][2] = 'lemon'
print(list_a) #appleがlomonに書き換わる


#リストの一部取り出し
list_a = [1,2,3,4,5]
list_b = list_a[:3] #index番号の0~2を表示する
print(list_b)
list_b = list_a[1:4]
print(list_b)
list_b = list_a[1:4:2]
print(list_b)


# リストのメソッド
  # append
  #   値を１つ追加
list_a.append('apple')
print(list_a)
list_a.append(['banana', 'melon'])
print(list_a)
  # extend
  #   リストにリストを追加して拡張
list_a.extend(['banana', 'melon'])
print(list_a)
  # insert
  #   リストに位置を指定して値を追加
list_a.insert(1, 'grape') #index1にgrapeを追加
print(list_a)
  # clear
  #   リストを初期化
list_a.clear()
print(list_a)
  # remove
  #   指定した要素をリストから削除
list_a = [0,1,2,3,4,5,5,6,6,7]
list_a.remove(3)
print(list_a)
  # pop
  #   指定したインデックスの要素を取り出して削除
value = list_a.pop()
print(list_a, value)
  # count
  #   指定した値がリストに含まれる数を返す
print(list_a.count(3))
  # index
  #   指定した値のインデックスを返す
print(list_a.index(1))
  # copy
  #   リストをそのままコピーして新たなリストを作成し、返す
print(list_a)
list_b = list_a.copy()
list_b[0] = 'AAAA'
print(list_a)






  # 並び替え
    # sort(sorted)
    #   リストを並び替える（型が同じ出ないとエラー）
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
list_a.sort() #昇順に並び替える
print(list_a)
list_a = sorted(list_a)
print(list_a)
    # reverse
    #   リストの順番を入れ替える
list_a.reverse()
print(list_a)

    
