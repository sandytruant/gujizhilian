import sqlite3
from pypinyin import lazy_pinyin
import re, zhconv

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
        content TEXT UNIQUE NOT NULL,
        source TEXT
    );
    ''')

# 清除表中内容
def clear_table(cursor):
    cursor.execute('DELETE FROM ancient_texts')

# 插入（可以批量插入）
def insert(cursor, texts, source):
    cursor.execute('INSERT OR IGNORE INTO ancient_texts (content, source) VALUES (?, ?);', (texts, source))



def main(mode):
    library_file = 'library.txt'
    db_file = f'ancient_texts_{mode}.db'
    conn, cursor = connect_db(db_file)

    # 第一次使用，需要创建表
    create_table(cursor)

    clear_table(cursor)

    with open(library_file, 'r', encoding='utf-8') as fp:
        for line in fp:
            if mode=="zh":
                text = line.strip().split(' ')[0]
            elif mode=="zhs":
                text = zhconv.convert(line.strip().split(' ')[0], 'zh-cn')
            text1 = re.sub("[，。？！《》“”【】（）；：]","",text)
            pinyin_text = '|' + '|'.join(lazy_pinyin(text1))
            print(pinyin_text)
            if len(line.strip().split(' ')) > 1:
                insert(cursor, text + pinyin_text, line.strip().split(' ')[1])
            else:
                insert(cursor, text + pinyin_text, "出處不明")

    
    conn.commit()

    conn.close()

if __name__ == '__main__':
    main(mode="zh")