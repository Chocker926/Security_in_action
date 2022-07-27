import time
import random
from gmssl import sm3, func

def birthday_attck(n):
    for i in range(2**n):
        b=random.randint(0,2**n)
        b=hex(b)[2:]
        original_b=b
        b=bytes(b, encoding = "utf8")
        b=sm3.sm3_hash(func.bytes_to_list(b))
        c=random.randint(0, 2 ** n)
        c = hex(c)[2:]
        original_c = c
        c=bytes(c, encoding = "utf8")
        c = sm3.sm3_hash(func.bytes_to_list(c))
        if b ==c:
            print(original_b,original_c)
            print("找到碰撞")
            print("查找了{0}次".format(i))
            return
    print("失败")



if __name__=="__main__":
    # print(hash(m))
    time1=time.time()
    birthday_attck(512)
    time2=time.time()
    timesum=time2-time1
    print("运行时间为：{0}".format(timesum))
