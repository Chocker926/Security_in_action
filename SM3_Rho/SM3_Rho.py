import time
import random
from gmssl import sm3, func
def my_sm3(m):
    #input number
    m = hex(m)[2:]
    m = bytes(m, encoding="utf8")
    m = sm3.sm3_hash(func.bytes_to_list(m))
    return m


def rho_method(n):
    m = random.randint(0, 0xffffff)
    dict={}
    for i in range(2**256):
        original_m = m
        temp=bytes(hex(m)[2:], encoding="utf8")
        m = my_sm3(m)
        dict[m[:n]]=original_m
        m = (2 * original_m + 1)
        if my_sm3(m)[:n] in dict.keys():
            print("找到碰撞")
            print(bytes(hex(m)[2:], encoding="utf8"))
            print(bytes(hex(dict[my_sm3(m)[:n]])[2:], encoding="utf8"))
            print("查找了{0}次".format(i))
            return
    print("失败")

if __name__=="__main__":
    start=time.time()
    rho_method(4)
    end=time.time()
    print("运行时间为:{0}".format(end-start))
