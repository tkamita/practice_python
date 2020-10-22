# 関数
#   一連の処理を１つにまとめたもの

# def 関数名():
#   処理



def print_hello():
  print('hello world')

print_hello()


def num_max(a, b):
  print('a = {}, b = {}'.format(a, b))
  if a > b:
    return  a
  else:
    return  b

print(num_max(10, 20))
print(num_max(b=100, a=20))




# 関数のデフォルト値の指定
# def function(arg1, art2=100):

# 可変長引数
#   可変長のタプル型: *arg1
#   可変長の辞書型:   **arg1

# 複数の返り値
# return a, b



def sample(arg1, arg2=100):
  print(arg1, arg2)

sample(200, 300)    #デフォルト値は300に上書きされる
sample(200)       #デフォルト値100が実行される



def spam(arg1, *arg2):
  print("arg1 = {}, arg2 = {}".format(arg1, arg2))
  print(type(arg2))

spam(1, 2, 3, 4, 5)     # 2, 3, 4, 5 はarg2にタプル型で格納される



def spam_2(arg1, **arg2):
  print('arg1 = {}, art2 = {}'.format(arg1, arg2))
  print(type(arg2))

spam_2(3, name='taro', age='30')



# エラー 
# def spam_2(arg1, **arg2, **arg3):
#   print('arg1 = {}, art2 = {}'.format(arg1, arg2))
#   print(type(arg2))

# spam_2(3, name='taro', age='30')


#   *と**は同時に使える
def spam_3(arg1, *arg2, **arg3):
  print(arg1, arg2, arg3) 

spam_3(1, 2, 3, 4, 5, name='taro', age=15)



def sample_2():
  return 1, 2

a, b = sample_2()
print(a, b)


