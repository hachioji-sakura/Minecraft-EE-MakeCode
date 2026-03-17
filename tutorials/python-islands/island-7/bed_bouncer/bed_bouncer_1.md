### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# ベッドバウンサー（Bed Bouncer）

## はじめに @showdialog
ベッドの上で跳ねるのは楽しいですよね？以下のプログラム用フローチャートに従って、次のことを行う Python プログラムを作成してください。

- プレイヤーがベッドの上でバウンドしているかチェックし、そうであれば  
    - 浮遊（Levitation）を付与する  
    - 再生（Regeneration）を付与する

下のフローチャートに従います。

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/Flowchart.png)

## パート 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_1.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

```python
```
プレイヤーが `BOUNCE`（バウンド）したときに呼び出される関数を作成してください。

## パート 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_2.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。*Next* を押して次のステップへ進みます。

```python
blocks.test_for_block(BED, player.position())
mobs.apply_effect(LEVITATION, mobs.target(NEAREST_PLAYER), 2, 1)
```

```ghost
def on_jump():
    if blocks.test_for_block(BED, player.position()):
        mobs.apply_effect(LEVITATION, mobs.target(NEAREST_PLAYER), 2, 1)
        mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 3, 2)

player.on_travelled(BOUNCE, on_jump)
```

プレイヤーがベッドの上でジャンプしている場合、最も近いプレイヤーに `LEVITATION` を付与してください。

上のコードは参考として役立ちます。

## パート 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_3.png)

フローチャートの黒い部分に対応するコードを書きます。行き詰まったらヒントを確認してください。

```python
```
`LEVITATION` を付与したあと、最も近いプレイヤーに `REGENERATION` を付与してください。
