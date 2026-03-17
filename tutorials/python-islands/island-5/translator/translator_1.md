### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# トランスレーター（変換器）

```customts
/**
 * トランスレーターのコンピュータを解読する機能を提供する
 */
//% color=purple weight=100 icon="\uf002" block="Telescope"
namespace telescope {
    /**
    * 望遠鏡に解読関数を実行するよう指示する
    */
    //% block"Decode telescope bit signal"
    export function decode_signals(): void {
        // 暫定対応: makecode は Record<> をオブジェクトでサポートしないため ts コンパイラで `object[key]` が使えない
        const index_key = [ORANGE_CONCRETE_POWDER, MAGENTA_CONCRETE_POWDER, LIGHT_BLUE_CONCRETE_POWDER, YELLOW_CONCRETE_POWDER]
        const index_value = ["a", "b", "c", "d"]
        // ユーザーの decode() 関数から期待されるビットのリスト
        const list_of_numbers: number[] = [1, 2, 4, 3, 2, 1]

        let counter = 0  // メッセージの進行状況をチェックするためのカウンター

        for(let bit_index = 0; bit_index < list_of_numbers.length; bit_index++){
            const bit = list_of_numbers[bit_index]
            const inspect = agent.inspect(AgentInspection.Block, FORWARD)
            // ブロックを取得
            const block_key_index: number = index_key.indexOf(inspect)
            let block = "Z"
            if (block_key_index >= 0){
                block = index_value[block_key_index]
            }

            counter++
            const num = decode(block)  // ユーザーの decode を実行

            if (num === undefined) {
                throw "No number given! Please fix your function, or Reset Bit Input and try again."
            }
            player.say(`Decoded bit as : ${num}`)

            if (num !== bit) {
                player.say("Incorrect bit given!")
                throw "Incorrect bit! Please fix your function, or Reset Bit Input and try again."
            } else {
                if (counter === 6) {  // 最後のビットを受信した場合
                    player.say("Received full all the data, task complete!")
                    player.say("Data: 1, 2, 4, 3, 2, 1")
                    loops.pause(1000)
                } else { // 次のビットを読み込む
                    player.say("Loading Next Bit")
                }
                mobs.spawn(21, world(1007, 150, 132))  // 21 is a Snow Golem
            }
            loops.pause(1000)
        }
        mobs.spawn(21, world(1014, 148, 132))  // 21 is a Snow Golem
    }
}
```

```template

// 解読関数を実行するため、コードの最後にこの行を残してください！
telescope.decode_signals()
```

## 入力を受け取って変換する @showdialog

**ジョリーン**- 「*コンピュータ研究センターへようこそ。宇宙からのメッセージを受信するために望遠鏡が向けるべき角度を計算する、高度なコンピュータプログラムを作りました。その出力データの解読を手伝ってもらえませんか？*」

![Computer terminal](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/translator/cover.jpg)

## ステップ 1

コンピュータ研究センターから、彼らのために `decode` 関数を作ってほしいと頼まれました。エージェントと一緒に使い、コンピュータが出力するデータを解読するのに使います。

データを `function`（関数）に渡すには、`parameter`（引数）を作る必要があります。`parameter` を使うと、メインプログラムから変数の形で関数にデータを渡せます。

**まず、`info` という 1 つの引数を持つ `decode` という関数を作成してください。**

```python
def decode(info):
    pass
```

## ステップ 2
関数に `info` という引数でデータが渡されるようになりました。`info` には文字が入り、コンピュータはその文字に対応する数字が必要です。

まず `info` が `"a"` のときに `1` を返すようにしましょう。そのために `||logic:if||` 文が使えます。

`||logic:if||` の後、関数の中で、`info` が認識されないときのデフォルト値 `0` を返す `||logic:else||` 文を追加してください。

```python
def decode(info):
    if info == "a":
        return 1
    else:
        return 0
```

## ステップ 3

基本的な `decode` 関数ができたので、コンピュータが解読してほしい入力すべてに対応できるようにします。

そのために、作った `||logic:if||` を `||logic:elif||` で広げます。

次の表に従って、正しい数字を返す `||logic:if/else||` 文のセットを作成してください。

| info     | return |
|----------|--------|
| `a`      | `1`    |
| `b`      | `2`    |
| `c`      | `3`    |
| `d`      | `4`    |
| `other`  | `0`    |

```python
def decode(info):
    if info == "a":
        return 1
    elif info == "b":
        return 2
    # ... 以下同様
    else:
        return 0
```

## コードを実行しよう！

準備ができたらコードを実行して、動くか確認してください！

*注意：コードを始める前に、エージェントの上にある **Reset Bit Input** ボタンを押す必要があります！*
