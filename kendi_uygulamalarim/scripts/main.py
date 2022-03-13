#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from kendi_uygulamalarim.msg import ImuVeri,KonumVeri

# bu sınıf çok önemli şuanda. bu şekilde callback fonksiyonları dışında gelen verileri kullanabileceğiz...

class GetData():
   def __init__(self):
      rospy.init_node("get_data")
      self.konumX = 0.0
      self.konumY = 0.0
      self.yon = 0.0
      self.rate = rospy.Rate(10)

      rospy.Subscriber("imu_veri", ImuVeri, self.imuCallback)
      rospy.Subscriber("konum_veri", KonumVeri, self.konumCallback)

      while not rospy.is_shutdown():
         print("Yön: " + str(self.yon))
         print("Konum x: " + str(self.konumX) + " | Konum y: " + str(self.konumY))

         self.rate.sleep()

      

   def imuCallback(self, mesaj):
      self.yon = mesaj.yon

   def konumCallback(self, mesaj):
      self.konumX = mesaj.konumX
      self.konumY = mesaj.konumY
      

data = GetData()