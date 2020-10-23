# 関数を変数で扱うことができる
# 関数を他の関数の引数にする
# 関数を他の関数の返り値にする


def print_hello():
  print('hello')

def print_goodbye():
  print('goodbye')

var = ['AA', 'BB', print_hello, print_goodbye]
var[2]()
var[3]()







def print_world(msg):
  print('{} wrold'.format(msg))

def print_ohayo():
  print('おはよう')

def print_hey(func):
  func('hello')
  return print_ohayo

var = print_hey(print_world)
var()





