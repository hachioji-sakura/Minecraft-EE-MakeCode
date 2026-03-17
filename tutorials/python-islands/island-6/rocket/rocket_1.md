### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# ロケット
打ち上げ準備ができているかロケットをチェックする

```template
let accepted_blocks = [COAL_BLOCK, CONCRETE, GRAY_STAINED_GLASS, BLOCK_OF_QUARTZ, QUARTZ_STAIRS, IRON_BARS];

let block = agent.inspect(AgentInspection.Block, FORWARD);

if () {
    // 上の if 文を完成させる
    player.say("Accept")
    agent.accept()
}
```

```customts
namespace agent {
    /**
    * 科学者向けにブロックを承認としてマークする
    */
    //% block
    export function accept(): void {
        agent.setSlot(1);
        agent.place(BACK);
    }

    /**
    * 科学者向けにブロックを却下としてマークする
    */
    //% block
    export function deny(): void {
        agent.setSlot(2);
        agent.place(BACK);
    }
}
```

## ロケットの修理 @showdialog

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/rocket/cover.png)
ロケットにひびがないかチェックする必要がある！エージェントを使って、損傷やひびのあるブロックがないか調べてください。あれば修理の印をつけてください。

## リストのチェック @showdialog

エージェントの前のブロックが、科学者がエージェントに渡した `accepted_blocks` のリストに含まれているか確認する必要がある。これらのブロックが、各ブロックの許容される状態だ。

キーワード `in` を使うと、各ブロックを簡単にチェックできる。

`in` で、ある値が**リストに含まれているか**をチェックできる。含まれていれば `True` を返す。例：

```python
my_list = ["A", "B", "C", "D"]
if "B" in my_list:
    say("True!") # "B" は my_list に含まれるので "True!" と表示される
```

## ステップ 1
**`block` が `accepted_blocks` リストに「含まれている」（in）かチェックする if 文を、'in' キーワードで完成させてください。**

`||logic:if item in list:||`

```python
if block in accepted_blocks:
    player.say("Accept")
    agent.accept()
```


## ステップ 2
承認ブロックに印をつけて科学者に知らせたので、次は却下ブロックに注目しよう。

**`||player:player.say("Deny")||` と `||agent:agent.deny()||` を使った else 文をコードに追加してください。**

```python
if block in accepted_blocks:
    player.say("Accept")
    agent.accept()
else:
    player.say("Deny")
    agent.deny()
```

## ステップ 3
コード全体をまとめるために、エージェントの上にある各ブロックをチェックする `for` ループを使う。科学者によるとロケットの高さは 26 ブロックだ。

**「if else」文とブロックの検査を、`||loops:for||` ループで囲んでください。ループの最後で ``||agent:agent.move||`` でエージェントを「UP」（上）に 1 ブロック移動させる。エージェントがロケットの頂上に着くまで（26 回）ループするようにしてください。**

```python
for i in range(26):
    player.say("Looping 26 times.")
```

```ghost
agent.move(UP, 1)
```

```ghost
agent.accept()
agent.deny()
```
