from flask import Flask, render_template, request

app = Flask(__name__)

# 新增文件读取和写入函数
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

@app.route('/', methods=['GET', 'POST'])
def home():
    file_path = 'read.txt'
    if request.method == 'POST':
        # 获取表单数据并写入文件
        content = request.form['content']
        # no need to write back to file.
        # write_file(file_path, content)  # 新增：将内容写入文件
        return render_template('index.html', content=content)  # 返回更新后的内容
    else:
        # 读取文件内容
        content = read_file(file_path)
        return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)