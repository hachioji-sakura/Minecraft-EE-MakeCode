### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - 湖: ターゲット2

```template
agent
```

## ターゲット2に向かう   @showdialog

最後に、エージェントを左側の2番目の金色のブロックまで移動させることができますか？

それは木の上にあります。

![Target 2](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/lake/target_2.jpg)

## ターゲット2

`||agent:agent.move(DIRECTION, DISTANCE)||`を使って、エージェントを木の中の金色のブロックまで移動させましょう。

```python
agent.move(FORWARD, 1)
```
