import sqlite3
import re
import argparse

# 连接数据库
def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor

def remove_pinyin(text):
    # 匹配中文及中文标点，去除后面的拼音部分
    result = re.match(r"[\u4e00-\u9fa5，。？！：；“”‘’（）《》【】]+", text)
    return result.group(0) if result else text

# 查找包含特定词的句子
def search_text(cursor, search_word):
    cursor.execute("SELECT content FROM ancient_texts WHERE content LIKE ?", ('%' + search_word + '%',))
    return cursor.fetchall()

def main(target):
    if not args:
        print('请输入目标拼音')
        return

    db_file = 'ancient_texts.db'
    conn, cursor = connect_db(db_file)

    result = search_text(cursor, target)
    clean_result = [remove_pinyin(row[0]) for row in result]

    for row in clean_result:
        print(row)

    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='待匹配的目标拼音')

    args = parser.parse_args()
    main(args.target)