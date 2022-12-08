# SPDX-FileCopyrightText: 2022/11 Shusei Aida 0912cocacola@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

def cb(self):
    msg = Int16()
    msg.data = self.n
    self.pub.publish(msg)
    self.n += 1

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
talker = Talker(node)
rclpy.spin(node)            #実行（無限ループ）