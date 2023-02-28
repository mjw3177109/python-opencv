"""

描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足


1≤n≤10000  ，坐标保证满足

≤
2
31
−
1

−2
31
 ≤x,y≤2
31
 −1  ，且数字部分仅含正数
输入描述：
一行字符串

输出描述：
最终坐标，以逗号分隔

示例1
输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
复制
输出：
10,-10
复制
示例2
输入：
ABC;AKL;DA1;
复制
输出：
0,0

"""

import sys


initial_location=[0,0]
for line in sys.stdin:
    a = line.split()
    if a ==[]:
        break
    data=a[0]
    for m in data.split(";"):
        if not 2<=len(m)<=3:
            continue
        direction =m[0]
        try:
            step =int(m[1:])
        except Exception as e:
            continue
        if direction in ["A","D","W","S"]:
            if 0<=step<=99:
                if direction == 'A':
                    initial_location[0] -=step
                elif direction == "D":
                    initial_location[0] +=step
                elif direction == 'S':
                    initial_location[1] -=step
                elif direction == "W":
                    initial_location[1] +=step

    print(str(initial_location[0])+","+str(initial_location[1]))

