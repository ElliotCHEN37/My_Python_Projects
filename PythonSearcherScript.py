import webbrowser #利用“webbrowser”模塊以達到開啟瀏覽器標簽頁的效果

print("Welcome") #問候語
while True: #重複無限次直到出現“break”指令
    Eng = input("Please choose search engine(1)Google(2)Bing(3)Wikipedia(4)Exit: ") #詢問選項
    if Eng in ("1", "2", "3", "4"): #輸入的選項
        if Eng == "1": #偵測選項
            q = input("What's your Question: ") #詢問問題
            url = f'https://www.google.com/search?q={q}' #預先寫好的URL地址
            webbrowser.open(url, new=2) #使用“webbrowser”模塊訪問
        elif Eng == "2":
            q = input("What's your Question: ")
            url = f'https://www.bing.com/search?q={q}'
            webbrowser.open(url, new=2)
        elif Eng == "3":
            q = input("What's your Question: ")
            url = f'https://zh.wikipedia.org/w/index.php?search={q}'
            webbrowser.open(url, new=2)
        elif Eng == "4":
            print("Goodbye~") #結束語
            break #終止迴圈
