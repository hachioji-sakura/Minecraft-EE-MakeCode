### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# バウンス（跳ね）

```customts
namespace blocks {
    /**
    * 指定した位置の下にブロックがあるかチェックする
    */
    //% block"Is the block %block under %pos"
    //% block.defl=SLIME_BLOCK
    export function isUnder(block: Block, pos: Position): boolean {
        for (let y = 0; y < 10; y++) {
            const yPos = pos.getValue(Axis.Y) - y
            const checkPos = world(pos.getValue(Axis.X), yPos, pos.getValue(Axis.Z))
            if (blocks.testForBlock(block, checkPos)){
                return true
            }
        }
        return false
    }
}
```

## 望遠鏡を完成させよう @showdialog

新しい望遠鏡は設置されたが、建造を完了するために最後のビーコンを取り付ける必要がある。跳ね上がって設置できるか？

少し高く跳べるように、「浮遊」のやり方を学んで、バウンスするたびにちょっとしたブーストを得よう！

![Image of telescope build](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/bounce/cover.jpg)

## ステップ 1

まず、バウンスしたときに実行される関数を作る必要がある。そのために、`on_player_bounced()` という関数を作る。

**`on_player_bounced()` という関数を作成してください。**

```python
def on_player_bounced():
    # 後でここにコードを書く
    pass
```

## ステップ 2

関数ができたので、関数が実行されたときのプレイヤーの位置を知る必要がある。そのために、`loc` という*変数*を追加し、``||player:player.position()||`` を代入する。

```python
def on_player_bounced():
    loc = player.position()
```

## ステップ 3

スライムブロックの上でバウンスしたときだけ、ブーストの手助けをしたい。そのために、建築業者が ``||blocks:blocks.is_under()||`` という特別な関数を用意してくれた。2 つの入力を受け取る。1 つ目は `SLIME_BLOCK` のようなブロックの種類、2 つ目は調べたい位置の下の場所だ。

**前のステップで追加した `loc` の後に、`block_under` という新しい変数を追加し、``||blocks:blocks.is_under()||`` に `SLIME_BLOCK` と変数 `loc` の 2 つを渡した結果を代入してください。**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
```

## ステップ 4

前のステップで設定した変数 `block_under` が `True` かどうかを、``||logic:if||`` 文でチェックしたい。

**`block_under` が `True` のときの ``||logic:if||`` を作成してください。**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        # 次のステップでここにコードを追加する
```

## ステップ 5

``||logic:if||`` が `True` なら、まず `target`（浮遊効果がかかる対象）を知る必要がある。

そのために ``||mobs:mobs.target(NEAREST_PLAYER)||`` で、効果をかける最も近いプレイヤー（君）を見つけられる。

**`target` という新しい変数を作り、``||mobs:mobs.target(NEAREST_PLAYER)||`` を代入してください。**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
```

## ステップ 6

`target` がわかったので、``||mobs:mobs.apply_effect()||`` で効果をかけられる。

4 つの引数を渡す。1 つ目は使う効果で `LEVITATION`（浮遊）。2 つ目は前のステップで設定した `target`。3 つ目は効果の持続時間で `1` 秒。4 つ目は amplifier（強さ）で、効果の強さを指定する。

**`True` のときに ``||mobs:mobs.apply_effect()||`` が実行されるように追加してください。**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
        mobs.apply_effect(LEVITATION, target, 1, 10)
```

## ステップ 7

最後に、移動したときにゲームがこのコードを実行するようにする。そのために ``||player:player.on_travelled()||`` が使える。2 つの引数を取る。1 つ目は移動の種類で、望遠鏡に上がるには `BOUNCE`。2 つ目は実行したい関数の名前。

**作った関数の外、コードの最後に、``||player:player.on_travelled()||`` を追加し、引数に `BOUNCE` と作った関数 `on_player_bounced` の名前を渡してください。**

## ビーコンを設置しよう！

コードができたら試して、アンテナに上ってビーコンを設置できるか見てみよう！

*注意 - 跳びにくい場合は、`LEVITATION` 効果の持続時間と amplifier を変更してもよい。*

![Bounce path](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/bounce/bounce_path.jpg)

*上はおすすめのバウンス経路です。*
