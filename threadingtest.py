#!/usr/bin/python
# coding: utf-8
import threading
import time

'''
hhhhhhhh
'''

class MyThread(threading.Thread):
    def run(self):
        for i in range(0,5):
            #print i
            #print self.name
            msg = '线程' + self.name + str(i)
            print msg
	    print threading.activeCount()


# 单线程 注意 若调用start,则先执行主线程的，后执行子线程的 若调用run()方法，则相当于函数调用，按照程序的顺序执行
if __name__ == '__main__':
    t = MyThread()
    t.run()



