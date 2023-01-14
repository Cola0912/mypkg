# ROS2_listener_&_talker
![test](https://github.com/Cola0912/mypkg/actions/workflows/test.yml/badge.svg)

2022年のロボットシステム学の講義内で製作したプログラム
提出用

## 内容
tallkerとlistenerの通信する様子を観察しROSについての理解を深めることが本レポジトリの本意。


### 動作確認のための準備
ROS2のインストールがまだの人は以下のURLの手順に従いインストールしてください。

https://docs.ros.org/

インストール後、ワークスペースを作成し本レポジトリをクローンしてください
以下のコマンドを実行することで準備が整います。
```bash
  mkdir -p ros2_ws/src
  cd ros2_ws/src
  git clone https://github.com/Cola0912/mypkg.git
  cd ~/ros2_ws
  colcon build
  source ~/.bashrc
```
### 開発環境
* Ubuntu20.04
* ROS2 Foxy
* Python 3.8.10

# ノード

## listener
countupを受け取った後、表示する。
[](countupがない場合、待機。)

```bash
  ros2 run mypkg listener
```
すでにtalkerが動いていたときの実行結果
```bash
  [INFO] [1672490453.017639528] [listener]: Listen: 0
  [INFO] [1672490456.000637224] [listener]: Listen: 1
  [INFO] [1672490459.000537012] [listener]: Listen: 2
  ...
```

## talker
実行されてから0.5秒おきに変数に１を足しメッセージを流す。

```bash
  ros2 run mypkg talker
```

## トピック
### countup
talkerからlistenerに対して0.5秒おきにメッセージを送るための流路。
![industrial_ci](https://github.com/Cola0912/mypkg/blob/master/rosgraph.svg)

# テスト環境
* Ubuntu22.04
* ROS2 Humble

またこれらのテストには[上田 隆一先生のコンテナ](https://hub.docker.com/layers/ryuichiueda/ubuntu22.04-ros2/latest/images/sha256-0e1773bc6f12b57172c8818aac36aeb97ca13269028028d49ad5f6f8cc0d6204?context=explore)を使用しています。

# ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、教育目的で本人の許可を得て自身の著作としています。

[ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

©︎ 2022 Shusei Aida
