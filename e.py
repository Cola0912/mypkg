# SPDX-FileCopyrightText: 2022 Yuki Kumazawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():
    def __init__(self,node):

        self.pub = node.create_publisher(Int16, "countup", 10)  #オブジェクト
        self.n = 0
        node.create_timer(0.5,self.cb)

    def cb(self):       #関数を抜けてもnがリセットされないようにしている
        msg = Int16()  #メッセージの「オブジェクト」 #msg.name = "熊澤佑紀"   #msgオブジェクトの持つdataにnを結び付け
        msg.data = self.n
        self.pub.publish(msg)        #pubの持つpublishでメッセージ送信
        self.n += 1

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
talker = Talker(node)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）