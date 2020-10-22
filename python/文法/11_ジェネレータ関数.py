# yieldを使う
  # yieldの部分で処理がストップ
  # yieldの引数が呼び出し元に返される
  # 再度,yieldの部分から処理がスタート
  # yieldの部分で処理がストップ



def generator(max):
  print('ジェネレータ作成')
  for n in range(max):
    yield n
    print('yield実行')

# gen = generator(10)
# n = next(gen)
# print('n = {}'.format(n))
# n = next(gen)
# print('n = {}'.format(n))

#毎回nextで呼び出すのが手間
gen = generator(10)
for x in gen:
  print('x = {}'.format(x))




# send()
#   yieldで停止している箇所に値を送る
# throw()
#   例外を発生させて処理が終了
# close()
#   ジェネレータを正常終了
def generator(max):
  print('ジェネレータ作成')
  for n in range(max):
    x = yield n
    print('x = {}'.format(x))
    print('yield実行')

gen = generator(10)
next(gen)
gen.send(100)
gen.close()   #ここでジェネレータ終了
# next(gen)     #実行されない


def generator(max):
  print('ジェネレータ作成')
  for n in range(max):
    try:
      x = yield n
      print('x = {}'.format(x))
      print('yield実行')
    except ValueError as e:
      print('throwを実行しました')

gen = generator(10)
next(gen)
gen.throw(ValueError('invalid value'))


