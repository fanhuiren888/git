#!/usr/bin/python
# -*- coding: utf-8 -*

# 【项目一】统计成绩
#
# 从成绩单文件 report.txt（点击下载）中读取班级成绩，并完成统计分析。
#
#     姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理
#     小A 89 94 90 96 89 92 54 73 80
#     小B 92 37 93 43 67 77 82 84 89
#     小C 90 88 87 89 82 79 79 80 82
#     ...
#
# 要求：
#
#     读取 report.txt 文件中的成绩；
#     统计每名学生总成绩、计算平均并从高到低重新排名；
#     汇总每一科目的平均分和总平均分（见下表第一行）；
#     添加名次，替换60分以下的成绩为“不及格”；
#     将处理后的成绩另存为一个新文件。
#
# 结果展示：
#
#     名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分
#     0 平均 72 67 76 47 63 73 77 73 82 630 70.0
#     1 小S 94 90 96 89 92 84 83 80 82 790 87.8
#     2 小D 90 88 87 89 82 79 79 83 85 762 84.7
#     3 小A 89 94 90 96 89 92 不及格 73 80 757 84.1
#     ...
#     21 小K 82 不及格 83 63 66 67 72 83 86 638 70.9

def showSumAvg():  # 统计每名学生总成绩、计算平均并从高到低重新排名
    temp = []  # 创建一个临时序列，存放处理后的结果
    with open('file/score.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
    for i in content:  # 遍历读取的内容
        lines = i.split()  # 分离出每个同学
        psum = 0  # 个人总成绩
        project = 0  # 总科目
        for j in lines[1:]:  # 遍历每一个同学的所有成绩
            project += 1  # 每遍历一次科目数+1
            psum += int(j)  # 个人总成绩 = 每一科成绩相加
        avg = psum / project  # 平均分 = 总成绩 / 总科目
        avg1 = '%.1f' % avg
        lines.append(str(psum))  # 把个人总成绩放入每个同学中
        lines.append(str(avg1))  # 把个人平均分放入每个同学中
        temp.append(lines)  # 把每个同学处理后的成绩再放入临时的序列
    # m = sorted(temp, key=lambda x: x[-1] ,reverse = True)
    temp.sort(key=lambda x: x[-1], reverse=True)  # 序列按要求排序
    return temp  # 返回序列


def summarize():  # 汇总每一科目的平均分和总平均分
    result = ['0', '平均']  # 存放处理后的结果
    temp = showSumAvg()  # 获取处理过的数据
    for n in range(1, 12):  # 控制科目列数
        person = 0  # 学生人数
        sum = 0  # 单科目成绩总和
        for a in temp:  # 遍历之前处理过的数据
            person += 1  # 记录学生人数
            sum += float(a[n])  # 全班成绩  由于之前的成绩里分数有小数，所以这里转换成float 类型   a[n] :表示第a个学生的第n科成绩
        avg = sum / person  # 平均分 = 全班成绩总和 / 人数
        avg1 = '%.1f' % avg  # 格式化处理，保留1位小数
        result.append(str(avg1))  # 所有的平均分添加至结果

    return result,temp

def sort():     #排名次，并替换60分以下为不及格
    head = ['名次', '姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '总分', '平均分']
    result,temp = summarize()   #获取数据
    p = 0                       #学生人数
    for i in temp:              #遍历数据
        p += 1                  #计数
        i.insert(0,str(p))      #加入序号
        count= 2                #从第二列开始查
        for j in i[2:-2]:  # 遍历每一个学生的成绩
            if int(j) <= 60:  # 找出60分以下的成绩
                i[count] = '不及格'  # 替换为不及格
                count += 1      #如果有小于60分 先替换，然后列+1
            else:
                count += 1      #如果没有，列+1 再查下一列
    temp.insert(0,result)   #把计算的平均值放入temp列表
    temp.insert(0,head)     #给列表添加表头
    return temp


def showTime():
    temp = sort()
    try:
        file = open('file/newscore','w',encoding='utf-8')
        for i in temp:
            file.writelines('\n')
            for j in i:
                result = '%s\t\t'%j
                file.writelines(result)
    except IOError:
        print("文件写入有误")
    finally:
        file.close()



if __name__ == '__main__':
    showTime()
