# _*_ coding:utf-8 _*_
# Filename: test_apriori.py
# Author: pang song
# python 3.6
# Date: 2018/04/22
# 利用Apriori算法，从而发现该某一时段内使用最频繁的智能家居组合

# 计算频率
def get_frequency(use_data,target):
    frequency = 0
    for key in use_data:
        if target in use_data[key]:
            frequency += 1
    return frequency

# 利用支持度，取得基础频繁项集（1个元素）
def get_frequency_list_first(use_data,sup):
    frequency_list_1 = []
    for key in use_data:
        for target in use_data[key]:
            if get_frequency(use_data,target) >= sup:
                if target not in frequency_list_1:
                    frequency_list_1.append(target)
    return frequency_list_1

# 从1个元素度频繁项，生成2个元素度频繁项
def get_frequency_list_second(frequency_list_1):
    frequency_list_2 = []
    frequency_list_2_item = []
    max_num = len(frequency_list_1)
    for i in range(max_num):
        frequency_list_2_item.append(frequency_list_1.pop(0))
        for item in frequency_list_1:
            frequency_list_2_item.append(item)
            # print(frequency_list_2_item)
            frequency_list_2.append(frequency_list_2_item.copy())
            frequency_list_2_item.remove(item)
        frequency_list_2_item = []
    return frequency_list_2

# 候选频繁项计数
def get_frequency_by_list(use_data,f_set):
    # f_set形如 ['A', 'B']
    f_set_count = 0
    count_temp = 0
    for key in use_data:
        for item in f_set:
            if item in use_data[key]:
                count_temp += 1
        if count_temp == len(f_set):
            f_set_count += 1
        count_temp = 0
    # print(f_set, f_set_count)
    return f_set_count

# 从n个元素，生成n+1个频繁元素集合
def get_frequency_list_n(f_set):
    frequency_list_n = []
    f_set_temp = f_set.copy()
    # print(f_set_temp)
    for set_in_f_set in f_set:
        f_set_temp.pop(0)
        for else_set in f_set_temp:
            for i in range(len(set_in_f_set)-1):
                if set_in_f_set[i] != else_set[i]:
                    break
                if i == len(set_in_f_set) - 2:
                    # 前n项都相等
                    frequency_list_n_item = set_in_f_set.copy()
                    frequency_list_n_item.append(else_set[-1])
                    frequency_list_n.append(frequency_list_n_item)
                    # print(frequency_list_n)
    return frequency_list_n

# 频繁项集函数
def main_apriori(data,sup):
    # 生产频繁项（1个元素）
    f_list_n = get_frequency_list_first(data, sup)
    f_list_n.sort()
    print('所有使用过的智能设备为：', f_list_n)
    for set1 in f_list_n:
        print(set1,get_frequency_by_list(data, set1))

    while len(f_list_n) > 1:
        if len(f_list_n[0]) == 1:
            f_list_n = get_frequency_list_second(f_list_n)
        else:
            f_list_n = get_frequency_list_n(f_list_n)
        # print(f_list_n)
        for set in f_list_n.copy():
            # 去除小于支持度的频繁项
            if get_frequency_by_list(data, set) < sup:
                f_list_n.remove(set)
                # print('remove is', set)

        for set3 in f_list_n:
            print(set3, get_frequency_by_list(data, set3))
    return f_list_n

if __name__ == '__main__':
    '''
    定义测试数据集合：
    前面数字为日期，以下为智能家居代号
    A 代表 灯
    B 代表 空调
    C 代表 电视机
    D 代表 电饭煲
    E 代表 空气净化器
    data 为每天17：00至18：00智能家电使用记录
    '''
    data = {
        '20170619': ['A', 'C', 'D', 'E'],
        '20170620': ['A', 'B', 'C', 'D'],
        '20170621': ['A', 'B', 'C', 'D', 'E'],
        '20170622': ['A', 'C', 'D', 'E'],
        '20170623': ['A', 'B', 'C', 'D'],
        '20170624': ['A', 'C', 'E'],
        '20170625': ['A', 'B', 'D', 'E'],
        '20170626': ['A', 'B', 'E'],
        '20170627': ['A', 'B', 'C']
    }

    # 设定支持度，出现频次超过支持度才认为是频繁项
    sup = 5
    print('该时段常用设备组合为：',main_apriori(data,sup))