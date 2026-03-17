### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 船の接岸 2

## タラップを作る @showdialog

![Gangplank location](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/ship/gangplank.jpg)

ハッチは覆えました。船長が飛行船を埠頭にできる限り近づけてくれました。

タラップを作る必要があります。エージェントのインベントリのスロット 1 に木材が入っています。

## タラップを作る

**エージェントを `FORWARD`（前）に動かしながら下にブロックを置き、埠頭まで届くタラップを作る ``||loops:for||`` ループのプログラムを作成してください。島までの距離は推測する必要があります！**

```python
for i in range(8):
    agent.move(FORWARD, 1)
    agent.place(DOWN)
```

## タラップができた！

できたらこのウィンドウを閉じて、町を探索してください。

