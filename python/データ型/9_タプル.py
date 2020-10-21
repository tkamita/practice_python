# リストに似ているが値を変更、追加できない

# 配列よりもタプルの方がアクセスするスピードが速い
# ハッシュ化して辞書型のキーとして利用する
# 値を変更したくないとき
#   MONTH = ('Jan', 'Feb', ....)


fruit = ('apple', 'banana', 'lemon')
print(fruit)
print(type(fruit))
print(fruit[0])

fruit[1] = 'grape' #error
fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count('aplle'))
print(fruit.index('apple'))
print(fruit.index('appl')) #error

pos = (135, 35)
countries = {pos: 'Japan'}
print(countries.get(135, 35))

