### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 農場

```customts
/**
* 承認と拒否の関数
*/
namespace agent {
    /**
    * 下の種を小麦としてマークする
    */
    //% block
    export function approve(): void {
        agent.setSlot(1)
        agent.place(UP)
    }

    /**
    * 下の種をニンジンとしてマークする
    */
    //% block
    export function reject(): void {
        agent.setSlot(2)
        agent.place(UP)
    }
    
}
```

## ニンジンと小麦のチェック @showdialog
小麦農場からニンジンを取り除くのを手伝おう！
ピーターは植え付けのときに小麦とニンジンの種をいくつか混ぜてしまいました。エージェントは**あらゆる**ブロックを検出できるので、種をチェックするプログラムを組めます。始めましょう！
![Cover image of Peter](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/farm/PeterCover.png)

ピーターが種をマークするために使える 2 つの特別な関数を用意してくれました：

- `agent.approve()`：下の種を承認する（小麦の種として）

- `agent.reject()`：下の種を拒否する（ニンジンの種として）

## エージェントを動かす

**白いマーカーで印がついた最初の種まで、エージェントを 3 ブロック前に移動させてください。**   
   
**まだコードを実行しないでください！**

```python
agent.move(FORWARD, 3)
```

## エージェントでブロックを調べる
エージェントが種の上に来ました。どんな種か調べましょう。エージェントは `||agent:agent.inspect(AgentInspection.BLOCK, DIRECTION)||` でブロックを調べられます：

**エージェントに下を調べさせ、結果を `block` という新しい変数に格納してください。**
**そして、`block` 変数に格納された値を `say` で表示してください。**

```python
agent.move(FORWARD, 3)
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
```

## If 文のおさらい @showdialog

前のステップでは、エージェントが検出した種（`WHEAT`）を表示しました。今度は、エージェントが小麦を見つけたときに何をするか選ぶコードを作ります。そのために `if` 文を使います。
形のおさらいです：

```python
if (condition):
    # 条件が真のときに実行するコード
```

**変数に値を代入するときは = を 1 つ、2 つの変数の値が等しいか比較するときは == を 2 つ使うことを忘れないでください。**

例：

```python
name = "bob"
if (name == "bob"):
    say("It's bob!")
```

## Inspect と If を組み合わせる
if 文の下に、インデントを 1 つ右にずらして実行したいコードを追加してください。

`||logic:if (condition):||`
        # 何かする

**ブロックが `WHEAT` と*等しい*かチェックする ``||logic:if||`` 文を作成してください。等しければ ``||agent:agent.approve()||`` を実行してください。**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
if block == WHEAT:
    agent.approve()
```


## Else 文のおさらい @showdialog
いいですね！これで、小麦ではないブロックを拒否するために `else` 文が使えます。
`else` 文の形のおさらいです…
```python
if (condition):
    # 条件が真のときに実行するコード
else:
    # 条件が真でないときに実行するコード
```

例：

```python
name = "bob"
if (name == "bob"):
    say("It's bob!")
else:
    say("It isn't bob!")
```

## Else 文を追加する
`||logic:if (condition):||`
        # 何かする
`||logic:else:||`
        # 別のことをする

``||agent:reject||`` 関数を実行する else 文をコードに追加してください。

```python
if block == WHEAT:
    agent.approve()
else:
    agent.reject()
```

## 残りも繰り返す
``||logic:else||`` 文を追加したので、コードを何度か実行してエージェントを畑の端まで進めてください。4 箇所すべてをチェックしたら、ピーターが話しかけてきます。
