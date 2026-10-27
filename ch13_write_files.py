# pathlib 专门用处理【文件/文件夹】的工具包，面向对象的路径库
# from pathlib import Path
# path = Path("./data.txt")
# path.write_text("Hello\nYoooo")  表示写文件，要写的内容通过字符串传入，要写多行的话就\n换行符进行换行
# read_text：如果根据这个文件路径找不到文件时就会报错
# write_text：不存在上述问题，如果文件不存在，程序就会自动创建；
# 需要注意文件已经存在且里面有内容的话，就会先把原本的文件内容清空，再写入传入的内容，所以要三思而后行！




from pathlib import Path

names = ""
user_input = input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")
while user_input != "q":
    names += user_input + "\n"
    user_input = input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")
path = Path("./guest_book.txt")
path.write_text(names)
