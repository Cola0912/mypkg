# SPDX-FileCopyrightText: 2022/11 Shusei Aida 0912cocacola@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msg.srv import Query


def cb(request, response):          #17行目で定期実行されるコールバック関数
	if request.name == "akiya shusei":
		response.age = 20
	else:
		response.age = 255

	return response

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)            #実行（無限ループ）