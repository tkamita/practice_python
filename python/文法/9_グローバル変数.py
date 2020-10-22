# 変数には利用できる領域（名前空間）がある

# globalを使わない場合
# 関数の中が名前空間

# global
# 関数の外までスコープが広がる



def printAnimal():
  animal = 'cat'
  print('関数内animal = {}, id = {}'.format(animal, id(animal)))

animal = 'dog'
printAnimal()   #関数内のcatが実行
print('関数外animal = {}, id = {}'.format(animal, id(animal)))     #関数外のdog



def printcat():
  global animal   #関数の外のanimalという変数が使えるようになる
  animal = 'cat'
  print('関数内animal = {}, id = {}'.format(animal, id(animal)))

animal = 'dog'
printcat()
print('関数外animal = {}, id = {}'.format(animal, id(animal)))     #関数外のcat

