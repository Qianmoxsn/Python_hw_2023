'''
Description:

句子反转：
给定一个句子（只包含字母和空格），将句子中的单词位置反转，单词用空格分割, 单词之间只有一个空格，句子前后没有空格。
比如：“hello xiao ming”-> “ming xiao hello”

输入描述：可以输入多组数据。每组包含一个句子。
输出描述：最后统一输出每组句子单词反转后形成的句子。  
'''

str = input(">>>")

if __name__ == "__main__":
    # answer here
    ls = str.split(" ")
    ls_reverse = ls
    ls_reverse.reverse()

    str_reverse = ""
    
    for item in ls_reverse:
        str_reverse += item
        str_reverse += " "
        
    print(str_reverse)
