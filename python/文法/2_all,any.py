# if文でall,anyを使うと処理の記載が楽になる
# all
#   オブジェクト全てがtrueの場合に実行
# any
#   オブジェクトの一部がtureの場合に実行


if all((True, 10 < 20, 'a' == 'a')):    #andで繋がなくていい
  print('allの中の処理')

if not all((True, 10 < 20, 'a' == 'a')):    #andで繋がなくていい
  print('allの中の処理')


if any((False, False, True)):  #1つでも当てはまれば処理実行
  print('anyの中の処理')

if any((10 < 20, 10 < 5, 'a' == 'b')):
  print('anyの中の処理')

if not any((10 < 20, 10 < 5, 'a' == 'b')):
  print('anyの中の処理')



