import sqlite3
import re
import argparse
from flask import Flask, request, jsonify
from flask_cors import CORS

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
    cursor.execute("SELECT content FROM ancient_texts WHERE content LIKE ?", ('%' + search_word + '%',))
    return cursor.fetchall()


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    # query = input()
    if not query:
        return jsonify([])

    db_file = './ancient_texts.db'
    conn, cursor = connect_db(db_file)

    result = search_text(cursor, query)
    conn.close()
    
    # 处理逻辑有点问题    
    clean_result = [remove_pinyin(row[0]) for row in result]
    
    final_res = [
        {
            'id': i,
            'name': clean_result[i],
            'description': "《十三經注疏》"
        }
        for i in range(len(clean_result))
    ]
    with app.app_context():
        return jsonify(final_res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
