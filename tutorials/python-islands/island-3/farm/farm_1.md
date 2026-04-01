### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 農場

```ghost
agent.place(DOWN)
agent.destroy(FORWARD)
agent.move(FORWARD, 1)
const block = agent.inspect(AgentInspection.Block, DOWN)
if (block == WHEAT) {
    player.say("Wheat!")
}
```



## 自動農作業と作物の収穫 @showdialog

``||loops:for||`` ループが使えるようになったので、エージェントに農地の収穫と再植えを自動でやらせて腕試ししましょう！

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/farm/cover.png)

## ステップ 1

ピーターが、植え付けに必要な種の正確な数をエージェントに渡してくれました。

まず、最初の作物を調べる前にエージェントを前に進める必要があります。

**エージェントを 1 ブロック前に進めてください！**

```spy
agent.move(FORWARD, 1)
```

## ステップ 2

次に、エージェントに下(DOWN)のブロックを調べさせ、変数に格納します。

**`block` という新しい変数を追加し、エージェントが調べたブロックを代入してください。**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
```

## ステップ 3

ブロック名が変数に格納できました。``||logic:if||`` 文で、エージェントの下のブロックに応じて処理を分けられます。

**ブロックが `WHEAT` かどうかをチェックする ``||logic:if||`` 文を追加してください。**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    player.say("Wheat!")
}
```

## ステップ 4

小麦のときのチェックができたので、``||agent:agent.destroy()||`` に方向を指定して小麦を収穫し、``||agent:agent.place()||`` で種を置く方向を指定して植え替えましょう。

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    agent.destroy(DOWN)
    agent.place(DOWN)
    player.say("Wheat!")
}
```

## ステップ 5

``||logic:if||`` 文ができたので、``||logic:elif||`` 文を作りましょう！

**ブロックが `AIR` のときに ``||agent:agent.place()||`` で種を植える ``||logic:elif||`` 文を追加してください。**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    agent.destroy(DOWN)
    agent.place(DOWN)
    player.say("Wheat!")
}else if (block == AIR) {
    agent.place(DOWN)
    player.say("Air!")
}
```

## ステップ 6

ここまでできたら、for ループで全体を何度も繰り返し、``||agent:agent.move()||`` で毎回エージェントを前に進めるようにしましょう。

**既にあるコードを `0` から `8` の範囲で繰り返す ``||loops: for||`` ループを作成してください。また、``||agent:agent.move()||`` でエージェントを `FORWARD`（前）に移動させることも忘れずに。**

## 収穫を始めよう！

コードが揃ったら実行し、**ホイッスルでエージェントをダイヤモンドブロックのところに呼び戻して**ください。農作業を楽しんで！
