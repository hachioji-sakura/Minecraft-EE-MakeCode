### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 鉱山

```template
let found_diamond = 0;
while (found_diamond < 3) {

}
```

```customts
namespace agent {
    /**
    * 鉱石の種類を返す
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function checkOre(direction: SixDirection): Block {
        if (agent.inspect(AgentInspection.Block, direction) == RED_NETHER_BRICK) {
            return DIAMOND_ORE
        } else if (agent.inspect(AgentInspection.Block, direction) == NETHER_BRICK) {
            return DIRT
        } else {
            return agent.inspect(AgentInspection.Block, direction)
        }
    }

    /**
    * ダイヤモンドブロックに印をつける
    */
    //% block="agent mark diamond"
    export function markDiamond(): void {
        if (checkOre(FORWARD) != AIR) {
            agent.setSlot(2)
            agent.place(UP)
        } else {
            player.say("Unable to detect a block!")
        }
        loops.pause(300)
    }

    /**
    * 廃棄するブロックに印をつける
    */
    //% block="agent mark bin"
    export function markBin(): void {
        if (checkOre(FORWARD) != AIR) {
            agent.setSlot(1)
            agent.place(UP)
        } else {
            player.say("Unable to detect block")
        }
        loops.pause(300)
    }
}
```

## 採掘したものを選別する @showdialog
![Farming](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/mine/cover.jpg)

鉱山へようこそ！今日採掘した鉱石の選別を鉱夫たちが手伝ってほしいと言っています。ただ、選別室は粉塵が多すぎて人が入れません。なのでエージェントが送り込まれました。選別して処理用に印をつけるプログラムを書きましょう。
この任務ではダイヤモンド鉱石を 3 つ見つける必要があります。


## While ループ @showdialog
まず、探している 3 つのダイヤモンド鉱石ブロックをまだすべて見つけていない間だけ実行される `||loops:while||` ループを作ります。

そのために `||loops:while||` ループを使い、ダイヤモンドの数を数える変数が `<` 記号で 3 未満かどうかをチェックします。これは、記号の左側が右側より小さいことを意味します。

以下が `||loops:while||` ループの例です。


```python
found_diamond = 0
while found_diamond < 3:
    player.say("I keep looping!")
```

## タスク 1

エージェントに、指定した方向の鉱石を返す `||agent:agent.check_ore||` という特別な関数が与えられています。

**ループの中に、``||agent:agent.check_ore||`` を使った `||logic:if||` 文を追加し、エージェントの前のブロックが `DIAMOND_ORE` かどうかをチェックしてください。ダイヤモンドなら found_diamond を増やし、``||player:player.say||`` で「`diamond found`」と表示してください。**

```python
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        player.say("diamond found")
        found_diamond = found_diamond + 1
```

## ダイヤモンドに印をつける @showdialog
ダイヤモンド鉱石のチェック方法がわかったので、鉱夫向けにダイヤモンドを含むブロックに印をつける必要があります。そのために `||agent:agent.mark_diamond||` が使えます。鉱山で処理できるようにダイヤモンド鉱石に印をつけてくれます。

ダイヤモンド以外の鉱石にも、廃棄する印をつける必要があります。if 文の後に `||logic:else||` 文と `||agent:agent.mark_bin||` を使い、廃棄する鉱石に印をつけます。`||logic:else||` 文は、その上の `||logic:if||` 文が実行されなかったときに実行されます。

## タスク 2
**鉱夫がダイヤモンド鉱石の場所を知れるように、``||player:player.say||`` を ``||agent:agent.mark_diamond||`` に変更してください。**

```python
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.mark_diamond()
        found_diamond = found_diamond + 1
```

## タスク 3
**`||loops:while||` ループの中で、鉱石がダイヤモンド鉱石でないときに ``||agent:agent.mark_bin||`` を実行する `||logic:else||` 文を追加し、鉱夫が廃棄すべきだとわかるようにしてください。**


```ghost
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.mark_diamond()
        found_diamond = found_diamond + 1
    else:
        agent.mark_bin()
```
