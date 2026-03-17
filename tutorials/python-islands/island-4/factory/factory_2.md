### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# 工場 - 2
飛行船を修理する

```template
while (agent == ) {
    // 上の while ループを完成させる
    // ステップ 1
    agent.move(FORWARD, 1)

    // ステップ 2
    while (agent.inspect(AgentInspection.BLOCK, DOWN) == AIR) {
        agent.move(DOWN, 1)
    }

    // ステップ 3
    agent.collect_all()

    // ステップ 4
    while (agent.get_position().get_value(Axis.Y) != 157) {
        agent.move(UP, 1)
    }

    // ステップ 5
    agent.set_slot(1)
    agent.place(DOWN)
}
```

## 飛行船の修理を自動化する
1 ブロックの修理を無事に案内できたので、前のコードを 1 つの大きな `while` ループにまとめて、残りの飛行船の修理を自動で行いましょう。

**外側の while ループを完成させ、FORWARD 方向の ``||agent:agent.inspect||`` が `"AIR"` と等しい間、外側の while ループが実行されるようにしてください。**
```python
agent.inspect(AgentInspection.BLOCK, DIRECTION)
```

- `DIRECTION`: エージェントがブロックを置く方向。使える方向は FORWARD、BACK、LEFT、RIGHT、UP、DOWN です。
