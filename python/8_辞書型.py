# dictinary = {'kye1': '値', 'key2': '値'}
car = {"brand": "Toyota", "model": "Prius", "year": 2015}
print(car['brand'])
print(car.get['brand'])
if key in car:
  print(car['key'])


car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}
print(car['brand'])
print(car['bran']) #error
print(car.get('bran', 12)) #nullの場合、第二引数が表示される

print(car.keys()) #keyの一覧
print(car.values()) #値の一覧
print(car.items()) #keyと値の一覧

for k, v in car.items():
  print('key = {}, value = {}'.format(k, v))

if 'brand' in car:
  print('carのブランドは{}'.format(car['brand']))


# メソッド
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}
tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

car.update(tmp_car) #値の追加と更新
print(car)

car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car)

value = car.popitem() #最後に追加した要素の取り出し
print(car)
print(value)

value = car.pop('model') #キーを追加して値を取り出し
print(car)
print(value)

car.clear() #辞書の中身のクリア
print(car)

del car #辞書の中身を削除
print(car)
