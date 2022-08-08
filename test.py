#
#输出一个字符串,为二叉树中序遍历各节点值的拼接结果
#
#题目描述
# 根据给定的二叉树结构描述字符串，输出该二叉树按照中序遍历结果字符串。中序遍历顺序为:左子树，根结点，右子树。
#
# 输入描述
# 由大小写字母、左右大括号、逗号组成的字符串:
# 1、字母代表一个节点值，左右括号内包含该节点的子节点。
# 2、左右子节点使用逗号分隔，逗号前为空则表示左子节点为空,没有逗号则表示右子节点
# 为空。
# 3、二叉树节点数最大不超过100。
# 注:输入字符串格式是正确的，无需考虑格式错误的情况。
#
# 输出描述
# 输出一个字符串，为二叉树中序遍历各节点值的拼接结果。
#
# 示例：
# 输入：a{b{d, e{g,h{,I}}},c{f}｝
# 输出：dbgehiafc

#
#
#
# 输出一个字符串,为二叉树中序遍历各节点值的拼接结果。 示例: 输入:a{b{d, e{g,h{,I}}},c{f}} 输出:dbgehiafc

#给定一个字符串s，并且s头尾相连。s中含有若干个字符‘o’，现求s所有子串中，含偶数个字符‘o’的最大长度。

####
##主管期望你来实现英文输入法单词联想功能
# 需求如下
# 依据用户输入的单词前缀
# 从已输入的英文语句中联想出用户想输入的单词
# 按字典序输出联想到的单词序列
# 如果联想不到
# 请输出用户输入的单词前缀
# 注意
# 英文单词联想时区分大小写
#缩略形式如
#"don't" 判定为两个单词 "don"和 "t"
#输出的单词序列不能有重复单词
#且只能是英文单词，不能有标点符号

#输入描述
#输入两行
#首行输入一段由英文单词word和标点构成的语句str

#接下来一行为一个英文单词前缀pre
#0 < word.length() <= 20
#0 < str.length <= 10000
#0 < pre <=20

#输出描述
#输出符合要求的单词序列或单词前缀
#存在多个时，单词之间以单个空格分割

#示例一
#输入
#I love you
#He

#输出
#He

#说明
#用户已输入单词语句"I love you",
#中提炼出"I","love","you"三个单词
#接下来用户输入"He" ，
#从已经输入信息中无法联想到符合要求的单词
#所以输出用户输入的单词前缀

#示例二
#输入
#The furthest distance in the world,Is not between life and death,But when I stand in front or you,Yet you don't know that I love you.
#f

#输出
#front furthest

##
##
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(line)
#     # print(int(a[0]) + int(a[1]))

#
# import sys
#
# filter_word = [",", ".", "*", "&", "%", "#", "!", "@", "'",]
# word_bags = []
# index = 0
# # result_str = ""
# for line in sys.stdin:
#
#     result_str = ""
#     first_word = (line.strip())
#     for m in filter_word:
#         if m in first_word:
#             first_word.replace(m, "")
#
#     signle_word = first_word.split(" ")
#     newsignle_word =[]
#     for h in signle_word:
#         new_h =h.strip()
#         if "'t" in new_h:
#             newsignle_word.append(new_h.split("'")[0])
#             newsignle_word.append("not")
#         else:
#             new_word =new_h.replace(",", " ").replace("."," ")
#             newsignle_word.append(new_word)
#         result_str += new_h
#     if len(signle_word) >= 1:
#         index += 1
#         result_str=""
#         for j in signle_word:
#             j=j.strip()
#
#             for k in word_bags:
#                 if j[0] in k and j[0]==k[0]:
#                     result_str += k + " "
#             word_bags.append(j)
#     if index >= 2:
#         print(result_str)


# import sys
# import re
# for line in sys.stdin:
#     words=line.strip()
#     o_numbers=re.findall("o",words)
#     # if len(o_numbers)%2==0:
#     #     print(len(new_word))
#     # else:
#     number =words[-0::].index("o")
#     print(number)
        # if number ==0:
        #     number =-1
        # else:
        #     number =-number
        # new_word =words[:number]
        # print(len(new_word))

import sys
import re
for line in sys.stdin:
    finall_number=0
    result_left = ""
    result_right = ""
    new_words = line.strip()
    result_mid = new_words[0]
    copy_words =new_words
    res_number =0
    # new_words = new_words[1:]
    # number_list=re.findall("{",new_words)
    while True:
        if "," in copy_words:
            finall_number =copy_words.index(",")
            res_number+=finall_number
            copy_words=copy_words[finall_number+1:]
        else:
            break



    left_part =new_words[1:res_number]
    right_part =new_words[res_number+1:]

    for k in left_part:
        if k =="{" or k=="}" or k ==",":
            pass
        else:
            result_left=k+result_left

    for m in right_part:
        if m =="{" or m=="}" or m ==",":
            pass
        else:
            result_right=m+result_right
    print(result_left+result_mid+result_right)





