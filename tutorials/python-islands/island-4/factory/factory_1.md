### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 工場
飛行船を修理する


## 船体を修理する @showdialog

![Airship Factory](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/factory/cover.jpg)

飛行船工場のクルーが、新しい飛行船の修理を手伝ってほしいようです。エージェントを送って穴を塞いでください！


始める前に、このウィンドウを閉じてエージェントを探してください。飛行船の中にいるはずです。

## ステップ 1
エージェントを見つけたら、修理する最初の穴の上に浮かぶように 1 ブロック前に移動させましょう。

**エージェントを前に移動させるコードを書いてください。**

```python
agent.move(FORWARD, 1)
```

## ステップ 2
エージェントが配置できたので、ドックの底まで下げて、落ちたブロックを回収する必要があります。

そのために、エージェントの下が空気の間だけ下に移動する while ループを使います。

**`||loops:while||` ループと DOWN 方向の ``||agent:agent.inspect||`` を使って、ブロックが `AIR` でなくなるまでエージェントを下に移動させるようにコードを変更してください。**

```python
while agent.inspect(AgentInspection.BLOCK, DOWN) == AIR:
    agent.move(DOWN, 1)
```


## ステップ 3
エージェントがドックの底にいるので、壊れて落ちたブロックを回収できます。飛行船の下の見学廊下からブロックの位置を確認できます。
ブロックを回収するには `||agent:agent.collect_all()||` 関数を使います。

**エージェントの近くのアイテムをすべて回収するようにコードを変更してください。**

```python
agent.collect_all()
```


## エージェントの位置を取得する @showdialog
修理用のブロックを持ったエージェントを、ブロックを置き直す正しい位置まで戻す必要があります。
工場の作業員から、修理する y 座標は `157` だと聞きました。
エージェントの座標を取得するには：
```python
agent.get_position()
```
この位置から y 座標を取得するには：
```python
agent.get_position().get_value(Axis.Y)
```

## ステップ 4
`||loops:while||` ループと ``||agent:agent.get_position()||``、``||positions:.get_value(AXIS.Y)||`` を使って、エージェントの y 座標が `157` になるまで ``||agent:agent.move(UP)||`` を繰り返してください。


```python
while agent.get_position().get_value(Axis.Y) != 157:
    agent.move(UP, 1)
```

## ブロックを置く @showdialog
エージェントが正しい y（高度）座標に来たので、`||agent:agent.set_slot||` と `||agent:agent.place||` で、今回収したブロックを置けます。

これらの関数の使い方のおさらいです…

```python
agent.set_slot(SLOT_NUMBER)
agent.place(DIRECTION)
```

- `SLOT_NUMBER`: エージェントが選択するスロット（ブロックを置く元）。

- `DIRECTION`: エージェントがブロックを置く方向。使える方向は FORWARD、BACK、LEFT、RIGHT、UP、DOWN です。

## ステップ 5
`||agent:agent.set_slot||` と `||agent:agent.place||` を使って、スロット番号 `1` のブロックを `DOWN`（下）方向に置いてください。


```python
agent.set_slot(1)
agent.place(DOWN)
```
