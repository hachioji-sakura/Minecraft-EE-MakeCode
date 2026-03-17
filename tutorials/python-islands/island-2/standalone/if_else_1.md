### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# If-Else（条件分岐）

```customts
namespace gameplay {
    /**
    * 現在の天気をランダムに変える
    */
    //% block
    export function randomWeather(): void {
        if (randint(0, 1) == 0) {
            gameplay.setWeather(CLEAR)
        } else {
            gameplay.setWeather(THUNDER)
        }
    }
}

namespace player {
    /**
    * タスクを完了する
    */
    //% block
    export function complete(): void {
        blocks.place(Block.DiamondBlock, world(112, 150, 194))
        player.say("Task complete")
    }
}
```

```template
gameplay.randomWeather();

if (THUNDER) {
    player.say("");
}
```

## Python で判断する @showdialogue

プログラミングでは、条件に応じて判断を下すことがよくあります。判断では、ある条件が ``||logic:True||`` のときに ``||logic:if||`` でコードを実行したいと思います。

例えば、いつも判断しなければならないことの一つに、レインコートを着るかどうかがあります。

雨が降っているなら ---> コートを着よう！

Python では、次のように書けます：

```python
if gameplay.weather_query() == RAIN:
    player.say("Put on a coat!")
```

## If 文

以下のプログラムを完成させ、``||gameplay:gameplay.weather_query()||`` が ``||THUNDER||`` かどうかをチェックしてください。雷の場合は 2 行目で ``||player:player.say||`` にメッセージを追加してください。

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
```

## 雨じゃない場合は？ @showdialogue

何かが成り立つ場合の扱いは説明しましたが、成り立たない場合はどうでしょう？

雨が降っていない場合は？

成り立たない場合を扱うには `||logic:else||` を使います。`||logic:Else||` は**それ以外すべて**の場合にコードを実行できます。

例は次のとおりです：

```python
if gameplay.weather_query() == RAIN:
    say("Put on a coat!")
else:
    say("Just put on a jumper")
```

## Else 文

``||THUNDER||`` がない場合に、適切な別のメッセージを送るようにプログラムを完成させてください。

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
else:
    player.say("There is no thunder :)")
```

## インデント

インデントとは、行の先頭の空白の数です。Python では、どのコードがどの構造に含まれるかを示すためにインデントを使います。

**タスクを完了するには ``||player:player.complete||`` 関数を実行してください。必ず実行されるように、インデントしないでください。**

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
else:
    player.say("There is no thunder :)")
player.complete()
```
