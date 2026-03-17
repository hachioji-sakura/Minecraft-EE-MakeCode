### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 鉱山 - 1

```customts
/**
 * 鉱山で作業するための関数
 */
namespace agent {
    /**
    * エージェントの下の地面が安定しているかチェックする
    */
    //% block="agent check ground stable"
    export function check_ground_unstable(): boolean{
        const agent_pos = agent.getPosition()
        if (positions.equals(agent_pos, world(88, 146, 167))){
            return true
        }
        return false
    }

    /**
     * エージェントの下の地面が不安定であることを警告する
     */
    //% block
    export function alert(){
        if(agent.check_ground_unstable()){
            player.say("Unstable ground alert!!!")
            agent.destroy(DOWN)
        }else{
            player.say("This seems to be a false alarm, the ground below the agent seems pretty stable... Try moving to a different location")
        }
    }
}
```

```ghost
player.say("")
agent.check_ground_unstable()
agent.alert()
agent.move(FORWARD, 1)
```

## 不安定な地面をテストする @showdialog

地面の不安定な区域が開いたので、エージェントを使ってブロックごとに安全かどうかチェックしてください。

鉱夫から、地面の一部が開いて沈んだと聞いています。彼は下の地面が不安定かもしれないと心配しており、（浮くことができる）エージェントを使ってブロックを一つずつチェックして安全かどうか確認してほしいと頼んでいます。

![Unstable ground](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/cover1.jpg)

## 地面をテストする

鉱夫が、下の地面が安全かどうかをチェックする特別な関数 ``||agent:agent.check_ground_unstable()||`` をエージェントに用意してくれました。

この関数は次のように返します：

- **True**  ：エージェントの下の地面が安定している場合。
- **False** ：エージェントの下の地面が不安定な場合。

**``||player:player.say()||`` を使って、エージェントの下の地面が安全かどうか確認してください。**
```spy
player.say(agent.check_ground_unstable())
```

## 警告する

鉱夫がエージェントに用意した 2 つ目の特別な関数は ``||agent:agent.alert()||`` です。

不安定な地面を見つけたら、このコードを実行してください。

**「if」文について学んだことを使って、不安定な地面が検出されたときに「alert()」を実行するプログラムを作成してください。**

```spy
if (agent.check_ground_unstable()){
    agent.alert()
}
```

## 砂利採掘場をスキャンする
``||agent:agent.move()||`` を追加して、エージェントを砂利区域でブロックごとに動かしてください。

**コードが実行されるたびにエージェントを **FORWARD**（前）に移動するようにコードを更新してください。**

## 砂利採掘場全体をスキャンする
コードが完成したら、各砂利ブロックをチェックして不安定なものがないか探してみてください。
