### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 船の接岸

```template
for (let count = 0; count < 5; count++){
    player.say("Hello")
}
```

## ループの基本 @showdialog

Python では、何度も同じことを実行したいとき（コードを何度もコピー＆ペーストしないで）は、ループというものを使います。

Python には主に 2 種類のループがあります：

- **For ループ** - 繰り返し回数がわかっているときに使う。

- **While ループ** - 何回繰り返すかわからないときに使う。

このワールドでは **for ループ**を中心に使います。

``||loops: for loop||`` は次のような書き方で作ります：

```spy
for (let count = 0; count < 5; count++){
    player.say("hello")
}
```

上のコードでは、`player.say("hello")` が 5 回実行されます。

## ハッチを覆おう @showdialog

![Captain](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/ship/captain.jpg)

**パパート船長** - *もうすぐ接岸するが、その前にハッチを覆うのを手伝ってくれないか？船のメインデッキにあるんだ。*

## エージェントでデッキを覆う

パパート船長がエージェントに**カーペット**（スロット 1）を渡してくれました。``||loops:for||`` と ``||agent:agent.place()||`` で、ハッチの上にカーペットを敷いてください。

*1 列終わったら**ホイッスル**（または ``||agent:agent.move()||``）でエージェントを移動させ、もう一度コードを実行してください。*

方向：
- 前：FORWARD
- 後：BACK
- 左：LEFT
- 右：RIGHT
- 上：UP
- 下：DOWN

```spy
for (let count = 0; count < 6; count++){
    agent.move(FORWARD, 1)
    agent.place(DOWN)
}
```
