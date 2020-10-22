# ジェネレータ
#   他のジェネレータを呼び出す
#   yield from
# サブジェネレータ
#   他のジェネレータから呼び出される
#   return



def sub_sub_generator():
  yield "sub subのyield"
  return "sub sub のreturn"

def sub_generator():
  yield "subのyield"
  res = yield from sub_sub_generator()    #sub_subのreturnが変数resに代入される
  print('sub res = {}'.format(res))
  return "subのreturn"

def generator():
  yield "generatorのyield"
  res = yield from sub_generator()
  print('gen res = {}'.format(res))
  return 'generatorのreturn'

gen = generator
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))




# ジェネレータの使い道
  # メモリ使用量を削減
  # DBから大量のレコードを一気に取得するとき
import sys
list_a = [i for i in range(1000000)]
def num(max):
  i = 0 
  while i < max:
    yield i 
    i += 1

# for i in num(10000000):
#   print(i)

gen = num(1000000)
print(sys.getsizeof(list_a))    #メモリ使用量多い
print(sys.getsizeof(gen))       #メモリ使用量少ない
