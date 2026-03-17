### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 鉱山 - 2

## 坑道を探索する @showdialog

鉄を探して、古い坑道をエージェントで探索してください。

![Old mineshafts](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/mine_2.gif)

## 鉄を探す @showdialog

![Dark mineshaft](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/dark_mine.jpg)

本坑から分かれた古い坑道がいくつかあるようです。うわさでは、未探索の鉄の鉱床があるとか。

残念ながら、坑道の奥は暗くて何があるか見えません。エージェントを坑道の奥まで案内して、鉄があるか確認してみてはどうでしょう？

## エージェントにプログラムする

エージェントを使って、5 本の坑道をそれぞれチェックし、暗闇の奥に鉄鉱石があるか確認してください。あれば、採掘してください！

プログラムでは、以下のコマンドをそれぞれ少なくとも 1 回は使う必要があるでしょう。

- ``||agent:agent.move()||``
- ``||agent:agent.destroy()||``
- ``||agent:agent.inspect()||``

最後に、この任務では**ホイッスル**を使うことを忘れないでください！

## プログラムを書く
**エージェントが `IRON_ORE` を検出したら壊すプログラムを書いてください。ただし、他のブロックは壊さないように注意！**

プログラムができたら、上の実行ボタンを押してください。この任務を完了するには、5 本の坑道すべてを調べて、奥に鉄鉱石ブロックがある坑道を特定する必要があります。

```python
if agent.inspect(AgentInspection.Block, FORWARD) == IRON_ORE:
    player.say("This is iron ore")
```
```ghost
agent.destroy(FORWARD)
if (agent.inspect(AgentInspection.Block, FORWARD) == IRON_BLOCK){
    agent.destroy(FORWARD)
} else {
    player.say("Agent didn't find iron!")
}
```
