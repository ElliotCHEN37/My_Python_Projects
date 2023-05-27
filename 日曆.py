import calendar #必須導入“calendar”（用於顯示日曆）否則無法使用

year = int(input("Year：")) #將輸入後的字符轉換為數字
moon = int(input("Month："))

print(calendar.month(year, moon)) #顯示日曆
