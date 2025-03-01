import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def create_database():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT,
        temperature REAL
    )
    ''')
    conn.commit()
    conn.close()

def get_current_temperature():
    url = 'https://sinoptik.ua/pohoda/chernihiv'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature_tag = soup.find('p', class_='today-temp')
    if temperature_tag:
        temperature = temperature_tag.text.strip().replace('°C', '')
        return float(temperature)
    else:
        raise Exception('Не вдалося знайти інформацію про температуру на сайті.')

def insert_temperature_to_db(temperature):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO weather (datetime, temperature)
    VALUES (?, ?)
    ''', (current_datetime, temperature))
    conn.commit()
    conn.close()

def main():
    create_database()
    try:
        current_temperature = get_current_temperature()
        insert_temperature_to_db(current_temperature)
        print(f'Дані успішно додані до бази даних: {current_temperature}°C на {datetime.now()}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()