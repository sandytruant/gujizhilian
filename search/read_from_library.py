import sqlite3
from pypinyin import lazy_pinyin

# 连接数据库
def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor

# 创建表
def create_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ancient_texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT UNIQUE NOT NULL
    );
    ''')

# 清除表中内容
def clear_table(cursor):
    cursor.execute('DELETE FROM ancient_texts')

# 插入古籍内容（可以批量插入）
def insert_texts(cursor, texts):
    cursor.executemany('INSERT OR IGNORE INTO ancient_texts (content) VALUES (?)', texts)

def main():
    library_file = 'library.txt'
    db_file = 'ancient_texts.db'
    conn, cursor = connect_db(db_file)

    # 第一次使用，需要创建表
    create_table(cursor)

    clear_table(cursor)

    with open(library_file, 'r', encoding='utf-8') as fp:
        for line in fp:
            text = line.strip()
            pinyin_text = ''.join(lazy_pinyin(text))
            insert_texts(cursor, [(text + pinyin_text,),])
    
    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()