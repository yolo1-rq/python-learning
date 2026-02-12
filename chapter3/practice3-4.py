list = ['4577','8855','1807','朱小葵','迪迪大王']
message = f"尊敬的{list[1]},可以邀请你一起吃晚餐吗？"
print(message)
pity = list.pop(4)
print(list)
print(f"{pity}无法参加聚餐")
list[0]='卤蛋'
print(list)
message = f"尊敬的{list[0]},可以邀请你一起吃晚餐吗？"
print(message)
list.insert(0,'可爱鬼')
list.insert(3,'瑞酱')
list.append('小杨')
print(list)
print(f"亲爱的{list[4]},因为找到了更大的桌子,想邀请你一起吃晚餐")
print("抱歉,只能邀请两位聚餐")
new_pity = list.pop()
print(f"非常抱歉{new_pity},不能邀请你共进晚餐")
new_pity = list.pop()
print(f"非常抱歉{new_pity},不能邀请你共进晚餐")
new_pity = list.pop()
print(f"非常抱歉{new_pity},不能邀请你共进晚餐")
new_pity = list.pop()
print(f"非常抱歉{new_pity},不能邀请你共进晚餐")
print(list)
new_pity = list.pop()
print(f"非常抱歉{new_pity},不能邀请你共进晚餐")
print(list)
print(f"亲爱的{list[0]},不要忘记我们的聚餐")
print(f"亲爱的{list[-1]},不要忘记我们的聚餐")
del list[0]
del list[0]
print(list)