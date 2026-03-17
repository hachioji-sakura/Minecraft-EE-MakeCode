### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# 農場
```customts
namespace agent {
    /**
    * 指定した方向の花を返す
    */
    //% block
    export function checkFlower(direction: SixDirection): Block {
        let block = agent.inspect(AgentInspection.Block, direction);
        if (block == POINTED_DRIPSTONE) {
            return POPPY;
        } else {
            return block;
        }
    }
}
```


## 花の自動収穫と選別 @showdialog
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/farm/cover.jpg)

**庭師** - 「*植物園へようこそ！必要な赤い染料にするヒナゲシを摘むのを手伝ってほしい。君とエージェントでヒナゲシを摘んでくれないか？*」

`||loops:while||` ループを使うと、**十分な数になるまで**エージェントがヒナゲシを集め続けます。ヒナゲシが十分（4 つ）になったら、エージェントは止まります。

## タスク 1
**`||loops:while||` ループを用意し、条件に ``||agent:agent.get_item_count||`` をスロット番号（1）だけを引数にして使ってください。スロット 1 のヒナゲシが 4 つ未満の間、このループを繰り返します。**

```python-ignore
while agent.get_item_count(1) < 4:
```

## タスク 2

**ループの中で、ヒナゲシが 4 つ未満の間、エージェントを 'FORWARD'（前）方向に動かす ``||agent:agent.move||`` を追加してください。**

いつでもホイッスルでエージェントを呼び戻せることを忘れないでください。

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
```

## 花をチェックして壊す @showdialog
エージェントを動かせるようになったので、下にどんな花があるか確認し、収穫（*壊す*）するかどうか決める必要があります。
そのために ``||agent:agent.check_flower||``（方向は `DOWN`）が使えます。エージェントの下の花の種類を返します。
この情報を `||logic:if||` 文で使い、花が `"POPPY"` かどうかをチェックできます。
ヒナゲシなら、``||agent:agent.destroy||``（方向は `DOWN`）でエージェントの下の花を摘めます。

## タスク 3
**while ループの中に、``||agent:agent.check_flower||`` で花が `"POPPY"` かどうかをチェックする `||logic:if||` 文を追加してください。**
**ヒナゲシなら、`||agent:agent.destroy||` を呼んでください。エージェントの下（DOWN）をチェックするようにしてください。**

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
    if agent.check_flower(DOWN) == POPPY:
        agent.destroy(DOWN)
```

## タスク 4
エージェントが 1 列の花をチェックし終えたので、次の列に移る必要があります。そのために while ループの上に ``||agent:agent.move||`` と ``||agent:agent.turn||`` を追加し、エージェントが次の列を始められるようにしてください。
向きを変える方向を毎回変えながら、もう何度か繰り返して、すべての列を調べてください。

```ghost
agent.turn(LEFT)
```
