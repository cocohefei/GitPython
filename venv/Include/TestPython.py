import time,datetime

class timeTest:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.timetime = float(time.time()).__str__()
        self.time_locatime = time.localtime(time.time())
        #self.time_strf = time.strftime('%Y-%m-%d %H:%M:%S',time_locatime)
        self.time_datatime = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def timeF(self):
        print(self.odometer)

    def timeE(self):
        print(self.time_locatime)

    def timeG(self):
        print(self.time_datatime)

    def timeT(self):
        print(self.timetime)

if __name__ == '__main__':

   my_time  = timeTest()
   print("I'm a TimeTest!")

   my_time.timeF()
   time.sleep(2)
   my_time.timeE()
   time.sleep(2)
   my_time.timeG()
   time.sleep(2)
   my_time.timeT()

   for i in range(1,5):
       print(i)
   else:
       print("OK")
#========================================================#
   #print(my_time.time_strf)
   #time.sleep(2)
   #print(my_time.time_datatime)
   #time.sleep(2)
   #print(my_time.speed)

#---------------------------------------------------------#
#t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#print(t)
# 暂停一秒
#time.sleep(1)
#t1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#print(t1)
#t2 = time.localtime(time.time())
#print(t2)
#t3 = time.time()
#print(t3)

# time.sleep(1)
# TIME = datetime.datetime.now()
# print(TIME.strftime("%Y.%m.%d %H:%M:%S"))