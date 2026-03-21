### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 森

```customts
namespace agent {
    /**
     * エージェントの前のブロックを収穫する
    */
    //% block Harvest block
    export function harvest(): void {
        let inspect = agent.inspect(AgentInspection.Block, FORWARD);
        if (inspect === STONE) {
            agent.destroy(FORWARD)
            agent.drop(FORWARD, 2, 1)
        } else if (inspect === 18) {  // Leaves
            agent.destroy(FORWARD)
            agent.drop(FORWARD, 1, 1)
        }
    }

    /**
    * エージェントの前のブロックが巣かどうかをチェックする。巣があれば True、なければ False を返す。
    */
    //% block Check if block is nest
    export function is_nest(): boolean {
        let inspect = agent.inspect(AgentInspection.Block, FORWARD)
        if (inspect === STONE) {
            return true
        }
        return false
    }

    /**
    * エージェントを次の場所に移動させる
    */
    //% block Move to next location
    export function next_location(): void {
        // 21 is a Snow Golem
        mobs.spawn(21, world(166, 153, 220))
    }
}
```

```ghost
player.say(agent.is_nest())
if (agent.is_nest()){
    agent.harvest()
}
agent.next_location()
```


## 森の木材を集める @showdialog

島の森には濃い霧がかかっており、森の探索者たちが島用の木材を収穫するのはほとんど不可能です！

TJ が、君とエージェントで木から木材を収穫してくれないかと頼んでいます。**はしご用に少し取っておく**こともできます。

ただし、木に巣を作っている**鳥を邪魔しない**よう、**十分**注意する必要があります！

![Cover image of forest](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/forest/ForestCover.png)

## はじめに @showdialog

TJ が、この森の任務で使える特別な関数をいくつかエージェントに用意してくれました：

- ``||agent:agent.is_nest()||``：エージェントの前に鳥の巣があれば `True` を返す。なければ `False` を返す。

- ``||agent:agent.harvest()||``：エージェントの前の木材を慎重に収穫し、地面に落とす。

- ``||agent:agent.next_location()||``：TJ がエージェントを次の枝に移動させてくれる。

## ステップ 1

TJ がエージェントを枝の真正面に移動させました。最初の仕事は、（エージェントが見えない状態で）枝に巣があるかどうかを確認することです。

これには ``||agent:agent.is_nest()||`` 関数が使えます。巣があれば `True`、普通の木材だけなら `False` を返します。

**``||player:player.say()||`` で結果を表示して、エージェントの前に巣があるか確認してください。**

```spy
player.say(agent.is_nest())
```

## ステップ 2

``||agent:agent.is_nest()||`` の使い方がわかったので、``||logic:if||`` 文と組み合わせて、前のブロックが**巣かどうか**をチェックできます。

巣がある場合は触らず、``||agent:agent.next_location()||`` を実行して次の場所へ進みます。

**``||agent:agent.is_nest()||`` が `True` を返したときに次の場所へ移動する ``||logic:if||`` 文を作成してください。**

```spy
if(agent.is_nest()){
    agent.next_location()
}
```

## ステップ 3

次に、他のブロックを収穫してから次の場所へ進めるように ``||logic:else:||`` を追加します。

**作成した ``||logic:else:||`` 文の中に ``||agent:agent.harvest()||`` を追加してください。**    
**収穫した後も次の場所へ移動することを忘れずに！**

## ステップ 4

これですべて揃いました。十分な木材が見つかるまで、このプログラムを何度か実行してください。鳥を邪魔しないように気をつけて！頑張って！
