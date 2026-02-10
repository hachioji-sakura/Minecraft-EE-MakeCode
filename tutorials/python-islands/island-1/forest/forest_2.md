### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - 森 2

```template
agent
```

## リンゴを摘む @showdialog
調査の結果、ニコルがマーヴィンという鳥と一緒に木のてっぺんに閉じ込められていることがわかりました。マーヴィンはお腹を空かせているため、木のてっぺんに巣を作っているようです。リンゴを取りに行きましょう！
![Cover Image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/cover2.png)
はしごを降りてエージェントを見つけ、準備ができたら最初のリンゴを摘みに行きましょう！

## リンゴまで移動する
リンゴを摘むには、まずエージェントをリンゴの1つの隣に配置する必要があります。エージェントは上（UP）、下（DOWN）、左（LEFT）、右（RIGHT）、前（FORWARD）、後（BACK）に移動できることを覚えておいてください。
`||agent:agent.move||`（とホイッスル）を使ってエージェントを移動させ、最初に摘みたいリンゴまで移動しましょう！


```python
agent.move(DIRECTION, BLOCKS)
```


## リンゴを拾う @showdialog
エージェントがリンゴの隣にいることを確認してください。（下の画像と同様の位置）
![Agent position before picking apple](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/agent_before_pick.png)

## リンゴを拾う
エージェントがリンゴの前にいる状態で、`||agent:agent.destroy||`コマンドを使って特定の方向のブロックを壊すことができます。
```python

agent.destroy(DIRECTION)

```
- `DIRECTION`とは、エージェントが壊そうとする方向のことです。

使用できる方向は：前（FORWARD）、後ろ（BACK）、左（LEFT）、右（RIGHT）、上（UP）、下（DOWN）です。


## 残りを取得する
素晴らしい！最初のリンゴを取得しましたが、あと4つ必要です。
周りを探して、あと4つ摘んでから、終わったらニコルのところに戻りましょう。
