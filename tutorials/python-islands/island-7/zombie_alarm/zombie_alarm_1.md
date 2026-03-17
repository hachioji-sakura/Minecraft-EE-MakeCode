### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# ゾンビアラーム（Zombie Alarm）

## はじめに @showdialog

この演習では、下のフローチャートに従う Python プログラムを作成します。

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart.png)

ゾンビはいつでも厄介な存在です。この演習では、スポーンしたゾンビの存在をみんなに知らせるシステムを作りましょう！

以下のフローチャートに従って、次のような Python プログラムを作成します。

- ゾンビがスポーンしたかをチェックし、スポーンしていれば:
    - 雷のサウンドを再生する
    - すべてのプレイヤーにささやきメッセージを送る

## パート 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart-landscape_1.png)

フローチャートの黒い部分に対応するコードを書きます。

```python
def on_entity_spawned(mob, spawner):
    pass
events.on_entity_spawned(on_entity_spawned)
```

- モブがスポーンしたときに呼び出される関数を作成する

## パート 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart-landscape_2.png)

フローチャートの黒い部分に対応するコードを書きます。

```
```

- モブがゾンビであれば、雷のサウンドを再生し、チャットにメッセージを送る
- それ以外のモブのスポーンは無視する

```ghost
def on_entity_spawned(mob, spawner):
    if mob == ZOMBIE:
        music.play_sound(Sound.THUNDER)
        player.say("Zombie Spawned!")
events.on_entity_spawned(on_entity_spawned)
```

```package
events
music=github:microsoft/makecode-minecraft-music#v0.0.8
```