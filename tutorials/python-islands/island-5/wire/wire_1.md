### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# ワイヤー（配線）

```customts
namespace positions {
    /**
    * 補正した位置を返す
    */
    //% block"Correct Location %pos"
    export function correctLocation(pos: Position) {
        const y = pos.getValue(Axis.Y)+1
        return world(pos.getValue(Axis.X), y, pos.getValue(Axis.Z))
    }
}

namespace agent {
    /**
     * エージェントにワイヤーを置かせる
     */
    //% block="agent place wire %direction"
    //% direction.defl=DOWN
    export function placeWire(direction: SixDirection) {
        agent.setSlot(1)
        if (direction !== DOWN) {
            return
        }
        const agentLoc = agent.getPosition()
        const y = agentLoc.getValue(Axis.Y)-1
        const blockTest = blocks.testForBlock(AIR, world(agentLoc.getValue(Axis.X), y, agentLoc.getValue(Axis.Z)))
        if (blockTest){
            agent.place(DOWN)
        }
    }
}
```

```ghost
function test() {
    return
}

player.onTravelled(WALK, function () {
    let loc = player.position()
    loc = positions.correctLocation(loc)
    agent.teleport(loc, NORTH)
    agent.placeWire(DOWN)
})

```

## 発電所までワイヤーを引く @showdialog

望遠鏡が建てられ、星を探す準備が整った。あと必要なのは電源だ！発電所と望遠鏡の島にある変圧器の建物の間にワイヤーをつなぐ必要がある。

ワイヤーは壊れやすいので、エージェントにやらせる。

橋の上で君についてきて、ワイヤーを置くようにエージェントにプログラムしてくれないか？

![Picture of Power station](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/wire/cover.jpg)

## ステップ 1

まず、移動するたびに実行される関数を作る必要がある。そのために、移動したときに Minecraft が呼び出す関数を作る。`on_travelled_walk()` と呼ぼう。

**`on_travelled_walk()` という関数を作成することから始めてください。**

```python
def on_travelled_walk():
    # これからのステップでここにコードを追加する
    pass
```

## ステップ 2

プログラムに、君が歩いた場所を知らせる必要がある。そのために、`loc` という*変数*を追加し、``||player:player.position()||`` を代入する。

```python
def on_travelled_walk():
    loc = player.position()
```

## ステップ 3
歩きながら、エージェントがワイヤーを置く正確な位置を取得する必要がある。そのために、今追加した `loc` 変数が使える。

エージェントが使う位置を補正するには、`||positions:positions.correct_location()||` 関数を実行し、`loc` 変数を渡す。そして結果を新しい `loc` に格納する。

**新しい行で、`loc` を `||positions:positions.correct_location()||` の結果にし、`position` として `loc` 変数を渡してください。**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
```

## ステップ 4
次のステップは、エージェントを補正した位置にテレポートさせることだ。エージェントのテレポートには ``||agent:agent.teleport()||`` が使える。

**エージェントを `loc` の位置に `NORTH`（北）を向けてテレポートさせるコードを追加してください。**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
    agent.teleport(loc, NORTH)
```

## ステップ 5
最後のステップは、エージェントにワイヤーを置いて接続させることだ。

発電所のスタッフが、すでにエージェントにワイヤーと、ワイヤーを置く関数を渡してくれている。あとは ``||agent:agent.place_wire()||`` で `DOWN`（下）に置くだけだ。

**下に ``||agent:agent.place_wire||`` を追加し、`DOWN` に置くようにしてください。**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
    agent.teleport(loc, NORTH)
    agent.place_wire(DOWN)
```

## ステップ 5
最後に、移動したときにゲームがこのコードを実行するようにする。そのために ``||player:player.on_travelled()||`` が使える。2 つの引数を取る。1 つ目は移動の種類で、ワイヤーを敷くには `WALK`。2 つ目は実行したい関数の名前。

**作った関数の外、コードの最後に、``||player:player.on_travelled()||`` を追加し、引数に `WALK` と作った関数 `on_travelled_walk` の名前を渡してください。**

## ワイヤーを敷き始めよう！

準備ができたらコードを実行し、橋の右側の道をゆっくり歩いて、エージェントがついてきてワイヤーを置くようにしよう。「**外部発電所プラグ**」から始めてください。
