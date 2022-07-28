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
    dict={}
    for i in range(2**256):
        b=random.randint(0,2**(16*n))
        original_b=bytes(hex(b)[2:], encoding="utf8")
        b=my_sm3(b)
        dict[b[:n]]=original_b
        c=random.randint(0,2**(16*n))
        original_c = bytes(hex(c)[2:], encoding="utf8")
        c=my_sm3(c)
        if c[:n] in dict.keys():
            if dict[c[:n]] == original_c:
                break
            print("找到碰撞")
            print(dict[c[:n]])
            print(original_c)
            print("查找了{0}次".format(i))
            return
        else:
            dict[c[:n]]=original_c
    print("失败")



if __name__=="__main__":
    start = time.time()
    birthday_attck(4)
    end = time.time()
    print("运行时间为:{0}".format(end - start))
    start=time.time()
    birthday_attck(8)
    end = time.time()
    print("运行时间为:{0}".format(end - start))
    start = time.time()
    birthday_attck(16)
    end = time.time()
    print("运行时间为:{0}".format(end - start))
