# 为SDNU集训队处理比赛统计事宜

由vjudgeChecker更名为OJchecker

## 使用方法

1. 安装python3

2. 安装openpyxl

3. 将用户数据放入config(第一行不用于放置信息, 第一列放置姓名，第二列放置oj用户名

    vjudge数据保存为vjudge.xlsx
    
    牛客数据保存为newcoder.xlsx

4. 使用

```bash
#查询vjudge
python vjc.py
#查询牛客
python ncc.py
```

5. 根据提示进行参数输入

将会在根目录保存统计数据

## 统计项说明

1.出题数 --- 比赛中做出题目

2.罚时 --- ac一题罚时加上当前时间，ac题目的错误提交一次加二十分钟罚时

3.补题数 --- 队员后期补题数量

4.题目提交数 --- 为每题提交次数， 显示为 总提交次数 / 是否AC

5.未参加为红色，补完题为绿色

## 后续更新(gugugu

1.加入查重机制

2.优化统计项

3.扩展统计OJ范围

4.使用go语言重写