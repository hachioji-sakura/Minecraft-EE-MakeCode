### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 図書館

```template
if (agent.check_book_on_shelf(FORWARD) === ){
    player.say("Found the book!")
} else {
    player.say("")
}
```

```customts
/**
 * 図書館で作業するための関数
 */
namespace agent {
    /**
    * 呪文の本が棚にあるかチェックする
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function check_book_on_shelf(direction: SixDirection): boolean {
        let block = agent.inspect(AgentInspection.Block, direction)
        if (block == DEAD_BRAIN_CORAL_BLOCK) {
            return true
        }
        return false
    }

    /**
     * 呪文の本がある棚に印をつける
     */
    //% block="agent mark book %direction"
    //% direction.defl=FORWARD
    export function mark_book(direction: SixDirection){
        if(direction === FORWARD){
            agent.place(BACK)
        }else{
            player.say("Seems like the agent can only mark facing forward of the bookshelf")
        }
    }
}
```

```ghost
for (let count = 0;count < 5;count++){
    if (agent.check_book_on_shelf(FORWARD)){
        agent.mark_book(FORWARD)
    }
    agent.move(UP, 1)
}
```

## 呪文の本を探す @showdialog

魔法使いに必要な呪文の本を図書館で見つけてください。

![Bookshelves](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/library/shelves.jpg)

## 棚をスキャンする
図書館には本の棚がたくさんあります。どれも同じに見えますが…正しい本は見つかるでしょうか？

*「私がお手伝いします！エージェントに ``||agent:agent.check_book_on_shelf(DIRECTION)||`` という特別な関数を追加しました。**if 文**で、調べている本棚に目的の本があるか確認するときに使えます。本があれば True、なければ False を返します。」 - ウィロー（司書）*

**エージェントを見つけ、目の前の本棚をチェックするために用意されたコードを完成させてください。**

```spy
if (agent.check_book_on_shelf(FORWARD) == true){
    player.say("Found the book!")
} else {
    player.say("No book here!")
}
```

## 本棚の列全体をスキャンする

その本ではなかったようです…でも、まだチェックできる本棚はたくさんあります。``||loops:for||`` で、1 回の実行で複数の本棚をチェックできます！

**列にある本棚の数を数え、前の活動のコードを使った for ループを作成して、その列の本をすべてチェックしてください。**

```diffspy
if (agent.check_book_on_shelf(FORWARD) == true){
    player.say("Found the book!")
} else {
    player.say("No book here!")
}
---------------------------------------
for (let count = 0; count < 5; count++){
    if (agent.check_book_on_shelf(FORWARD) == true){
        player.say("Found the book!")
    } else {
        player.say("No book here!")
    }
    agent.move(UP, 1)
}
```

## 棚に印をつける

本が見つかったら、司書が本を取れるようにその棚に印をつける必要があります。

司書がエージェントに ``||agent:agent.mark_book(DIRECTION)||`` という関数を追加してくれました。本が見つかった棚でこの関数を実行してください。

**本が見つかったときに実行されるよう、if 文にこれを追加してください。**

## 本を受け取る

棚に印をつけたら、司書のところへ戻って本を取ってもらってください。司書はとても忙しいので、正しい棚かどうかよく確認してください。
