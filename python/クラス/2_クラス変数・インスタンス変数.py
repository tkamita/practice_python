# クラスで定義する属性（プロパティ）には
#   クラス変数
#     オブジェクト同士で共有できる
#     メソッド内部ではなく、クラスの直下に定義
#   インスタンス変数
#     インスタンごとに別々に利用する
    # メソッド内部に定義


class SampleA():
  class_val = 'class val'   #クラス変数

  def set_val(self):
    self.instance_val = 'instance val'    #インスタンス変数

  def print_val(self):
    print('クラス変数 = {}'.format(self.class_val))
    print('インスタンス変数 = {}'.format(self.instance_val))


instace_a = SampleA()   #インスタンス化
instace_a.set_val()
print(instace_a.instance_val)
instace_a.print_val()

print(SampleA.class_val)    #クラス変数
print(instace_a.__class__.class_val)    #クラス変数

instance_b = SampleA()    #インスタンス化
instance_b.set_val()
instance_b.print_val()
instace_a.__class__.class_val = 'class val 2'
instance_b.print_val()

print(id(instace_a.__class__.class_val))
print(id(instance_b.__class__.class_val))