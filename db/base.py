from operator import truediv
import psycopg2


class Base:
    def __init__(self):
        self.conn = None

    def db_connect(self):
        try:
            self.conn = psycopg2.connect(
                database="inventory",
                user="postgres",
                password="postgres2019",
                host="127.0.0.1",
                port="5432",
            )
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            return e

    def db_cursor(self):
        return self.cursor

    def get_records(self, table):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def save_record(self, *args, **kwargs):
        query = f"INSERT INTO {kwargs['table']} (category_code,category_name,long_desc) VALUES (%s,%s,%s)"
        self.cursor.execute(query, (args))
        self.conn.commit()
        return True

    def search_items(self, table, keyword):
        query = f"SELECT * FROM {table} WHERE category_code LIKE '%{keyword}%'"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
