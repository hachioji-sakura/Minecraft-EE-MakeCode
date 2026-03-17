### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0
### @explicitHints true

# アイスウォーカー（Ice Walker）

```customts
const LAKE_WATER = 9
```

## はじめに @showdialog

この演習では、下のフローチャートに従う Python プログラムを作成します。

Minecraft では、広大な湖や海を横断する必要がよくあります。以下のフローチャートに従って、次のような Python プログラムを作成してください。

- 永続的にループする  
- プレイヤーの周囲のブロックを LAKE_WATER から ICE に変える

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)


## Ice Walker

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)

足元だけでなく、プレイヤーの周囲のブロックも ICE に設定する必要があります。  
`||positions:pos||` を使って、自分を基準にした相対座標を使用してください。

**注意：足元のまわりに ICE の箱（-1 ～ 1 の座標）を作る必要があります。`blocks.replace` メソッド内の座標ペアを変更する必要があります（詳しくはヒントを参照）。**

### ~ tutorialhint
**ヒント**
- 注意！`blocks.replace` メソッドは、新しいブロック（ICE）、次に置き換え対象の古いブロック（LAKE_WATER）の順で指定します。
- どの座標を使えばよいか分からない場合は、下の図を確認してください。
![Player coords](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/player_coords.jpg)

**スターターコード**
```python
def on_forever():
    # ここにコードを書く
    pass
loops.forever(on_forever)
```



```ghost
def on_forever():
    blocks.replace(ICE,
        blocks.block_by_id(LAKE_WATER),
        pos_camera(-1, -1, -1),
        pos_camera(1, -1, 1))
loops.forever(on_forever)
```
