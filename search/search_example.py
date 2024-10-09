import sqlite3

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

# 查找包含特定词的句子
def search_text(cursor, search_word):
    cursor.execute("SELECT content FROM ancient_texts WHERE content LIKE ?", ('%' + search_word + '%',))
    return cursor.fetchall()

def main():
    db_file = 'ancient_texts.db'
    conn, cursor = connect_db(db_file)

    # 第一次使用，需要创建表
    create_table(cursor)

    # 清除表中内容
    clear_table(cursor)

    texts = [
        ('海内存知己，天涯若比邻。',),
        ('威加海内兮归故乡， 安得猛士兮守四方！',),
        ('古者庖羲氏之王天下也，仰則觀象於天，俯則觀法於地，視鳥獸之文與地之宜，近取諸身，遠取諸物；於是始作《易》八卦，以垂憲象。及神農氏，結繩為治，而統其事。庶業其繁，飾偽萌生。黃帝史官倉頡，見鳥獸蹄迒之跡，知分理之可相別異也，初造書契。百工以乂，萬品以察，蓋取諸夬。',),
    ]
    insert_texts(cursor, texts)

    conn.commit()

    search_word = '海内'
    result = search_text(cursor, search_word)

    for row in result:
        print(row[0])

    conn.close()

if __name__ == '__main__':
    main()