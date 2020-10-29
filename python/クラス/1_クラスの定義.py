# class クラス名:
#   """ドキュメンテーション文字列"""
#   def メソッド名(self, ...):

# class Prius:
#   maker = "Toyota"
#   tire = "Studiess"
#   wiper = "Standard"    #クラスとプロパティ(maker,tire,wiper)を定義している
#   def my_func(self):    #クラスのメソッド

# myCar = Prius()   #インスタンス作成
# print(myCar.maker)    #プロパティの値が表示される



class Car:
  """車クラス"""
  country = 'Japan'
  year = 2019
  name = 'Prius'    #プロパティ
  def print_name(self):
    print('print_name実行')
    print(self.name)

my_car = Car()    #インスタンス化
print(my_car.year)
my_car.print_name()

list_a = ['apple', 'banana', Car]
second_car = list_a[2]()
second_car.print_name()
list_a = ['apple', 'banana', Car()]
list_a[2].print_name()

help(Car)   #クラスの内容をみる  qで閉じる



