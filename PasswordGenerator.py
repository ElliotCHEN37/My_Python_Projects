import random #“random”模塊用於產生隨機數
import string #“string”模塊用於快速調用字符與數字

num = string.digits #導入數字
ABC = string.ascii_letters #導入所有ASCII大小寫字母
PSD = list(num + ABC) #密碼的樣式
random.shuffle(PSD) #使用“random”模塊打亂密碼順序
LEN = int(input("How long password do you need?: ")) #詢問密碼長度並將回答轉換為數字
PAS = "".join(PSD[:LEN]) #生成需要的長度的密碼
print(f"Your password is：{PAS}") #輸出密碼
