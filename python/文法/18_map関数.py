# 検索
#   リスト、辞書などのループ可能なクラスの変数を第二引数で受け取る
#   第一引数の関数に代入した値を出力する



list_a = [1, 2, 3, 4, 5]
map_a = map(lambda x: x * 2, list_a)

for x in map_a:
  print(x)


man = {
  'name': 'ichiro',
  'age': '18',
  'country': 'japan'
}
map_man = map(lambda x: x + ',' + man.get(x), man)
for x in map_man:
  print(x)

  def calcurate(x, y, z):
    if x == 'plus':
      return x + y
    elif  z == 'minus':
      return x - y
map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus'])
for x in map_sample:
  print(x)
