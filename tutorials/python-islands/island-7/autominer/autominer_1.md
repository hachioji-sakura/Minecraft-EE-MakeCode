### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# オートマイナー（Autominer）

```customts
const CAVE_LAVA = 11

agent.teleport(world(-440, 145, 669), SOUTH)
```

## はじめに @showdialog

この演習では、下のフローチャートに従う Python プログラムを作成します。

エージェントに、作業用の採掘坑道（mineshaft）を作らせましょう。以下のフローチャートに従って、次のようなエージェント用の Python プログラムを作成します。

- エージェントの前方に高さ 2 ブロックのトンネルを掘る  
- 自分の真下に溶岩があるかチェックし、あれば  
- 足元にブロックを置く

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Flowchart.png)

## パート 1
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/flowchart-landscape_1.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

```python
```
エージェントに丸石（STONE）を 64 個渡してください。

## パート 2
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/flowchart-landscape_2.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

```
```
0 から 19 まで繰り返す for ループを作成してください。

## パート 3
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/flowchart-landscape_3.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

```
```
ループの中で、エージェントの前のブロックを壊し、エージェントを 1 ブロック前に移動し、その後エージェントの上のブロックを壊してください。


## パート 4
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/flowchart-landscape_4.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

**注意：採掘中に見つかる溶岩を検知するために `CAVE_LAVA` を使ってください。**

```
```
エージェントの下のブロックが `CAVE_LAVA` なら、エージェントの足元に丸石ブロックを置いてください。


```ghost
agent.set_item(STONE, 64, 1)
agent.set_slot(1)

for i in range(19):
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(UP)

    block = agent.inspect_block(DOWN)

    if block == CAVE_LAVA:
        agent.place(DOWN)
```

```ghost
block = agent.inspect_block(DOWN)
```
