### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - 森 1

```template
agent
```

## 木に登る @showdialog
エージェントを使って、壊れたはしごを修復し、木のてっぺんから出ている煙を調査しましょう。   

エージェントはすでにはしごを装備しています。   

![Cover Image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/cover.png)

## エージェントをはしごまで移動させる
まず、`||agent:agent.move(DIRECTION, BLOCKS)||`を使ってエージェントをはしごまで移動させる必要があります。
```python
agent.move(FORWARD, 1)
```

## はしごを修復する
これで、木の上のはしごを修復する準備ができました。
ブロックを配置するには、`||agent:agent.place(DIRECTION)||`を使用できます。 
`||agent:agent.place||`を追加して、エージェントの前（`FORWARD`）にはしごを配置しましょう。
```python
agent.move(FORWARD, 1)
agent.place(FORWARD)
```

## 残りを修復する
最初のはしごを置き換えたので、上にもう1つ欠けているはしごがあるようです...
`||agent:agent.move||`と`||agent:agent.place||`を使って2番目のはしごを置き換えて、道を完成させましょう。

## 完了
これではしごを登って、煙を調査しましょう！
