# リストを昇順、降順に並び替える

list_a = [4, 1, 5, 2, 6, 6, 8, 3]

# i:   0 => list_aの長さ-1
for i in range(len(list_a)):
  # j:  0 => list_aの長さ-1 -i -1
  #一回のソートで配列の何番目までいくか
  # 一回目は右端、ソートする範囲を狭める
  for j in range(0, len(list_a) - i - 1):
    if list_a[j] > list_a[j+1]:   #昇順
      list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

print(list_a)


# i:   0 => list_aの長さ-1
for i in range(len(list_a)):
  # j:  0 => list_aの長さ-1 -i -1
  #一回のソートで配列の何番目までいくか
  # 一回目は右端、ソートする範囲を狭める
  for j in range(0, len(list_a) - i - 1):
    if list_a[j] < list_a[j+1]:   #降順
      list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

print(list_a)