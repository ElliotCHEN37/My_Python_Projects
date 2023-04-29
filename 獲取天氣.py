import requests
import webbrowser

金鑰 = input(f"請問您有API金鑰嗎?(y)有(n)沒有：")
if 金鑰 in ("y", "n"):
    if 金鑰 == "y":
        API = input(f"請輸入您的API金鑰：")
    elif 金鑰 == "n":
        url = f'https://home.openweathermap.org/api_keys'
        webbrowser.open(url, new=2)
城市 = input(f"請輸入需要查詢的城市：")
網址 = f"https://api.openweathermap.org/data/2.5/weather?q={城市}&appid={API}"
天氣資料 = requests.get(網址)
氣溫 = int(天氣資料.json()["main"]["temp"]-273.15)
最低氣溫 = int(天氣資料.json()["main"]["temp_min"]-273.15)
最高氣溫 = int(天氣資料.json()["main"]["temp_max"]-273.15)
print(f"現在{城市}氣溫為{氣溫}度，最高氣溫為{最高氣溫}度，最低氣溫為{最低氣溫}.")
