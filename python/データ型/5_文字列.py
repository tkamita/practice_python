# 文字列を変数として扱う
#   ""
#   """~~"""  改行も挿入できる

# 文字型メソッド
#   連結
#     +
#     *
#   bytes型への変換
#     encode
#     decode
#   回数検索
#     count
#   文字列の始まりと終わりをチェック
#     startswith
#     endswith
#   文字列の除去
#     strip
#     rstrip
#     lstrip
#   文字列の変換
#     upper 大文字変換
#     lower 小文字変換
#     swapcase  大文字小文字入れ替え
#     replace 文字変換
#     capitalize  最初だけ大文字に変換
#   文字列の検索
#     find
#     index
#     rfind
#     rindex
#   文字列の条件
#     islower
#     isupper


fruit = 'apple'
print(fruit)
pritn(type(apple))

print(fruit * 10)
print(fruit + 10) #error

fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[2])
print(fruit[-1]) #後ろから数える


#encode,decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count
msg = 'ABCDEABC'
print(msg.count('ABC'))
print(msg.count('ABCDEF'))

# startswith, endswith
print(msg.startswith('ABCD')) #true
print(msg.endswith('C')) #true

#strip(両端を削除), rstrip(右端), lstrip(左端)
msg = ' ABC'
print(msg)
print(msg.strip()) #デフォルトでスペースを削除
msg = 'ABCDEFABC'
print(msg.strip('C'))
print(msg.rstrip('C'))
print(msg.lstrip('C'))

# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s = msg.swapcase()  #大文字小文字入れ替え
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF') #ABCがFFFになる
msg_r = msg.replace('ABC', 'FFF', 1)　#左から最初のABCがFFFになる
msg_r = msg.replace('ABC', 'FFF', -1)　#全て
print(msg_r)

msg = 'hello world'
print(msg.capitalize())
msg = 'hello woRld'
print(msg.capitalize())

#文字列の一部取り出し、format,isloewr,isupper
msg = 'hello, my name is taro'
print(msg[:6])
print(msg[6:])
print(msg[1:6])
print(msg[1:10:3])
print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}') #3.6~
print(f'{name=}') #3.8~ デバックするときなど

msg = 'apple'
print(msg.islower())
print(msg.isupper())

#find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))
# errorの挙動
# find
#   -1が返ってくる
# index
#   errorが返ってくる
