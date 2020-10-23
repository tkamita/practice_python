# ループと条件を使って、一行でリストを作成
# 変数名 = [式 for 変数 in リスト (if 条件式)]


list_a = (1, 2, 3, 'a', 4, 'b')   #タプル
list_b = [x for x in list_a]
print(list_b)

list_b = [x*2 for x in list_a]
print(list_b)

list_b = [x*2 for x in list_a if type(x) == int]
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)




dict_a = {
  'a': 'apple',
  'b': 'banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c)


list_d = (x for x in range(100))
print(type(list_d))
list_d = {x for x in range(100)}
print(type(list_d))
list_d = tuple(x for x in range(100))
print(type(list_d))

def func(n):
  for x in range(2, n):
    if n % x == 0:
      return True
  return False

list_d = [x for x in range(100) if func(x) == False]
print(list_d)

list_d = [func(x) for x in range(100) if func(x) == False]  #関数をいれることもできる
print(list_d)
