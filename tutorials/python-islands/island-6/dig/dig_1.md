### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 発掘（Dig）

```customts
namespace agent {
    /**
    * エージェントの下に化石があるかチェックする
    */
    //% block
    export function isFossilBelow(): boolean {
        let block = agent.inspect(AgentInspection.Block, DOWN)
        return block == DEAD_FIRE_CORAL_BLOCK
    }
}

/**
 * 科学者
 */
//% color=purple weight=100 icon="\uf0c3" block="Scientist"
namespace scientist {
    /**
    * 科学者がリストにすべての化石が含まれているかチェックする
    */
    //% block
    export function check(final: any[]): void {

        let solution = [world(1019, 139, 110), world(1018, 139, 111), world(1017, 139, 109)].sort()
        let final_sorted = final.sort()

        let list_equal = true

        if (solution.length !== final_sorted.length) {
            list_equal = false
        };
        for (let i = 0; i < solution.length; i++) {
            if (!positions.equals(solution[i], final_sorted[i])) {
                list_equal = false
            };
        }

        if (list_equal) {
            blocks.place(DIAMOND_BLOCK, world(991, 144, 122))
        } else {
            player.say("\nHmmm...\nAll of the coordinates don't lead to fossils... Try again.")
        }
    }
}
```

## 恐竜を発掘しよう @showdialog
最近、島の考古学チームが先史時代の遺物を発見した。エージェントを使って、地面の下に隠れた古代の化石を探そう！

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/dig/cover.png)

## リスト @showdialog
エージェントは強力なセンサーで化石の位置を特定し、それぞれの位置を発掘チームに伝える。

そのために、化石の位置をリストに格納し、調査が終わったらチームに渡す。

リストの作り方のおさらい…

`||agent:agent.is_fossil_below()||`

```python

my_list = [] # 空のリスト（要素がない）

```

## 空のリストを作る
**後で化石の位置を追加できる、`coordinates` という空のリストを作成してください。**

```python
coordinates = []
```

## for ループをいくつか作る
2 つの for ループで 2 次元の範囲をカバーし、化石をチェックできる。

for var in range(start, stop):

**0 から 3 まで繰り返す 2 つの ``||loops:for||`` ループを、一方をもう一方の中に書いてください。**

**外側のループは変数 `row`、内側のループは列用に変数 `col` を使ってください。**

**プログラムが想定どおり動いているか確認するため、`row` と `col` の値を表示する say コマンドを追加してください。**

```python
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
```

## エージェントを動かす
エリア全体をスキャンするにはエージェントを動かす必要がある。

**内側のループの中で、``||agent:agent.move||`` でエージェントを 1 ブロック前に移動させてください。内側のループが 1 回終わるたびに、エージェントを 3 ブロック後ろに、それから 1 ブロック左に移動させ、次の行をスキャンできるようにしてください。**

**両方のループの外で、エージェントを開始位置に戻して最初からスキャンできるようにするため、両方のループの後にエージェントを右に 3 ブロック移動させてください。**

```python
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
        agent.move(FORWARD, 1)
    agent.move(BACK, 3)
    agent.move(LEFT, 1)
agent.move(RIGHT, 3)
```

## リストへの追加 @showdialog
リストの末尾に何かを追加するには `||arrays:append||` を使う。

例えばエージェントの座標を coordinates リストに追加するなら、こうする：

```python
agent_pos = agent.get_position()
coordinates.append(agent_pos)
```

```ghost
if agent.is_fossil_below():
    scientist.check([])
```

## 化石をチェックする
科学者向けに化石に印をつける必要がある。

**内側のループでエージェントを動かす前に、エージェントの下に化石があるかチェックしてください。そのために ``||agent:agent.is_fossil_below||`` を使う。化石があれば、エージェントの座標をリストに追加する。**

**コードの最後で ``||scientist:scientist.check(coordinates)||`` を呼んでリストをチェックし、任務を完了してください。**

```python
if agent.is_fossil_below():
    coordinates.append(agent.get_position())
```

```ghost
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
        if agent.is_fossil_below():
            coordinates.append(agent.get_position())
        agent.move(FORWARD, 1)
    agent.move(BACK, 3)
    agent.move(LEFT, 1)
agent.move(RIGHT, 3)

scientist.check(coordinates)
```
