### @flyoutOnly true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0
### @explicitHints true

# 動物の囲い（Animal Pen）

## はじめに @showdialog

この演習では、下のフローチャートに従う Python プログラムを作成します。

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart.png)

## 動物をスポーンさせる - 1
   
![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart-landscape_1.png)
まず、フローチャートの黒い部分に対応するコードを書き、自分の位置に牛をスポーンさせましょう。必要ならヒントを使ってください。  
終わったら次のパートに進みます。

### ~ tutorialhint
次の例は、プレイヤーの位置に牛をスポーンさせるコードです。
```python
mobs.spawn(COW, player.position())
```


## 動物をスポーンさせる - 2

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart-landscape_2.png)
次に、黒で示されたフローチャートの部分に対応するコードを書きます。必要ならヒントを使ってください。  
   
### ~ tutorialhint
次の例は、プレイヤーの位置に牛をスポーンさせるコードです。  
ここでは牛だけでなく、ブタとヒツジもスポーンさせる必要があります。
```python
mobs.spawn(COW, player.position())
```


## 発展課題（Extension）@showdialog

Animal Spawner（動物スポーナー）に追加できるアイデアの例です：

- ワールド座標（`pos` ではなく `world`）を使って、ランダムな動物の組み合わせを囲いの中にスポーンさせる。
- 各場所で複数の動物をスポーンさせるために、`||loops:for||` ループを使ってみる。
- フェンスで囲いを作り、動物が出ていかないようにしてみる。

```ghost
import random

blocks.place(OAK_FENCE, player.position())

pos = positions.add(pos(0, 0, 0), pos(0, 0, 0))

pos_2 = world(0, 0, 0)
pos_3 = pos(0, 0, 0)


for i in range(3):
    rand_num = random.randint(1, 10)
    for i in range(rand_num):
        mobs.spawn(COW, player.position())
        
```
