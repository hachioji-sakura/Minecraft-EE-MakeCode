# エージェントを最初の丸石の上に配置する
agent.move(FORWARD, 1)

# 1列分の金をすべて取得する。その後ボタンをクリックしてエージェントを次の列に移動させ、コードを再実行する
for i in range(3):
    for dig in range(3):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        if agent.inspect(AgentInspection.BLOCK, DOWN) == GOLD_ORE:
            agent.destroy(DOWN)
    agent.move(UP, 3)
    agent.move(FORWARD, 2)