### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Python Islands 1 - 農業

```template
// Add your code below
agent
```

## 農業の紹介 @showdialog
エージェントを使って、農夫が地面を耕し、種を植えるのを手伝いましょう。農夫はすでにエージェントのインベントリに種を入れてくれています！

![Farming](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/farm/farm.jpg)

## エージェントを適切な位置に移動する
農夫は畑の上に3つのマーカーを設置して、どこを耕すべきか示してくれています。
`||agent:agent.move(DIRECTION, 1)||`を使って、エージェントをマーカーの1つまで移動させましょう。   
上記の`1`を移動したいブロック数に変更することを忘れないでください。
```python
agent.move(LEFT, 3)
```


## 必要な場所を耕す
耕すことで、通常の土を準備して種を育てられるようになります。エージェントを土ブロックの上に浮かせたら（`||agent:agent.move(FORWARD)||`を使用）、それを耕す必要があります。
エージェントを使って土を耕すには、`||agent:agent.till(DIRECTION)||`を使用します。


```python
agent.move(LEFT, 3)
agent.till(DOWN)
```

## 種を植える
地面が耕されたので、マーカーが白色に変わったのが見えるはずです。  
次に、`||agent:agent.place(DIRECTION)||`を使って種を植える必要があります。


```python
agent.move(LEFT, 3)
agent.till(DOWN)
agent.place(DOWN)
```

## 残りの種を植える
種を1つ植えたので、残りの2つの種を植えて作業を完了させましょう。  
農夫が設置したマーカーを探してみてください。
