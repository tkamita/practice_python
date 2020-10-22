# inner関数
  # 使い道
  #   外の関数の外からアクセスできない
  #   関数の中で同じ処理がある
  #   デコレータ関数を作成
# ノンローカル変数


def outer():
  def inner():
    print('A')
  inner()

# inner()   #関数の外からinner関数は呼べないのでerror
outer()   #outer関数からinner関数を呼び出す



def outer():
  outer_value = '外側の変数'    
  def inner():
    outer_value = '内側の変数'    #inner関数内でのみ有効な変数
    print('inner:  outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
  inner()
  print('outer:  outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()

def outer():
  outer_value = '外側の変数'    
  def inner():
    nonlocal outer_value      #outer側の変数も書き換わる
    outer_value = '内側の変数'    
    print('inner:  outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
  inner()
  print('outer:  outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()


