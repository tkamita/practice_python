# range関数
#   range(5)
#   range(2,6)


for i in range(10):
  print(i)

for _ in range(100):  #_は単に100回やるだけ
  print('A')


for i in range(2, 20, 3) #１引数＝初め  ２引数＝終わり　３引数＝飛ばす（間隔）
  print(i)


sample = ['john', 'paul', 'george', 'ringo']    #リスト[]の場合
sample = ('john', 'paul', 'george', 'ringo')    #タプル()の場合
for member in sample:
  print(member)



human = {
  'Name': 'taro',
  'age': 20,
  'gender': 'man'
}
for h in human:
  print(h)    #keyのみ取り出す
  #print(h, human.get(h))   #keyと値を取り出す






# enumeratek関数
  # 配列の中の値とインデックスを同時に取得する

# zip関数
#   ２つの配列の中の値を同時にループする

# while
#   whileの中の式がtrueであるうちは処理を実行する


fruits = ['grape', 'pine', 'apple']
for index, value in enumerate(fruits):
  print('index = {}'.format(index))
  print('value = {}'.format(value))


classA = ['taro', 'hanako', 'jiro']
classB = ['katsuo', 'wakame', 'taro']
for A, B in zip(classA, classB)
  print('classA student: {}'.format(A))
  print('classB student: {}'.format(B))


count = 0
while count < 10:
  print(count)
  count += 1



# continue
#   ループ内にcontinueがあると処理が一度飛ばされる
# break
#   ループの外に処理が出る
# else
#   ループの外に出たときに実行される
#   breakで抜けた場合は実行されない


for i in range(10):
  if i == 3:
    continue
  print(i)
  
for i in range(10):
  if i == 3:
    break
  print(i)
else:
  print('終了')


num = 0
while num < 10:
  if num == 5:
    num += 1
    continue
  if num == 7:
    break
  print(num)
  num += 1

while num < 10:
  if num == 5:
    num += 1
    continue
  print(num)
  num += 1
else:
  print('whileループ終了')
  


