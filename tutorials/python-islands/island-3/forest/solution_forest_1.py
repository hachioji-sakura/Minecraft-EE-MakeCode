# 最下層の丸太を取り除く
agent.destroy(FORWARD)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
agent.destroy(RIGHT)
agent.move(FORWARD, 1)
agent.destroy(RIGHT)
agent.move(BACK, 1)

# 残りの木を取り除く
for i in range(12):
    agent.destroy(UP)
    agent.move(FORWARD, 1)
    agent.destroy(UP)
    agent.move(RIGHT, 1)
    agent.destroy(UP)
    agent.move(BACK, 1)
    agent.destroy(UP)
    agent.move(LEFT, 1)
    agent.move(UP, 1)
