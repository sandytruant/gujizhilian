### 使用方法

需要安装的软件：
- SQLite（https://www.sqlite.org/download.html）
- Python（以及pypinyin库）

```bash
# 从library.txt读取文献中的句子，会生成ancient_texts.db
python read_from_library.py
# 根据拼音从数据库中检索匹配的句子，例如：检索“hainei”
python search.py hainei
```
这样会输出：  
海内存知己，天涯若比邻。  
威加海内兮归故乡，安得猛士兮守四方！