### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - 採掘

```template
agent
```

## 崖の上の石炭を採掘する @showdialog
崖の端から石炭を採掘しましょう！
ニコルとマーヴィンがこの石炭の鉱脈まで連れてきてくれました。鉱夫たちはここに到達できないので、エージェントを使って鉱石を採掘できますか？
![Cover image of coal for mine task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/mine/cover.png)

## エージェントを移動させる
石炭の隣にいるので、エージェントは飛んで行って、その前に立って採掘できるはずです。
石炭鉱石の前にエージェントを移動させるコードを書きましょう。

```python
agent.move(DIRECTION, BLOCKS)
```
## 石炭を採掘する @showdialog
エージェントが石炭鉱石の前にいることを確認してください。（下の画像と同様の位置）
![Agent in front of the coal](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/mine/agent_coal.png)


## 石炭を採掘する
これでブロックを採掘して石炭を集めることができます！
エージェントを使って、前の石炭ブロックを破壊しましょう。

```python
agent.destroy(DIRECTION)
```
- `DIRECTION`: エージェントが壊そうとする方向。使用できる方向は：前（FORWARD）、後ろ（BACK）、左（LEFT）、右（RIGHT）、上（UP）、下（DOWN）です。

## 残りを取得する
1つ完了、あと2つです！離れたい場合は、ニコルに話しかけてください。ただし、そうすると最初からやり直しになります。
終わったら、マーヴィンが地表まで飛んで戻り、鉱夫のところにあなたを降ろしてくれます。頑張ってください！
**最後の2つの石炭を採掘しましょう！**
