import requests, os

def ensure_file_exists():
    if not os.path.isfile("fliztoken.txt"):
        with open("fliztoken.txt", "w"):
            pass

def read_shop_key():
    if os.path.isfile("fliztoken.txt"):
        with open("fliztoken.txt", "r") as f:
            return f.read().strip()
    return None


def save_shop_key(key):
    with open("fliztoken.txt", "w") as f:
        f.write(key)

def display_info(data, fields):
    for field in fields:
        value = data['info'].get(field, "")
        print(f"{field.replace('_', ' ').title()}: {value}")

def get_server_info(api_token, ip, port, gamemode):
    url = "https://api.flizan.ru/api/getstatusserver"
    params = {
        "server_ip": ip,
        "server_port": port,
        "game": gamemode,
        "api_key": api_token
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        data = response.json()
        fields = [
            "HostName", "Map", "Players", 
            "MaxPlayers", "Protocol", "ModDir", 
            "ModDesc", "AppID", "Bots", 
            "Dedicated", "Os", "Password", 
            "Secure", "Version", "ExtraDataFlags", 
            "GamePort", "SteamID"
        ]
        display_info(data, fields)

def start():
    ensure_file_exists()
    api_token = read_shop_key()
    if not api_token:
        fliz_token = input("Введите ваш апи ключ FlizanAPI\nПолучить можно тут - https://api.flizan.ru/\n")
        save_shop_key(fliz_token)
        print("Ключ сохранен, перезапустите программу.")
        return
    while True:
        choice = input("Выберите действие.\n1. Просмотр информации о сервере\n2. Выход\n")
        if choice == "1":
            ip = input("Введите айпи адрес сервера: ")
            port = input("Введите порт сервера: ")
            gamemode = input("Введите игру\nВажно! Работает только с source играми (в том числе и с cs2)\nПример: gmod\n")
            get_server_info(api_token, ip, port, gamemode)
        elif choice == "2":
            break
        else:
            print("Такого выбора нету!")
            start()
if __name__ == "__main__":
    start()
