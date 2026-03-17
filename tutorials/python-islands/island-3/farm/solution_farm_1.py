# 各列ごとに1回実行する。ホイッスルでエージェントを各列の開始位置に呼ぶ
for i in range(0, 8):
    agent.move(FORWARD, 1)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destroy(DOWN)
        agent.place(DOWN)
    elif block == AIR:
        agent.place(DOWN)
