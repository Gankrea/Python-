"""
许多逻辑的判断是嵌套的多层次的,对于这种需求我们可以
自由组合if elif else完成特定的需求

基础语法格式(空格来决定属于哪个嵌套判断)
if 条件1:
    满足条件所执行的代码1
    if 条件2:(注意，该if有4个空格缩进，所以属于外层的if)
    满足条件所执行的代码2

嵌套判断语句可以用于多条件，多层次的逻辑判断
嵌套判断语句，需要注意空格缩进，python中使用空格缩进来决定层次关系
"""

# if int(input("请输入你的身高(cm)：")) > 120:
#     print("你的身高超过限制！但是！！！")
#     vip = int(input("如果你是vip用户则可以免费，输入你的vip等级(0-1)："))
#     if vip ==1:
#         print(print("尊贵的vip用户，你可以免费玩"))
#     else:
#         print("请缴费")
# else:4
#     print("小朋友可免费游玩")

if int(input("输入你的年龄")) >= 18 < 30:
    if int(input("请输入你的在职时长")) > 2:
        print("可以抽奖（在职时长达成）")
    elif int(input("输入你的级别"))>3:
        print("可以抽奖（级别达成）")
    else:
        print("两种都不达标，不能抽奖")
else:
    print("年龄不达标，不能抽奖")