import sqlite3

# 连接到 SQLite 数据库（如果不存在则会创建）
conn = sqlite3.connect('news.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个表来存储两个字符串类型的数据
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                    id INTEGER PRIMARY KEY,
                    string1 TEXT,
                    string2 TEXT
                )''')

# # 插入数据
# data = ('Hello', 'World')
# cursor.execute('INSERT INTO my_table (string1, string2) VALUES (?, ?)', data)
# cursor.execute('INSERT INTO my_table (string1, string2) VALUES (?, ?)', data)
# cursor.execute('INSERT INTO my_table (string1, string2) VALUES (?, ?)', data)
search_string1 = 'Hello'
search_string2 = 'yyyyyyyy'
cursor.execute("SELECT * FROM my_table WHERE string1 = ? OR string2 = ?", (search_string1, search_string2))

# 获取查询结果
result = cursor.fetchall()
print(result)
# 提交更改
conn.commit()

# 关闭连接
conn.close()
