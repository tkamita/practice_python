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






# 数値について、２進数、８進数、１６進数
  # ２進数
  #   0b
  # ８進数
  #   0o
  # １６進数
  #   0x
age = 0b111 # 7
print(age)
age = 0o11 # 9
print(age)
age = 0x11 # 17
print(age)
# n進数の数値を文字列にする
#   bin(2進数)
#   oct(8進数)
#   hex(16進数)
print(bin(15)) #0b1111
print(oct(15)) #0o17
print(hex(15)) #0xf


# 複素数
  # 実数と虚数を含んだ数値
  # https://qiita.com/butchi_y/items/a4a7e992870d75e5ee7a
  # 複素数を表す方法にcomplex関数がある
  # 虚数: x + yj
  # real(実数部)
  # imag(虚数部)
a = 1 + 3j
b = 3 + 5j
print(a, b)
print(a + b)
print(a - b)
print(a * b)

a = complex(1, 3)
b = complex(3, 5)
print(a, b)
print(a + b)
print(a - b)
print(a * b)

print(a.real)
print(a.imag)


