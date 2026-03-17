### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - 湖

```template
agent
```

## エージェントの使い方  @showdialog

このタスクでは、エージェントを動かす方法を学びましょう！

![Image of Agent on a starting diamond block with their target in shot](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/lake/lake.jpg)

## Pythonプログラムの復習

Pythonプログラムは、1つ以上の命令で構成されており、コンピューターがそれらを順番に実行します。

## あなたのエージェント

ワールドを見回してみてください。青いダイヤモンドブロックの上に立っているエージェントが見えるはずです。

この素晴らしい小さなロボットは、ワールド内を移動でき、さらには飛ぶこともできます！

次のステップに進んで、エージェントに移動するよう指示を始めましょう。

## エージェントを動かす

`||agent:agent.move(DIRECTION, DISTANCE)||`でエージェントを動かします

**`DIRECTION`に入れる値を*FORWARD*（前）に変更してみるか、*BACK*（後ろ）や*LEFT*（左）などの別の方向に変更してみてください。**   
**数字を2や3に増やすとどうなるでしょうか？**

```python
agent.move(FORWARD, 1)
```

## ターゲット1 @showdialog

エージェントを上下左右前後に動かす方法がわかったので、少し難しいことに挑戦しましょう！

![Target 1](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/lake/target_1.jpg)

## ターゲット1に到達する
`||agent:agent.move(DIRECTION, DISTANCE)||`を使って、エージェントを金色のブロックの上の感圧板の上に立たせることができますか？

**`||agent:agent.move(DIRECTION, DISTANCE)||`を使って、エージェントを金色のブロックまで移動させましょう。**

- 前：FORWARD
- 後：BACK
- 左：LEFT
- 右：RIGHT
- 上：UP
- 下：DOWN