import sqlite3
import re
import argparse
from SyllSeg import SyllSeg

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

    db_file = './ancient_texts.db'
    conn, cursor = connect_db(db_file)
    
    syllables = SyllSeg().seg(target)
    if syllables:
        target = "|" + "%|".join(syllables)
        strict_pattern = r"\|" + r"[^\|]*?\|".join(syllables)
    # print(target)
    # print(strict_pattern)
    
    result = search_text(cursor, target)
    for row in result:
        if re.findall(strict_pattern, row[0]):
            print(row[0])


    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='待匹配的目标拼音')

    args = parser.parse_args()
    main(args.target)