import threading

# def hello():
#     print("hello world")
    
    
# t1 = threading.Thread(target=hello)
# t1.start()

# def function1():
#     for i in range(1000):
#         print("ONE")
        
# def function2():
#     for i in range(1000):
#         print("TWO")
        
# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)
# t1.run()
# t2.run()


def function3():
    for i in range(10000):
        print("************")
        
t3 = threading.Thread(target=function3)
t3.start()
t3.join(2)
print("THE END OF Program")