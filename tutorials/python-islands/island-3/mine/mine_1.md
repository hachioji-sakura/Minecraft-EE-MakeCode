### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 鉱山

## 金を掘る！ @showdialog

最近、島で使える金のブロックがいくつか見つかり、技術を進めるのに役立っています！マイケルが、人が降りるには安全でない場所で、エージェントを使って金鉱石を掘る手伝いをしてほしいと頼んでいます。

![Picture of Mine expert and mine](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/mine/cover.png)

## ステップ 1

マイケルは、金のブロックが地下のどこにあるか見当をつけています。掘る場所がわかるように、鉱夫のチームに地表のブロックを丸石に置き換えてもらいました！

まず、``||agent:agent.move||`` で最初のブロックの上に移動しましょう。

**エージェントを 1 ブロック FORWARD（前）に動かし、丸石の上に乗せてください。**

```python
agent.move(FORWARD, 1)
```

## ステップ 2

さあ、掘り始めましょう！マイケルによると、金は地表から 3 ブロック下にあります。

``||agent:agent.destroy||`` と ``||agent:agent.move||`` で地下に `DOWN`（下）へ掘り進めます。3 回繰り返すために ``||loops:for||`` ループを使います。

**3 回繰り返す ``||loops:for||`` ループを作成し、エージェントに下のブロックを壊してから下に移動させてください。**

```python
for dig in range(0,3):
    agent.destroy(DOWN)
    agent.move(DOWN, 1)
```

## ステップ 3

地表から 3 ブロック下に来たので、金があるか確認します。そのために `if` 文と ``||agent:agent.inspect||`` でブロックの詳細を取得し、``||logic:if||`` でブロック名をチェックします。マイケルから、金でないブロックを壊すと**エージェントが島から落ちる可能性がある**と注意されています！

**エージェントの下のブロックが `GOLD_ORE` かどうかをチェックする ``||logic:if||`` 文を追加してください。金鉱石なら壊してください。**

```python
for dig in range(0,3):
    agent.destroy(DOWN)
    agent.move(DOWN, 1)
block = agent.inspect(AgentInspection.BLOCK, DOWN)
if block == GOLD_ORE:
    agent.destroy(DOWN)
```

## ステップ 4

金を採掘し、石はそのままにしたら、エージェントを坑道を上がって戻しましょう！

**``||agent:agent.move||`` でエージェントを上に `3` ブロック移動させてください。**
```python
for dig in range(0,3):
    agent.destroy(DOWN)
    agent.move(DOWN, 1)
block = agent.inspect(AgentInspection.BLOCK, DOWN)
if block == GOLD_ORE:
    agent.destroy(DOWN)
agent.move(UP, 3)
```

## ステップ 5

コードができたら、最初の坑道を掘ってみましょう。

## ステップ 5

メインのコードが完成したら、全体をまとめて動かしましょう！

コードのほとんどはここにありますが、まだ完成していません…

**既にある坑道チェックのコードを `3` 回実行する ``||loops:for||`` ループをさらに作成し、最後にエージェントを前に移動させてください！**
