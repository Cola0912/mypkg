# ROS2_listener_&_talker
![test](https://github.com/Cola0912/mypkg/actions/workflows/test.yml/badge.svg)

2022年のロボットシステム学の講義内で製作したプログラム
提出用


### 動作確認のための準備
ROS2のインストールがまだの人は以下のURLの手順に従いインストールしてください。

https://docs.ros.org/

インストール後、本レポジトリを任意のワークスペースにクローンしてください。
```bash
  git clone https://github.com/Cola0912/mypkg.git
  colcon build
```
### 開発環境
* Ubuntu20.04
* ROS2 Foxy
* Python


# listenerコマンド
標準入力から読み込んだ数字を足すことができるコマンド。

# talkerコマンド
標準入力から読み込んだ数字を足すことができるコマンド。


## テスト環境
* Ubuntu22.04
* ROS2 Humble

またこれらのテストには[上田 隆一先生のコンテナ](https://hub.docker.com/layers/ryuichiueda/ubuntu22.04-ros2/latest/images/sha256-0e1773bc6f12b57172c8818aac36aeb97ca13269028028d49ad5f6f8cc0d6204?context=explore)を使用しています。

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。

©︎ 2022 Shusei Aida
