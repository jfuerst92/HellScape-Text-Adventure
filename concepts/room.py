#!/usr/bin/env python

import item

'''
Very rough draft of room object. Getting
thoughts down.
'''

class Room(object):
  def __init__(self,desc,conn, invItem, intItem):
      self.desc = desc
      self.conn = conn
      self.invItem = invItem
      self.intItem = intItem
