# 3.8以降
# while文と使う
# n += 1  で書かなくていい



if (n := 10) > 5:
  print('5より大きい: {}'.format(n))

n = 0
while (n := n + 1) < 10:
  print(n)
  