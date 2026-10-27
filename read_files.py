from pathlib import Path
path = Path("./learing_python.txt") # 由于文本和当前代码文件在同一文件夹下，所以为了简便使用相对路径
content = path.read_text()
print(content)
lines = content.splitlines()  # 里面的各个元素就是文件的每行
for line in lines:  # 遍历列表的每行
    print(line)
