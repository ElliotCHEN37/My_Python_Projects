import random

商品價格 = random.randint(1,500)
A玩家 = input("請輸入A玩家暱稱: ")
B玩家 = input("請輸入B玩家暱稱: ")
回答次數 = 1
總次數 = 10
print(f"歡迎來到“猜價格”的遊戲")
print(f"遊戲規則：")
print(f"該遊戲總共有10輪。每個玩家輪流回答。誰先答對，誰就贏了！")
print(f"小提示：")
print(f"商品價格在1~500之間")
while 回答次數 <= 總次數:
    A作答 = int(input(f"請{A玩家}輸入商品的金額: "))
    B作答 = int(input(f"請{B玩家}輸入商品的金額: "))
    if A作答 == 商品價格 or B作答 == 商品價格:
        break
    elif abs(商品價格 - A作答) <= abs(商品價格 - B作答):
        print(f"{A玩家}的回答更接近答案！")
    else:
        print(f"{B玩家}的回答更接近答案")
    回答次數 += 1
if A作答 == 商品價格 and B作答 == 商品價格:
    print(f"{A玩家}和{B玩家}都猜對了！這局是平局！")
elif A作答 == 商品價格:
    print(f"{A玩家}猜對了！獲勝者是{A玩家}！")
elif B作答 == 商品價格:
    print(f"{B玩家}猜對了！獲勝者是{B玩家}！")
elif abs(商品價格 - A作答) <= abs(商品價格 - B作答):
    print(f"商品價格為{商品價格}，{A玩家}的回答更接近答案。所以{A玩家}獲勝！")
else:
    print(f"商品價格為{商品價格}，{B玩家}的回答更接近答案。所以{B玩家}獲勝！")
