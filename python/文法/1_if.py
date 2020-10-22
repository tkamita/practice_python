# if(制御文)
# False
#   none
#   false
#   0
#   ""

bool_var = True
print('boolの計算結果: {}'.format(bool(bool_var)))
if bool_var:
  print('if文の中の処理')

var = 12
print('varの計算結果: {}'.format(var(var)))
if var:
  print('if文の中の処理')

var = False
print('varの計算結果: {}'.format(var(var)))
if var:
  print('if文の中の処理')

var = 0
print('varの計算結果: {}'.format(var(var)))
if var:
  print('if文の中の処理')

var = ''
print('varの計算結果: {}'.format(var(var)))
if var:
  print('if文の中の処理')

var = []
print('varの計算結果: {}'.format(var(var)))
if var:
  print('if文の中の処理')




class ClassA:
    def __init__(self,a):
      self.a = a
    def __bool__(self):
      if self.a == 'a':
        return True
      return False




msg = 'blue'
if msg == 'blue':
  print('進め')
elif mag == 'red':
  print('止まれ')
else:
  print('それ以外の処理')


age = 10
if age < 20:
  print('20未満')
elif age <= 40:
  print('20以上、４０以下です')
elif age >= 60:
  print('60以上です')
else:
  print('それ以外の年齢')



gender = 'man'
age = 10
if gender == 'man' and age < 20:
  print('未成年男性です')
if gender == 'man' or age < 20:
  print('男性もしくは２０未満です')

if not gender == 'man':
  print('男ではない')
if gender != 'man':
  print('男ではない')



