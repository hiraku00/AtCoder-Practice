import sqlite3

DB_FILE = "sample_db.sqlite"

def create_db_and_table():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY,
                name VARCHAR(50),
                age INTEGER,
                gender VARCHAR(10)
            )
        """)
        conn.commit()
        print("データベースとテーブルが作成されました。")

    except sqlite3.Error as e:
        print(f'データベース操作エラー: {e}')

    finally:
        if conn:
            conn.close()

def insert_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        employees = [
            (1, '山田太郎', 30, '男性'),
            (2, '鈴木次郎', 25, '女性'),
            (3, '佐藤三郎', 35, '男性'),
            (4, '小林四郎', 28, '男性'),
            (5, '加藤五郎', 32, '女性'),
        ]

        cursor.executemany("""
            INSERT INTO employee (id, name, age, gender) VALUES (?, ?, ?, ?)
        """, employees)
        conn.commit()
        print("データが挿入されました。")

    except sqlite3.Error as e:
        print(f'データベース操作エラー: {e}')

    finally:
        if conn:
            conn.close()

def select_with_condition():
    """WHERE句で条件を指定してデータを参照する"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee WHERE age >= 30")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"データベース操作エラー: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_db_and_table()
    insert_data()
    select_with_condition()
