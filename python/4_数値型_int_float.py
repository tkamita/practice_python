# 数値型は、int(整数型) float(浮動小数点数型)の２つ
# 数値計算
  # ＋：加算
  # ー：引き算
  # ＊：掛け算
  # /：割り算
  # //：割り算（小数点以下切り下げ）
  # ％：剰余
  # ＊＊：べき乗
value = 1
print(value)
value = -2
print(value)
value = value + 4
print(value)
print(value * 4)
print(value / 3)
value = 10
print(value // 3)
print(value % 3)
value += 3
value -= 2
print(value)
print(value ** 3)

# 浮動小数点数
height = 175.5
print(height)
print(type(height))
print(height + 10)


  # ＞＞
  # ＜＜：シフト演算
value = 8 #２進数では1000 >> 0010
print(value >> 2)
print(value << 3) #1000 <<< 1000000

  # ｜：ビット演算
  # https://qiita.com/7shi/items/41d262ca11ea16d85abc
  # https://qiita.com/Ingward/items/43acda931c8a62c70d2f
print(12 & 21)  #01100 and 10101 = 00100 => 4
print(12 | 21)  #01100 or 10101 = 11101 =>29
value = 12
value &= 21 #value = value & 21
print(value)
