import time
import random
from gmssl import sm3, func

def my_sm3(m):
    #input number
    m = hex(m)[2:]
    m = bytes(m, encoding="utf8")
    m = sm3.sm3_hash(func.bytes_to_list(m))
    return m

def birthday_attck(n):
    for i in range(2**n):
        b=random.randint(0,2**n)
        original_b=b
        my_sm3(b)
        c=random.randint(0,2**n)
        original_c=c
        my_sm3(c)
        if b ==c:
            print(original_b,original_c)
            print("找到碰撞")
            print("查找了{0}次".format(i))
            return
    print("失败")



if __name__=="__main__":
    start=time.time()
    birthday_attck(512)
    end=time.time()
    print("运行时间为:{0}".format(end-start))
