'''

Input: N, M
生成一个有 N (1<N≤100) 个元素的列表，
每个元素是一个随机数 n (1≤n≤2^31 −1),
从这个列表中随机取出 M (1<M≤N) 个数，
对这 M 个数字进行排序，显示
Output: 排序后的这 M 个数字 
'''
import random

n_int = int(input("n_"))
m_int = int(input("m_"))

if __name__ == "__main__":
    ls = []
    for i in range(n_int):
        rd_int = random.randint(1, 2 ^ 31 - 1)
        ls.append(rd_int)
    # print(ls)
    ls_m = random.sample(ls, m_int)
    # print(ls_m)
    ls_m_arr = sorted(ls_m)
    print(ls_m_arr)