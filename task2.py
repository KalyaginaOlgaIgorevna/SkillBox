import requests
import re

def extract_h3_headings(url):
    try:
        # Получаем HTML-контент страницы
        response = requests.get(url)
        response.raise_for_status()

        # Используем регулярное выражение для извлечения текста из тегов <h3>
        headings = re.findall(r'<h3[^>]*>(.*?)</h3>', response.text)

        return headings
    except requests.RequestException as e:
        return f"Ошибка при запросе: {e}"

url = "https://www.w3schools.com/html/html_examples.asp"
headings = extract_h3_headings(url)
print(headings)