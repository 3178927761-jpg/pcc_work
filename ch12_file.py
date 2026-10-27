"""电脑操作系统的目录结构
类Unix操作系统(Linux、macOS等)————目录结构会像树根一样，根节点叫根目录，用/表示，一切的文件、目录都存放在根目录下面
Windows操作系统，每个磁盘分区都有自己的根目录，用分区名加\表示
定位文件的路径有两种方法：
1.绝对路径：从根目录出发的路径，以根目录为基准，Unix操作系统绝对路径以/开头，路径中每个目录之间用/分隔，最后以目标文件或目标目录结尾
eg：/home/data       /home/data/a.py
Windows操作系统绝对路径以分区名+\开头，路径中每个目录之间用\分隔，最后以目标文件或目标目录结尾
eg:C:\home\ data      C:\home\data\a.py

2.相对路径:从一个参照位置出发，表示从那个位置来看，其他文件处于什么路径，相对路径用.来表示参照文件当前所在的目录，用..表示更上一层的父目录，
如果继续向上走，就用../..(..\..)表示当前文件所属目录的父目录的父目录
往下走，用/或\来分割路径中的目录
eg：home → .：当前目录      ./data:当前home文件夹里的data      上一级user → ..
../tmp：在home的上一级目录(/user)里      ../tmp/images    ../tmp/images/profile      ../tmp/images/profile/1.jpg
./可以省略，在同一目录下的文件想互相用相对路径找到彼此的话，可以直接使用文件名
pycharm右击点击文件，选择“复制路径/引用”，就可以获得那个文件的绝对路径以及以最顶层项目目录为参考的相对路径"""







from pathlib import Path      # from 模块名 import 类名
path = Path("./content.txt")   # 给Path类的构造函数传入文件路径，获得一个Path类的实例
print(path.read_text()) # 运行错误的原因：找不到content.textS
# 文本内容被读取后，存为字符串，针对字符串的操作都可以用在上面，如全部转化为大写、去除开头空格等
content = path.read_text()
lines =content.splitlines()  # splitlines作用把字符串根据换行符拆分成列表，对表示文件的字符串很有用
"""文件内容被读取为字符串后，换行符在字符串里用\n表示，根据\n进行拆分，列表里每个元素是单独一行的内容，
就可以结合for 循环对每行依次进行后续操作"""
for line in lines:
    print(line + "!")






