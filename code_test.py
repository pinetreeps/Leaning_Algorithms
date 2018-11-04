# _*_ coding:utf-8 _*_
# Filename: .py
# Author: pang song
# python 3.6
# Date: 2018/06/20

# --------题目2---------
# 兔子生兔子的问题
# 一对兔子第三个月"起"每个月都生一对兔子

# 我的实现 有些问题

def rabbit_bron(month):
    if month < 3:
        return 2
    elif month == 3:
        return 4
    else:
        return 2 * (month - 3) + 2 * rabbit_bron(month - 3) + rabbit_bron(month - 3)

print(rabbit_bron(4))



# exit()


# 网上的实现

f1 = 1
f2 = 1
for i in range(1, 22):
    print('%12ld %12ld' % (f1, f2),)
    if (i % 3) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2

exit()

a = [1,4]
b = [3]
print(a+b)
print(sum(a))
print(type(a))

exit()
# 同学的实现，初始条件可变
def cal_tuzi(list_tuzi, n):
    if n == 0:
        print(sum(list_tuzi))
    else:
        n -= 1
        list_tuzi = [sum(list_tuzi[1:]),] + list_tuzi
        cal_tuzi(list_tuzi, n)

for i in range(5):
    cal_tuzi([1,], i)
# exit()






# --------题目1---------
# 四个数取三个不重复的所有组合
# my_list = ["1","2","3","4","5"]
my_list = ["1","2","3","4","5"]
# my_list = [1,2,3,4,5]
your_list = []

print(enumerate(my_list))
for i, j in enumerate(my_list):
    print(i,j)
    print(type(i),type(j))



def fill_num(a_list, res_list):
    if len(a_list) == 1:
        print(res_list)
    else:
        for i, j in enumerate(a_list):
            a = a_list[:i] + a_list[i+1:]
            b = res_list + [j,]
            fill_num(a, b)

# fill_num(my_list, your_list)

exit()

# 1\2\3\4组合
num = [1,2,3,4]
for i1 in num:
    for i2 in num:
        for i3 in num:
            if i1 != i2 and i2 != i3 and i1 != i3:
                print(i1,i2,i3)



    # num_temp = num.copy()
