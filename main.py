from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# Функция для таймера
def start_timer(duration, callback):
    def timer_thread():
        time.sleep(duration)
        callback()
    thread = threading.Thread(target=timer_thread)
    thread.start()

# Коллбек для завершения таймера
def timer_done():
    print("Таймер завершен!")

@app.route('/alice', methods=['POST'])
def main():
    alice_request = request.json
    command = alice_request.get('request', {}).get('command', '').lower()

    if 'старт помидора' in command:
        duration = 25 * 60  # 25 минут
        start_timer(duration, timer_done)
        response_text = 'Таймер "Помидора" на 25 минут запущен!'
    elif 'стоп помидора' in command:
        response_text = 'Таймер "Помидора" остановлен.'
        # Логика остановки таймера (если необходимо)
    else:
        response_text = 'Я могу запустить или остановить таймер "Помидора". Скажите "старт помидора" или "стоп помидора".'

    response = {
        "version": "1.0",
        "session": alice_request['session'],
        "response": {
            "end_session": False,
            "text": response_text
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
