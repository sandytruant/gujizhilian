import sqlite3
import re
import argparse
from flask import Flask, request, jsonify
from flask_cors import CORS
from SyllSeg import SyllSeg

app = Flask(__name__)
CORS(app)

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
    cursor.execute("SELECT content, source FROM ancient_texts WHERE content LIKE ?", ('%' + search_word + '%',))
    return cursor.fetchall()

@app.route('/trust', methods=['GET'])
def trust():
    return "Trusted."

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    page = int(request.args.get('page', ''))
    print(page)
    # query = input()
    if not query:
        return jsonify([])

    db_file = './ancient_texts_zh.db'
    conn, cursor = connect_db(db_file)
   
    syllables = SyllSeg().seg(query)
    if syllables:
        query = "|" + "%|".join(syllables)
        strict_pattern = r"\|" + r"[^\|]*?\|".join(syllables)
    # print(target)
    # print(strict_pattern)
    
    result = search_text(cursor, query)
    # print(result)
    
    conn.close()
    
    # 处理逻辑有点问题    
    clean_result = [(remove_pinyin(row[0]), row[1]) for row in result if re.findall(strict_pattern, row[0])]
    
    
    final_res =     [
        {
            'id': i,
            'name': clean_result[i][0],
            'description': clean_result[i][1]
        }
        for i in range(0+10*(page-1), min(len(clean_result), 10+10*(page)))
        # for i in range(10)
    ]+ \
        [
        {
        "num": len(clean_result)
        }
    ]
    with app.app_context():
        return jsonify(final_res)


@app.route('/search-zhs', methods=['GET'])
def search_zhs():
    query = request.args.get('query', '')
    page = int(request.args.get('page', ''))
    # query = input()
    if not query:
        return jsonify([])

    db_file = './ancient_texts_zhs.db'
    conn, cursor = connect_db(db_file)
   
    syllables = SyllSeg().seg(query)
    if syllables:
        query = "|" + "%|".join(syllables)
        strict_pattern = r"\|" + r"[^\|]*?\|".join(syllables)
    # print(target)
    # print(strict_pattern)
    
    result = search_text(cursor, query)
    print(result)
    
    conn.close()
    
    # 处理逻辑有点问题    
    clean_result = [(remove_pinyin(row[0]), row[1]) for row in result if re.findall(strict_pattern, row[0])]
    
    final_res =      [
        {
            'id': i,
            'name': clean_result[i][0],
            'description': clean_result[i][1]
        }
        for i in range(0+10*(page-1), min(len(clean_result), 10+10*(page)))
        # for i in range(10)
    ] + \
        [
        {
        "num": len(clean_result)
        }
    ]
    with app.app_context():
        return jsonify(final_res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
