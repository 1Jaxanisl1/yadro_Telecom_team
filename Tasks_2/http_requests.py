import requests
import sys

# Функция для запросов
def make_request(url):
    if url.endswith('/100'):
        print(f"Пропускаем запрос к {url} (специфика httpstat.us/100)")
        return

    try:
        # Получаем ответ
        response = requests.get(url)
        # Проверяем код ответа
        if response.status_code // 100 in [2, 3]:
            print(f"Успешный ответ от {url}")
            print(f"Статус код: {response.status_code}")
            print(f"Тело ответа: {response.text}")
        else:
            # Исключение ошибок для 4хх, 5ххх
            raise Exception(f"Ошибка при запросе к {url}. Статус код: {response.status_code}. Тело ответа: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка при выполнении запроса к {url}: {str(e)}")

def main():
    # Список URL для тестирования разных статус кодов
    urls = [
        "https://httpstat.us/100",  # 1xx
        "https://httpstat.us/200",  # 2xx
        "https://httpstat.us/300",  # 3xx
        "https://httpstat.us/400",  # 4xx
        "https://httpstat.us/500"   # 5xx
    ]
    
    for url in urls:
        try:
            make_request(url)
        except Exception as e:
            print(f"Ошибка: {str(e)}\n", file=sys.stderr)

if __name__ == "__main__":
    main()