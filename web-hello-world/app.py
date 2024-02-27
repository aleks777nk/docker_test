import os 
import json
import datetime
from flask import Flask

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Как записывается путь в BASE_FOLDER C:\Users\Probe-Above4decoding\OneDelivery\web-hello-world
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources") # Как записывается путь в RESOURCE_DIR C:\Users\Probe-Above4decoding\OneDelivery\web-hello-world\resources
print('Как записывается путь в RESOURCE_DIR ', RESOURCE_DIR, 'Как записывается путь в BASE_FOLDER ', BASE_FOLDER, sep='\n')
print('Как записывается путь в BASE_FOLDER через os ', os.path.join(BASE_FOLDER, "resources", "response.json"), sep='\n')
print('Как записывается raw путь ', r'C:\Users\Probe-Above4decoding\OneDelivery\web-hello-world\resources\response.json', 'с которым все корректно работает')
RESOURCE_DIR_path = (os.path.join(RESOURCE_DIR, 'response.json'))
RAW_path = (r'C:\Users\Probe-Above4decoding\OneDelivery\web-hello-world\resources\response.json')
print('Сравнение записи пути ', RESOURCE_DIR_path==RAW_path) #Не запускался код изза опечатки в слове resurces, а я написал resourses и почти 2 часа искал в чем причина. Зато узнал как тут все устроено)
@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR, 'response.json')) as f:
        data = json.load(f)
        payload = data.get("payload", "string")
        current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        return f"{payload} - {current_time}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
    
"""Эта запись является логом доступа (access log) вашего веб-сервера, который отражает запросы, поступающие к серверу и ответы, возвращаемые сервером.
Давайте разберем каждую часть записи:
-127.0.0.1: Это IP-адрес клиента, который делает запрос к серверу. В данном случае это локальный IP-адрес (localhost), который обычно используется для доступа к серверу с того же компьютера, на котором он запущен.
-[26/Feb/2024 12:07:51]: Это временная метка запроса, которая указывает дату и время, когда запрос был получен сервером. В данном случае это 26 февраля 2024 года в 12:07:51.
-"GET / HTTP/1.1": Это метод запроса (GET), запрошенный URL (/), и версия протокола HTTP (HTTP/1.1). Этот запрос означает, что клиент отправил GET-запрос на главную страницу вашего сайта.
-200: Это статус ответа сервера. Код состояния 200 означает успешное выполнение запроса. В данном случае, сервер успешно обработал запрос и вернул запрошенную страницу.
-127.0.0.1 - - [26/Feb/2024 12:07:51] "GET /favicon.ico HTTP/1.1" 404 -: Это еще один запрос на получение иконки сайта (favicon.ico). Здесь также указан локальный IP-адрес клиента, метод запроса (GET), запрошенный URL (/favicon.ico), версия протокола HTTP (HTTP/1.1), статус ответа (404) и отсутствие передаваемых данных (для дополнительной информации).
-Статус ответа 404 означает, что запрошенный ресурс (в данном случае, иконка сайта) не был найден на сервере"""