# リストを昇順に並び替える


list_a = [5, 7 ,3 ,1, 3, 9, 2]

# Pythonで連番や等差数列を生成してfor文で使ったり、それらのリストを取得するには、range()を使う。
i = range(len(list_a))
print(i)    #0, 7

# i: 0 => list_aの長さまでループしたインデックス
for i in range(len(list_a)):
  min_idx = i   #min_idx: i以上のインデックスでlist_aに最小値の入っている物
  print(i)    #0 1 2 3 4 5 6
  for j in range(i+1, len(list_a)):
    if list_a[min_idx] > list_a[j]:     #昇順
      min_idx = j
  list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)



for i in range(len(list_a)):
  min_idx = i   #min_idx: i以上のインデックスでlist_aに最小値の入っている物
  for j in range(i+1, len(list_a)):
    if list_a[min_idx] < list_a[j]:   #降順
      min_idx = j
  list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)

