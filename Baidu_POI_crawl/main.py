import os
import os.path as osp
from util import get_baidu_poi
import argparse


def run(args):  #准备执行数据抓取的前置工作
    baidu_web_ak = args.ak
    city_str = args.city
    roi_key = args.poi
    output = args.save  #从传入的args对象中提取四个参数：百度API的AK密钥、城市名、POI关键词、保存路径
    if not osp.exists(output):  #检查输入目录，如果用户指定的保存文件夹路径不存在，则自动递归创建该文件夹
        os.makedirs(output)
    get_baidu_poi(roi_key, city_str, baidu_web_ak, output)
    print("current area completed")


parser = argparse.ArgumentParser(description="input parameters")
parser.add_argument("--ak", type=str, required=True, help="Baidu web ak")
parser.add_argument("--city", type=str, required=True, help="City name")
parser.add_argument("--poi", type=str, required=True, help="POI key")
parser.add_argument("--save", type=str, default="output", help="Save path")



if __name__ == "__main__":      #脚本运行时的起点
    args = parser.parse_args()  #调用parse_arge()获取用户在命令行输入的参数
    run(args)  #将其传递给run(arges)函数，正式启动流程