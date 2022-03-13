#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from kendi_uygulamalarim.msg import KonumVeri

# konum bilgisi bu şekilde kolayca alınabilir en azından simualasyon ortamında :)

class Konum():
   def __init__(self):
      rospy.init_node("konum_veri")
      self.rate = rospy.Rate(5)

      rospy.Subscriber("/odom", Odometry, self.konumCallback)

      self.pub = rospy.Publisher("konum_veri", KonumVeri, queue_size=10)
      self.konum_mesaji = KonumVeri()

      rospy.spin()

   def konumCallback(self, mesaj):
      self.konum_mesaji.konumX = mesaj.pose.pose.position.x
      self.konum_mesaji.konumY = mesaj.pose.pose.position.y

      self.pub.publish(self.konum_mesaji)
      print("Konum verisi paylasiliyor...")
      self.rate.sleep()

konum = Konum()