# 估算流水
# 1.流水公式，dau * 付费率 * 付费金额 = 日流水
# 2.多日dau = 新增人数（当天DAU）+之前每天的新增人数*留存率
# 3.新增DAU = 每日新增人数
# 4.留存率 = 40% ~ 50%

# 广告投放
# 1.渠道的广告投放，具体金额不同
# 2.支付通道费用，各大渠道不同
# 3.渠道分成，安卓 和 苹果

# 与渠道分成后
# 1.渠道分成后
# 2.再与发行分成
# 3.我们所得=我们分成-人员成本
# 4.奖金=我们所得*奖金系数/团队成员*不同成员奖金系数

# 汇总数据
# 1.月总流水
# 2.总支付通道费
# 3.总广告投入
# 4.净赚
# 5.奖金人数
# 6.奖金

'''
======================== 以下为代码实现部分========================
'''

# 需要的计算库
import xlrd
# 下面为定义好的参数

print("需要在你的D盘gameliushui文件夹下创建shuju.xlsx数据表，具体为：D:\gameliushui\shuju.xlsx,\n"
      "其中第一列为天数，第二列为新增。天数与新增需要保持一致，第一列表头为：天数，第二列表头为：新增")
print()
print("计算方法：dau * 付费率 * arppu ，已考虑DAU迭代问题，如第2天的dau=第2天的新增+第1天的老玩家")
print("请输入下面需要的参数后，继续运行。")
def jisuanliushui():
    fflv = float(input('输入付费率，仅支持小数：'))                  # 定义付费率 10%
    liucunlv =float(input('输入留存率，仅支持小数：'))             # 定义留存率 40%  其实也可以改成留存列表，因为每天的留存不一样
    arppu = float(input('输入arppu，可以为小数或整数：'))               # 定义ARPPU 200
    # xinzeng_List = [10,10,10]  # 定义新增玩家数据
    qian_xinzeng_List = []
    qian_day_List =[]
    xinzeng_List = []
    day_List =[]

    # day_List = [1,2,3]               # 计算天数
    huizong_liushui = []             # 定义汇总流水列表
    old_dauList =[]                  # 定义旧的dau列表，除新增之外的

    file = 'D:\\gameliushui\\shuju.xlsx'
    wb =xlrd.open_workbook(file)      # 打开D:\gameliushui\shuju.xlsx
    sheet = wb.sheet_by_index(0)   # 激活使用excel表第一个sheet页，支持中文名
    ncols = sheet.ncols
    for i in range(0,ncols):

        if i == 0:
            i_value_day = sheet.col_values(i)
            # print(i_value_day)
            qian_day_List.append(i_value_day)
        else:
            i_value_xinzeng = sheet.col_values(i)
            # print(i_value_xinzeng)
            qian_xinzeng_List.append(i_value_xinzeng)

    qian_day_day = 0
    qian_zeng_zeng =0
    for qian_day in qian_day_List:
        if qian_day != 'Null':
            # print(qian_day)
            qian_day_day = qian_day
    for qian_xinzeng in qian_xinzeng_List:
        if qian_xinzeng != 'Null':
            # print(qian_xinzeng)
            qian_zeng_zeng = qian_xinzeng

    # 往下就没有被执行！大爷的我就
    for day in range(0,len(qian_day_day)):
        if day < 1:
            continue
        else:
            day_value = qian_day_day[day]
            day_List.append(day_value)
            # print(day_List)

    for xinzeng in range(0,len(qian_zeng_zeng)):
        if xinzeng < 1:
            continue
        else:
            xinzeng_value = qian_zeng_zeng[xinzeng]
            xinzeng_List.append(xinzeng_value)

    for i in range(len(xinzeng_List)):
        calc_liushui = float(sum(old_dauList)) + float((xinzeng_List[i])) * float(fflv) * float(arppu)
        huizong_liushui.append(calc_liushui)
        old_dauList.append(float(xinzeng_List[i]) * float(liucunlv))
        print("第"+str(day_List[i])+"天"+"流水是："+str(calc_liushui))
    print("预估当月总流水："+str(sum(huizong_liushui)))
    a = input("是否继续使用该程序？输入y继续，其他键退出")
    while True:
        if a == 'y' or a == 'Y':
            jisuanliushui()
        else:
            exit()

if __name__ == '__main__':
    a = input("准备好数据excel后，输入y回车，开始执行：")
    if a == 'y':
        jisuanliushui()
    print()




