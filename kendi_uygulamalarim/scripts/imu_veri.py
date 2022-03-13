#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from kendi_uygulamalarim.msg import ImuVeri

# IMU calisma mantigi soyle:
# -1, 1 araliginda donus acisina bagli olarak artiyor ve azaliyor. Mutlak degerlerinin farkini aldigimizda 180 derece icin 1 deger fark ediyor.
# en basta kuzeye dogru 0, dogu 0.7, guney 0.95-0.99, bati 0.7 oluyor. İste buna gore hangi yolu secmesi gerektigine kadar verilecektir. (Bu degerler mutlak deger ile)
# bu durumda gelen konum ile ilgili bir yorum uretelim:
# eger x ve y buyuk ise demek ki gidilecek yer kuzey doguda demektir. yani yukarı ve sagda. bu durumda 0-0.7 arasinda bir yol aramamiz gerekir.
# ya da x kucuk y buyuk olsun o zaman kuzey batida olur ve yine 0-0.7 arasi olur burasi sıkıntılı mesela. burada her zaman sola dogru dondugumuzden ona gore bir algoritma gelistirilebilir
# mesela ikisi de kucuk olsun o zaman 0.99-0.7 arasi olacaktir. ama dedigim gibi donme yonune bagli olarak bir algoritma gelistirilmelidir yoksa sag ve sol karisir.



class ImuData():
   def __init__(self):
      rospy.init_node("imu_veri")
      self.rate = rospy.Rate(5)

      rospy.Subscriber("/imu", Imu, self.imuCallback)

      self.pub = rospy.Publisher("imu_veri", ImuVeri, queue_size=10)
      self.imu_mesaji = ImuVeri()
      rospy.spin()

   def imuCallback(self, mesaj):
      imu = abs(mesaj.orientation.z)

      self.imu_mesaji.yon = imu
      self.pub.publish(self.imu_mesaji)
      print("Imu verisi yayinlaniyor...")
      self.rate.sleep()



imu = ImuData()

