#print是内置的打印函数
print("I'm Python,Nice to meet you!")
# => I'm Python,Nice to meet you!

#给变量赋值前不用提前声明
#传统的变量命名是小写，用下划线分割单词
some_var = 5
print(some_var)
# => 5


#访问未赋值的变量会抛出异常
# print(num)
# =>print(num)
# NameError: name 'num' is not defined

#用列表（list）储存序列
li = []

#创建列表时可以同时赋给元素
other_li = [4,5,6]
print(other_li)
# => [1, 2, 3]

#用append在列表最后追加元素
li.append(1)
li.append(2)
li.append(3)
li.append(4)
print(li)
# => [1, 2, 3, 4]

# 用pop从列表尾部删除元素
li.pop()
print(li)
# => [1, 2, 3]

#把4放回去
li.append(4)
print(li)
# => [1, 2, 3, 4]

#列表存取跟数组一样
res = li[0]
print(res)
# => 1
#取出最后一个元素
res = li[-1]
print(res)
# => 4

#越界存取会造成indexError
# print(li[4])
#print(li[5])
#IndexError: list index out of range

#列表切割
#取第二和第三位
a = li[1:3]
print(a)
# =>[2, 3]
#取最后两位
b = li[2:]
print(b)
# =>[3, 4]
#取头三位
c = li[:3]
print(c)
# =>[1, 2, 3]
#隔一个取一个
d = li[::2]
print(d)
# => [1, 3]
#倒排列表
e = li[::-1]
print(e)
# => [4, 3, 2, 1]
#可以用三个参数的任何组合来构建切割
#li[始:终:步伐]

#用del删除任何一个元素
print(li)
# =>[1, 2, 3, 4]
del li[2]
print(li)
# => [1, 2, 4]

#列表可以相加
#注意：li和other_li的值不变
print(li+other_li)
# => [1, 2, 4, 1, 2, 3]

#用extend拼接列表
li.extend(other_li)
print(li)
# => [1, 2, 4, 4, 5, 6]

#用 in 测试列表是否包含值
print(1 in li)
# => True

#用len取列表长度
print(len(li))
# => 6

#元素是不可改变的序列
tup = (1,2,3)
print(tup[0])
# => 1

# tup[0] = 3
#    tup[0] = 3
#TypeError: 'tuple' object does not support item assignment

#列表允许的操作元组基本都可以
print(len(tup))
# => 3
print(tup+(4,5,6))
# => (1, 2, 3, 4, 5, 6)
print(tup[:2])
# => (1, 2)
print(2 in tup)
# => True

#可以把元组合列表解包，赋值给变量
a,b,c = (1,2,3)
print(a,b,c)
# => 1 2 3
#元组周围的括号是可以省略的
d,e,f = 4,5,6
# => 4,5,6
#交换两个变量的值
e,d = d,e
print(d,e)
# =>5 4

#用字典表达映射关系
empty_dict = {}
#初始化字典
filled_dict = {"one":1,"two":2,"three":3}
print(filled_dict)
# => {'one': 1, 'two': 2, 'three': 3}

#用[] 取值
print(filled_dict["one"])
# =>1

#用keys获取所有的键
# 因为 keys 返回一个可迭代对象，所以在这里把结果包在 list 里。我们下面会详细介绍可迭代。
# 注意：字典键的顺序是不定的，你得到的结果可能和以下不同。
print(list(filled_dict.keys()))
# => ['one', 'two', 'three']

#用values获得所有的值。跟keys一样，要用list包起来，顺序也可能不同。
print(list(filled_dict.values()))
# => [1, 2, 3]

# 用in测试一个字典是否包含一个键
print("one" in filled_dict)
# => True
print(1 in filled_dict )
# => False

# 访问不存在的键会导致KeyError
# print(filled_dict["four"])
# => KeyError

# 用get来避免KeyError
print(filled_dict.get("one"))
# => 1
print(filled_dict.get("four"))
# => None
# 当键不存在的时候get方法可以返回默认值
print(filled_dict.get("one", 4))
# => 1
print(filled_dict.get("four", 4))
# => 4

# setdefault方法只有当键不存在的时候插入新值
print(filled_dict.setdefault("five", 5))
# filled_dict["five"]设为5
print(filled_dict.setdefault("five", 6))
# filled_dict["five"]还是5

# 字典赋值
filled_dict.update({"four":4})
print(filled_dict)
# => {"one": 1, "two": 2, "three": 3, "four": 4}
# 另一种赋值方法
filled_dict["four"] = 4
print(filled_dict)
# => {'one': 1, 'two': 2, 'three': 3, 'five': 5, 'four': 4}

# 用del删除
del filled_dict["one"]  # 从filled_dict中把one删除

# 用set表达集合
empty_set = set()
# 初始化一个集合，语法跟字典相似。
some_set = {1, 1, 2, 2, 3, 4}
print(some_set)
# => {1, 2, 3, 4}

# 可以把集合赋值于变量
filled_set = some_set

# 为集合添加元素
filled_set.add(5)
print(filled_set)
# => {1, 2, 3, 4, 5}

# & 取交集
other_set = {3, 4, 5, 6}
print(filled_set & other_set)
# => {3, 4, 5}

# | 取并集
print(filled_set | other_set)
# => {1, 2, 3, 4, 5, 6}

# - 取补集
print({1, 2, 3, 4} - {2, 3, 5})
# => {1, 4}

# in 测试集合是否包含元素
print(2 in filled_set)
# => True
print(10 in filled_set)
# => False
