# エージェントを移動させ、最初の石炭を破壊します。
agent.move(UP, 2)
agent.move(LEFT, 1)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)

# 最初の石炭の前から、エージェントを2番目の石炭の前に移動させ、破壊します。
agent.move(RIGHT, 2)
agent.move(DOWN, 1)
agent.destroy(FORWARD)

# 3番目の石炭。
agent.move(DOWN, 2)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
