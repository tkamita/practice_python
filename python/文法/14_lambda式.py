# ifを一行で表して代入する
#   x = 0 if y > 10 else 1
# lambda 引数: 返り値


y = 10
x = 0 if y > 0 else 1   
print(x)

x = 0 if (y-20) > 0 else 1   
print(x)

x = 0 if (y-20)*2 > 0 else 1   
print(x)


lambda_a = lambda x: x * x  #引数x 返り値x*x
print(lambda_a(10))

lambda_b = lambda x, y, z=5: x * y * z
print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))    #デフォルト値設定しても上書きできる



# 条件式
lambda_c = lambda x, y: y if x < y else x
print(lambda_c(2, 4))


