### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 塔

```customts
/**
 * 望遠鏡
 */
//% color=purple weight=100 icon="\uf002" block="Telescope"
namespace telescope {
    /**
    * エージェントに塔の建設を開始するよう指示する
    */
    //% block"Build Tower"
    export function start_building() {
        agent.teleport(world(1018,159,79), NORTH)
        build_tower()  // ユーザー関数
        loops.pause(2000)
        let timer = 0
        while (timer < 30) {
            if (blocks.testForBlock(EMERALD_BLOCK, world(1027,154,60))){
                // 塔 A
                agent.teleport(world(1009,159,70), NORTH)
                build_tower()
                // 塔 B
                agent.teleport(world(1027,159,70), NORTH)
                build_tower()
                break
            }
            if (blocks.testForBlock(NETHER_WART_BLOCK, world(1027,154,60))) {
                player.say("There seems to be an issue with the tower")
                throw "Issue with your build_tower, please fix"
            } else {
                loops.pause(1000)
                timer ++
            }
        }
        if (timer === 30) {
            player.say("There seems to be an issue with the tower function")
            player.say("Reset the tower with the builder and start again")
            throw "Issue with your build_tower, please fix"
        }
    }
}

namespace agent {
    /**
    * エージェントにインベントリのブロックで四角形を描かせる
    */
    //% block"Draw Square $size"
    export function draw_square(size: number){
        [FORWARD, RIGHT, BACK, LEFT].forEach((dir) => {
            for(let pos = 0; pos < size-1; pos++){
                agent.place(DOWN)
                agent.move(dir, 1)
            }
        })
    }
}
```

```template

// この行の上にコードを書いてください
telescope.start_building()
```

## 支える塔を建設する @showdialog
地元の建築業者が新しい望遠鏡の準備をしているが、パラボラを支える塔が必要だ！塔を建てて望遠鏡の設置を手伝おう。

![The telescope](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/tower/cover.jpg)

## はじめに

この任務では `functions`（関数）を使います。`Functions` は小さなコードのまとまりで、メインプログラムで何度でも呼び出し・実行できます。例えば `||player:player.say()||` は、チャットに文字を表示するために呼び出す関数です。

以下の練習を進めると、建築業者が君の関数をテストして実行してくれます。

## ステップ 1

建築業者から、`"build_tower()"` という `function`（関数）を作ってほしいと頼まれました。

そのために、  
`def build_tower():` と書きます。

- `def` ：Python に新しい関数を作ることを伝える。
- `build_tower():` ：新しい関数の名前。このコードを実行したいときは、コードに `build_tower()` と書く。

```python
def build_tower():
    # 後でここに何かを書く
    pass
```

## ステップ 2

`function` ができたので、高さ `15` ブロックの塔を建てるようにします。そのために、`15` 回実行される ``||loops:for||`` ループを使います。

Python で関数にコードを書くとき、関数の一部として実行するコードはすべて*インデント*（字下げ）する必要があります。行の先頭にスペース 4 つを入れます。

**`0` から `15` まで数える ``||loops:for||`` ループを追加してください。**

```python
def build_tower():
    for height in range(0, 15):
        # 後でここに何かを書く
        pass
```

## ステップ 3

*注意：コードを開始すると、エージェントは自動的にダイヤモンドブロックの位置にテレポートします。*

``||loops:for||`` ループができたら、塔の層をすべて作るために、繰り返しのたびにエージェントを 1 ブロック上に移動させる必要があります。

**for ループの中で、エージェントを ``||agent:move||`` で `UP`（上）に `1` ブロック移動させてください。**

```python
def build_tower():
    for height in range(0, 15):
        agent.move(UP, 1)
```

## ステップ 4

エージェントが上に移動するたびに、塔の新しい層を作れます。そのために ``||agent:agent.draw_square()||`` 関数を使います。エージェントが立っている位置に四角形を作れます。

``||agent:agent.draw_square()||`` は 1 つの入力（四角形の幅）を取ります。例えば 5 なら 5x5 の層になります。

**幅 `3` で `agent.draw_square()` を実行するコードを追加してください。**

## コードを実行しよう
できたらコードを実行してください。建築業者が君のエージェントを使って塔を建てます。
