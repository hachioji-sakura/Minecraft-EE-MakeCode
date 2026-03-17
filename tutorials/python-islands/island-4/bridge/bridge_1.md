### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

```customts
agent.teleport(world(935,150,627), WEST)
```

# 橋
```template

while(== AIR) {
    agent.move()
}

player.say("I've reached the end")
```

## `while` ループの基本 @showdialog

アイランド 3 では `||loops:for||` ループを紹介しました。この島では、もう一つのループである `||loops:while||` ループを使いこなします。何回繰り返すかわからないときに使います。



`||loops:while||` ループの例です。

```python

while condition_1 == condition_2:

    player.say("Condition_1 is equal to condition_2")

```

上のコードは、条件が満たされている**限り**実行されます。``||logic:if||`` 文と同様に、``||loops:while||`` ループでも条件を使います。ループを止めるかどうかを、この条件で判断します。

## 距離に橋をかける @showdialog

![Bridging the gap](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/bridge/blind.jpg)


**鉱山マネージャー** - 「*君とエージェントで霧の中に橋を架けて、向こうに何があるか調べてくれないか？*」

まず、エージェントに while ループを実行させ、別の陸地（島）に着いたかどうかを確認する必要があります。
そのために、エージェントの前のブロックが `AIR` かどうかをチェックし、そうなら（`||loops:while||` ループの中で）前に進むようにできます。
別の陸地に着くと、前のブロックはもう `AIR` ではなくなるので、ループを止められます。

## ステップ 1
`||loops:while||` ループの条件に ``||agent:agent.inspect||`` を使います。

`FORWARD` 方向のブロックが空気かどうかをエージェントがチェックするように、``||loops:while||`` ループに ``||agent:agent.inspect||`` を追加して完成させてください。

```python-ignore
while (agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR):
    agent.move()
```

## ステップ 2

次に、毎回エージェントを前に進める必要があります。``||agent:agent.move||`` の行を、1 回に 1 ブロック `FORWARD`（前）に進むように更新してください。

```python
while (agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR):
    agent.move(FORWARD 1)
```


## 距離に橋をかける @showdialog

![Bridging the gap](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/bridge/blind.jpg)

**鉱山マネージャー** - 「*島まで橋を架けるために、エージェントに**石**（スロット 1）を渡した。エージェントの下に石ブロックを置いて、向こうの島に着いて前が空気でなくなるまで橋を作ってくれないか？*」


## ステップ 3
ループが動いている間、エージェントを動かせるようになったので、向こうの島までブロックを置いて橋を架けます。

そのために `||agent:agent.set_slot||` と `||agent:agent.place||` でブロックを置けます。

完成したコードを実行するために、ホイッスルでエージェントを呼び戻せることを忘れないでください。

**エージェントに石ブロック（スロット 1）を自分の `DOWN`（下）に置かせてください。そして向こうの島を調査しましょう！**


```python
agent.set_slot(slot_id)
agent.place(DIRECTION)
```

- `slot_id`: 選択するエージェントのインベントリのスロット番号（そこからブロックを置く）。

- `DIRECTION`: エージェントがブロックを置く方向。使える方向は FORWARD、BACK、LEFT、RIGHT、UP、DOWN です。
