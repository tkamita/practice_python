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


