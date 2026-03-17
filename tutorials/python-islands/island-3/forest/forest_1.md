### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 森

```template
# エージェントの前のブロックを壊す。残りは自分で追加しよう！
agent.destroy(FORWARD)



# 上にコードを追加
```

```ghost
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
for (let i = 0; i < 5; i++){
    agent.destroy(UP)
    agent.move(UP, 1)
    player.say("up 1")
}
```

## 腐った木を倒す @showdialog

木の専門家を手伝って、腐った木を倒しましょう！エージェントは上下に飛べるので、幹の大部分を取り除くのを手伝ってほしいと頼まれています。

作業中は上部を支える支柱と足場が設置してあるので、崩れないので安心してください。

![Cover image of tree](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/forest/cover.png)

## ステップ 1

まず、木の根元を取り除きます。``||agent:agent.destroy||`` で下の 4 ブロックを壊し、``||agent:agent.move||`` で次のブロックへ移動するだけです！

**``||agent:agent.destroy||`` と ``||agent:agent.move||`` を使って、木の最下層の 4 本の丸太を取り除いてください！**

```spy
agent.destroy(FORWARD)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
agent.move(BACK, 1)
agent.move(RIGHT, 1)
agent.destroy(FORWARD)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
```

## ステップ 2

木の最下層の丸太を取り除けたので、次は丸太の積み重なりを取り除きましょう。``||loops:for||`` ループで、同じコードを決まった回数だけ繰り返せます。

**12 回繰り返す ``||loops:for||`` ループをコードに作成してください。**

*for ループの形を忘れたらヒントを見てください*


```spy
for (let count = 0; count < 12; count++){
    // 繰り返すコード
    player.say("Hi")
}
```

## ステップ 3

for ループができたら、エージェントの上を壊してから上へ移動するようにしましょう。

**``||agent:agent.destroy||`` と ``||agent:agent.move||`` を使って、エージェントに `12` 本の丸太を壊すプログラムを書いてください。**

```diffspy
for (let count = 0; count < 12; count++){
    // 繰り返すコード
    player.say("Hi")
}
-------------------------
for (let count = 0; count < 12; count++){
    agent.destroy(FORWARD)
    agent.move(UP, 1)
}
```

## 木を倒し終えよう

いいですね！

丸太を 1 列分取り除けたら、エージェントを各丸太の根元に移動させて、すべて取り除いてください。頑張って！
