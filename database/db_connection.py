import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="MusicShop",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            client_encoding="UTF8"
        )
        return connection
    except Exception as e:
        print("Ошибка подключения к базе данных:", e)
        return None
