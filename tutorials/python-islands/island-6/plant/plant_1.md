### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 植物（Plant）

```customts
/**
 * 科学者
 */
//% color=purple weight=100 icon="\uf0c3" block="Scientist"
namespace scientist {
    /**
    * 植物の水分量を取得する
    */
    //% block
    export function getHydration(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "hydration 8"
        }
        
        if (plant == OAK_SAPLING) {
            return "hydration : 3"
        }
        
        if (plant == 32) {
            return "hydration : 0"
        }
        
        return "Unknown : 0"
    }

    /**
    * 植物の栄養価を取得する
    */
    //% block
    export function getNutrition(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "nutrition 4"
        }
        
        if (plant == OAK_SAPLING) {
            return "nutrition : 5"
        }
        
        if (plant == 32) {
            return "nutrition : 7"
        }
        
        return "Unknown : 0"
    }

    /**
    * 植物の強度を取得する
    */
    //% block
    export function getStrength(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "strength 3"
        }
        
        if (plant == OAK_SAPLING) {
            return "strength : 5"
        }
        
        if (plant == 32) {
            return "strength : 6"
        }
        
        return "Unknown : 0"
    }

    /**
    * 科学者が提供した情報をチェックする
    */
    //% block
    export function submit(answer: any[]) {
        let block = answer[0]
        if ([ORANGE_TULIP, OAK_SAPLING, 32].indexOf(block) < 0) {
            player.say("Hmmm, we aren't currently studying that...")
            player.say("Are you sure you are looking at the correct block?")
            return
        }
        
        let proof: any[] = [block, getHydration(block), getNutrition(block), getStrength(block)]

        if (answer[0] == proof[0] && answer[1] == proof[1] && answer[2] == proof[2] && answer[3] == proof[3]) {
            for (let e of answer) {
                player.say("Match")
            }
            player.say("Great! Matches perfectly...")
            blocks.place(DIAMOND_BLOCK, world(1054, 154, 139))
        } else if (answer.sort() == proof.sort()) {
            player.say("Hmmm, does not seem to be in the right order. Try again...")
        } else {
            player.say("Hmmm, information does not match up. Try again...")
        }  
    }
    
}
```

## 植物の処理 @showdialog

宇宙研究センターの科学者は、宇宙に送る正しい植物を選ぶ必要がある。エージェントに植物の性質を取得できる特別な装置が渡されている。宇宙で育つかどうかをチェックできる。

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/plant/cover.png)

## 下のブロックを調べる
**下方向のブロックを ``||agent:agent.inspect||`` で調べ、`block` という変数に格納してください。**

**次に ``||blocks:blocks.name_of_block(ID)||`` と ``||player:player.say||`` でブロック名を表示してください。**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(blocks.name_of_block(block))
```

## リスト @showdialog
Python では `my_list` というリストを次のように作れる：

```python
my_list = ["A", "B", "C", "D"]
```

リスト内の要素は角括弧で囲み、カンマで区切る。

変数をリストに入れることもできる。

## 科学者の関数 @showdialog
科学者が、特定の植物の情報を取得するために使える関数をいくつか用意している：

`||scientist:scientist.get_hydration(block)||`

`||scientist:scientist.get_nutrition(block)||`

`||scientist:scientist.get_strength(block)||`

いずれも引数にブロックを取る（``||agent:agent.inspect||`` で取得できる）。

## 水分・栄養・強度を取得する
**それぞれの関数が返す情報を格納した変数 `hydration`、`nutrition`、`strength` を作成してください。**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(blocks.name_of_block(block))

hydration = scientist.get_hydration(block)
nutrition = scientist.get_nutrition(block)
strength = scientist.get_strength(block)
```

## 植物の情報
**`block`、`hydration`、`nutrition`、`strength` をこの順で含むリストを作り、``||scientist:scientist.submit||`` で科学者の結果と照合してください。**

最初の植物の正しい情報が得られたら、他の 2 つもチェックするために使ってください。エージェントは自動的に移動する。

```python
plant_info = [...]

scientist.submit(plant_info)
```
