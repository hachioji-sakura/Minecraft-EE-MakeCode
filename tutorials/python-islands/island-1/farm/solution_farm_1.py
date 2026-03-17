# 最初のポイントに移動し、耕し、種を植えます。
agent.move(LEFT, 3)
agent.till(DOWN)
agent.place(DOWN)

# エージェントが最初のポイントから開始すると仮定して、2番目のポイントを処理します。
agent.move(RIGHT, 3)
agent.move(FORWARD, 1)
agent.till(DOWN)
agent.place(DOWN)

# エージェントが2番目のポイントから開始すると仮定して、3番目で最後のポイントを処理します。
agent.move(RIGHT, 4)
agent.move(FORWARD, 1)
agent.till(DOWN)
agent.place(DOWN)
