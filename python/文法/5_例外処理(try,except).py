# 例外処理
#   実行時に発生するエラー（実行エラー）を制御して処理を行う


# try:
#   処理
# except  エラー名:
#   例外発生時の処理


# FileNotFoundError
#   指定されたファイルが見つからないエラー
# IndexError
#   配列などで指定したインデックスに値が存在しない
# TypeError
#   型に関するエラー
# ZeroDivisionError
#   0で割ろうとしたことによるエラー
# Exception
#   全ての例外



a = 10 / 0
print('処理が完了しました')   #error


try:
  a = 10 / 0
except ZeroDivisionError as e:
  print(e, type(e))   #error内容
  pass    #何も処理を実行しない
print('処理が完了しました')

try:
  a = 10 / 0
except ZeroDivisionError as e:
  import traceback    #errorの詳細を表示
  traceback.print_exc()
  pass    #何も処理を実行しない
print('処理が完了しました')


try:
  b = [10, 20, 30]
  a = b[4]
  a = 10 / 0
except ZeroDivisionError as e:
  pass
except IndexError as e:
  print('indexerror')
print('処理が完了')


try:
  a = 10 / 0
except Exception as e:    #error全部
  print('exception', e, type(e))    #どんなerrorが起きているのか
print('処理が完了')



# else
  # 例外(error)が発生しなかった場合に実行される
  # tryとelseに分けて使う
    # try
    #   エラー想定
    # else
    #   エラーじゃない場合
# finally
  #例外が発生しても、しなくても実行される

try:
  a = 10 / 1
except Exception as e:    #error全部
  print('exception', e, type(e))    #どんなerrorが起きているのか
else:
  print('else処理')
print('処理が完了')

try:
  a = 10 / 1
except Exception as e:    #error全部
  print('exception', e, type(e))    #どんなerrorが起きているのか
else:
  a = 10 / 0    #elseの中でエラーが起きると処理が止まる
  print('else処理')
finally:      #ここで一旦、変数を初期化したり、logに出力したいときに使う
  print('finally処理')
print('処理が完了')



# raise
#   メッセージと例外を返すことができる


# 例外自作  exceptionを継承
# class MyException(Exception):


def devide(a, b):
  if b == 0:
    raise ZeroDivisionError('0ではわりきれません')
  else:
    return a / b

try:
  c = devide(10, 0)
except Exception as e:
  print(e, type(e))


class MyException(Exception):   #myexceptionの部分は自分がつけたいエラー名
  pass    #error名をつけたいだけなので特に処理は書かなくて大丈夫
def devide(a, b):
  if b == 0:
    raise MyException('0ではわりきれません')
  else:
    return a / b

try:
  c = devide(10, 0)
except Exception as e:
  print(e, type(e))



