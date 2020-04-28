# 整数，输出整数 3
print(3)
# => 3

#计算加减乘除,对于除法，python会自动将整数转换成浮点数
add = 1 + 2
sub = 5 - 2
mul = 5 * 5
print(add)
# => 3
print(sub)
# => 3
print(mul)
# => 25

div = 9 / 3
div2 = 5 / 3
print(div)
# => 3.0
print(div2)
# => 1.6666666666666667

#用 // 来除，那么得出的结果会向下取整
div3 = 10 // 3
print(div3)
# => 3
div4 = 10.0 // 3.0
print(div4)
# => 3.0

#浮点数的运算结果依然是浮点数
mul2 = 3.0 * 3.0
print(mul2)
# => 9.0

#取余数，python里面称之为模除
y = 10 % 3
print(y)
# => 1

# x的y次方
su = 2 ** 3
print(su)
# => 8

#如果有括号的，先算括号内的
res = (1+3) * 2
print(res)
# => 8

#布尔值，True 、False
print("2" == "2")
# => True
print("2" == "3")
# => False

print(not True)
# => False
print(not False)
# => True

#逻辑运算符
print(True and False)
# => False
print(False or True)
# => True

#整数也可以当作布尔值
print(0 == 2)
# => False
print(1 == 2)
# => True
print(1 != 2)
# => True
print(2 != 2)
# => False
print(0 and 2)
# => 0
print(0 or 2)
# => 2
print(0 == False)
# => True
print(1 == True)
# => True
print(2 == True)
# => False

#比较大小
print(3 < 4)
# => True
print(3 > 2)
# => True
print(-3 > -2)
# => False
print(2 <= 2)
# => True
print(1 > 2 < 3)
# => False
print(1 < 2 < 3)
# => True

#字符串用但双引号都可以表示
print("auto")
# => auto
print('auto')
# => auto

#用加号连接字符串
print('hello'+" "+"world")
# => hello world

#字符串可以当作字符列表
str = "hello world"
print(str[0])
# => h

#用.format来格式化字符串
print("{} can be {}".format("you","do"))
# => you can be do

#重复使用参数
print("{0} be engineer, {0} be manager, {0} jump over the {1}".format("Jack", "candle stick"))
# => Jack be engineer, Jack be manager, Jack jump over the candle stick

#使用关键字作为参数
str = "{name} wants to eat {food}".format(name="Bob", food="lasagna")
print(str)
# => Bob wants to eat lasagna

# None是一个对象
print(None)
# => None

#当与None进行比较时不要用 ==，要用is。is是用来比较两个变量是否指向同一个对象。
print('yes' is None)
# => False
print(None is None)
# => True

# None，0，空字符串，空列表，空字典都算是False
# 所有其他值都是True
print(bool(None))
# => False
print(bool(0))
# => False
print(bool(""))
# => False
print(bool([]))
# => False
print(bool({}))
# => False




