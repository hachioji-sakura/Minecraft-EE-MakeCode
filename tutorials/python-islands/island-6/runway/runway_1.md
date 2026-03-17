### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# 滑走路
```customts
namespace agent {
    /**
    * エージェントを滑走路の左端に戻す
    */
    //% block
    export function returnAgent(): void {
        let position = agent.getPosition();

        let y = position.getValue(Axis.Y);
        let z = position.getValue(Axis.Z);

        let orientation = agent.getOrientation();

        agent.teleport(world(948, y, z), SOUTH);
    }
}

/**
 * 滑走路
 */
//% color=purple weight=100 icon="\uf018" block="Runway"
namespace runway {
    /** 
    * 滑走路のデザインを含むリストを取得する
    */
    //% block
    export function getRunwayDesign(): boolean[][] {
        return [[false, false, false, false, false, false, false, false, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, false, false, false, false, false, false, false, false],
        [false, false, true, true, true, false, true, true, true, false, false],
        [false, false, false, true, false, false, true, false, true, false, false],
        [false, false, false, true, false, false, true, true, true, false, false],
        [false, false, false, true, false, false, true, false, true, false, false],
        [false, false, true, true, false, false, true, true, true, false, false]];
    }
}
```

```template
const runway_design = runway.get_runway_design();
for (const row of ) {
    player.say()
}
```

## 滑走路のデザイン @showdialog
ロケットの打ち上げエリアを建設する。

空港の滑走路はほぼ完成している。最後のステップは滑走路のマーキングを仕上げて、飛行機がどの角度で着陸すべきかわかるようにすることだ。

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/runway/cover.png)

## リストを扱う @showdialog

空港マネージャーのマリンダが、滑走路にマークしたい位置をリストの形でエージェントに渡してくれた。始める前に例を見てみよう。

小さなリスト（各行）にアクセスするには `||loops:for||` ループが使える。`range` の代わりに、`large_list` の中の各 `small_list` を取り出すようにする。

```python
large_list = [ [1,2,3], [4,5,6], [7,8,9] ]
for small_list in large_list:
    player.output(smaller_list)
```

## タスク 1
**滑走路デザインの各 `row`（行）を取得して表示する ``||loops:for||`` ループを完成させてください。**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    player.say(row)
```

## タスク 2
各行を個別に取得できるようになったので、各行の各ブロックを取得しよう。

前と同じようにするが、滑走路デザインの各 `row` を取得する代わりに、各 `row` の各 `block` を取得する。

**既に書いた for ループの中に、各 `row` の各 `block` を取得するもう 1 つの ``||loops:for||`` ループを書いてください。**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    for block in row:
        player.say(block)
```

## タスク 3

各行の各ブロックを 1 つずつ取得できるようになったので、エージェントを動かしてブロックを置くプログラムが書ける。

ブロックが「True」ならブロックを置き、そうでなければ置かない。

**内側のループで、`block` が true のときに、``||logic:if||`` 文と ``||agent:agent.set_slot||``、``||agent:agent.place||`` を使って、スロット 1 から `DOWN`（下）方向にブロックを置くコードを追加してください。**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    for block in row:
        if block:
            agent.set_slot(1)
            agent.place(DOWN)
```

## タスク 4 @showdialog

リストからブロックを取得して置けるようになったので、エージェントが滑走路を横切って移動するようにコードを書ける。

ループが 2 つあるので、``||agent:agent.move||`` を 2 つ追加する必要がある。

- 1 つ目は、ブロックを置くたびにエージェントを次のブロックへ移動させる。

- 2 つ目は各行の終わりに、エージェントを次の行へ前に移動させる。

各行が終わったら ``||agent:agent.return_agent||`` でエージェントを滑走路の左端に戻すこともできる。

## タスク 4

**``||agent:agent.move||`` を 2 つ追加してください。1 つはブロックを置いた後にエージェントを `RIGHT`（右）に移動させる。もう 1 つは 2 つ目のループが終わった後にエージェントを `FORWARD`（前）に移動させる。その後、2 つ目の ``||agent:agent.move||`` の下に ``||agent:agent.return_agent||`` を追加してください。**

```ghost
for i in range(4):
    pass
```
