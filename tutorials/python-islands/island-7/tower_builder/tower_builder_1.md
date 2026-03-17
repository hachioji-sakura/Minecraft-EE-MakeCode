### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# タワービルダー（Tower Builder）

```customts
agent.teleport(world(-517, 139, 712), WEST)
let agent_or = agent.getOrientation()
if (agent_or == EAST) {
    agent.turnLeft()
    agent.turnLeft()
}

if (agent_or == SOUTH) {
    agent.turnRight()
}

if (agent_or == EAST) {
    agent.turnLeft()
}
```

```template
function create_layer(): void{

}
```

## はじめに @showdialog

探検家として、基地に戻るために自分の足跡をたどれることは重要です。この演習では、2 つのフローチャートに従って塔を作る Python プログラムを作成します。

- 1 つ目のフローチャートは、1 層分の塔を作る関数を示しています。  
- 2 つ目のフローチャートは、この関数を使って塔を積み上げ、塔の頂上にグロウストーンを配置します。

### レイヤー関数

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-function.png)

### メインフローチャート

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart.png)

## 関数 - パート 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_1.png)

黒いボックスに一致するように、用意された関数を定義します。

```python
def create_layer():
    for i in range(4):
        pass
```

- `create_layer` という名前の関数の中で、**4 回ループする** for ループを作成してください。

## 関数 - パート 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_2.png)

フローチャートに合うように、関数の中のループにコードを追加してください。

```
```

- 石（スロット 1）を下に置く  
- エージェントを前に動かす

## 関数 - パート 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_3.png)

フローチャートに合うように、関数の中のループにさらにコードを追加してください。

```
```

- 石（スロット 1）を下に置く  
- エージェントを前に動かす  
- エージェントを右に回転させる

## メインコード - パート 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_1.png)

作成した関数の下に、フローチャートの黒い部分に対応するコードを書いてください。

```
```

- エージェントに石を 64 個（スロット 1）渡す  
- エージェントにグロウストーンを 1 個（スロット 2）渡す

## メインコード - パート 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_2.png)

黒い部分に示されたループを作成してください。

```
```

- 塔の高さ（3 段）ぶん、3 回ループするループを作成する。

## メインコード - パート 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_3.png)

黒い部分に示されたコードでループを完成させてください。

```
```

- エージェントを 1 ブロック上に移動させる  
- 先ほど作成した関数を実行する

## メインコード - パート 4

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_4.png)

塔の頂上にグロウストーンを置くために、フローチャートの黒い部分に対応するコードを書いてください。

```
```

- エージェントを右に移動させる  
- アクティブなスロットを 2 に設定する  
- 前方にグロウストーンを置く

```ghost
def create_layer():
    agent.set_slot(1)
    for sides in range(4):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.turn_right()

agent.set_item(STONE, 64, 1)
agent.set_item(GLOWSTONE, 1, 2)

for i in range(3):
    agent.move(UP, 1)
    create_layer()

agent.move(RIGHT, 1)
agent.set_slot(2)
agent.place(FORWARD)
```
