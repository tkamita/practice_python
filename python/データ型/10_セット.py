# リスト、タプルと似たように複数の値を入れる

# 同じ値を持つことがない（ユニーク）
#   set_a = {'1', 'b', 'c', 'c'} 最後のcは入らない
# 順序が保持されていない
# ユニオンやインターセクションなどの集合処理を高速で行う
# 配列は入れられない

set_a = {'a', 'b', 'c', 'd', 'a', 12}
print(set_a)
set_a = {'a', 'b', 'c', 'd', 'a', 12, ['a', 'b']}
print(set_a) #error

print('e' in set_a)
print('a' in set_a) #set_aに'a'があるか
print('a' not in set_a) 

print(len(set_a)) #要素の長さ

#add , remove, discard, pop, clear
set_a.add('A') #要素の追加
print(set_a)

set_a.remove('a') #要素の削除
print(set_a)

set_a.discard(12) #要素の削除
print(set_a)

val = set_a.pop() #要素の取り出し
print(val, set_a)

set_a.clear() #セットのクリア
print(set_a)


# セットのメソッド
# union, intersection, difference, symmetric_difference
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}
# union
#   和集合  |
u = s | t   #sかtどちらかに含まれてたら表示される
u = s.union(t)    #こういう書き方もある
print(u)
# intersection
#   積集合  &
u = s & t   #sとt両方に含まれているものが表示される
# u = s.intersection(t)
print(u)
# difference
#   差集合  -
u = s - t    #sに含まれててtに含まれていない要素
u = s.difference(t)
print(u)
# symmetric_difference
#   対象差  ^
u = s ^ t     #どちらか一方に含まれているが、片方には含まれていない要素
u = s.symmetric_difference(t)
print(u)


s |= t    #sの要素にtを追加できる
print(s)



# issubset
#   別の集合に含まれているか
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}
print(s.issubset(t))
# issuperset
#   別の集合を含んでいるか
print(t.issuperset(s))    #true
print(s.issuperset(t))   #false
# isdisjoint
#   重複要素はないか
print(t.isdisjoint(s))    #false  一つでも重複している要素があれば
print(t.isdisjoint(u))    #true

