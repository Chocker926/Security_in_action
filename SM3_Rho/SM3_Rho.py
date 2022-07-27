import time
import random
from gmssl import sm3, func
def my_sm3(m):
    #input number
    original_m = m
    m = hex(m)[2:]
    m = bytes(m, encoding="utf8")
    m = sm3.sm3_hash(func.bytes_to_list(m))
    return m


def rho_method(n):
    m = random.randint(0, 0xffffff)
    res = []
    for i in range(2**(n-1)):
        original_m = m
        m = my_sm3(m)
        res.append(m)
        m = (2 * original_m + 1)
        if my_sm3(m) in res:
            print("找到碰撞")
            print(my_sm3(m))
            print("查找了{0}次".format(i))
            return
    print("失败")

if __name__=="__main__":
    # print(hash(m))
    start=time.time()
    rho_method(512)
    end=time.time()
    print("运行时间为:{0}".format(end-start))
