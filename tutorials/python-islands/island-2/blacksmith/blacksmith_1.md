### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 鍛冶屋

```customts
/**
 * 鍛冶屋を手伝うコマンドを与える
 */
//% color=Grey weight=100 icon="\uf0e3" block="blacksmith"
namespace blacksmith {
    /**
    * 鉱石の純度を取得する
    */
    //% block="purity %direction"
    //% direction.defl=FORWARD
    export function purity(direction: SixDirection): number {
        const block = agent.inspect(AgentInspection.Block, direction)
        switch(block){
            case IRON_ORE:
                return 4
            case 896:
                // raw_iron_block
                return 3
            case 153:  // Nether quartz ore
                return 2
            case 765: // Block of netherite
                return 1
            default:
                return 0
        }
    }

    /**
    * 鉱石を却下する
    */
    //% block="Deny Ore"
    export function deny():void {
        agent.setSlot(2)
        agent.place(UP)
    }

    /**
    * 鉱石を受け入れる
    */
    //% block="Accept Ore"
    export function accept():void {
        agent.setSlot(1)
        agent.place(UP)
    }
}
```

```ghost
if(blacksmith.purity(FORWARD) <== 3) {
    player.say("Purity less than or equal to 3!")
    blacksmith.deny()
} else {
    blacksmith.accept()
}
```

## 純粋な鉄の抽出 @showdialog
必要な鉄鉱石を集めました。最後のステップは、使用するのに十分な純度かどうかを確認することです！鍛冶屋は、エージェントを使って最も純度の高い鉄を見つけてほしいと頼んでいます。

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/blacksmith/cover.png)

## 鉱石の純度を確認する

この作業を手伝うため、鍛冶屋はエージェントに ``||blacksmith:blacksmith.purity()||`` という鉄の純度をチェックできる特別な関数を装備してくれました。

この関数は、エージェントがチェックする方向（例：`FORWARD`）を引数として受け取ります。

*このステップではコードを書く必要はありません。次のステップに進んで始めましょう*

## ステップ 1

鉱石から最も純粋な鉄を得たいので、``||logic:if||`` 文を使って、ブロックの純度が 3 未満かどうかをチェックします。

Python では、ある値が別の値と等しいか（`==` を使用）をチェックするだけでなく、より大きいか小さいかのチェックもできます。

**鉱石の純度が `3` 以下（`<=` を使用）かどうかをチェックする ``||logic:if||`` を作成してください。**

```python
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
    // 次のステップでここにコードを書く
```

## ステップ 2
鉄の純度が 3 以下かどうかをチェックする if 文ができたので、``||blacksmith:blacksmith.deny()||`` コマンドを使って、鍛冶屋にとって無効なブロックとしてマークしましょう。

**純度が 3 以下のときに ``||blacksmith:blacksmith.deny||`` が実行されるように追加してください。**

```diffpython
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
------------------------------------
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
    blacksmith.deny()
```

## ステップ 3

純度が 3 以下の鉄用のコードが完成したので、受け入れる鉄鉱石ブロック用のコードを追加しましょう。

鉱石を受け入れるには、鍛冶屋が ``||blacksmith:blacksmith.accept()||`` というコマンドをくれています。

**if 文の下に、``||blacksmith:blacksmith.accept||`` を実行する `else` 文を追加してください。**

## すべての鉱石をチェックしよう！
コードが完成したら、すべての鉄がチェックされるまで何度も実行してください！
