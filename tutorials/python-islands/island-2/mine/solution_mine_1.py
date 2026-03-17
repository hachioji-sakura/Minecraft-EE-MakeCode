# エージェントが不安定な地面を検出するまで複数回実行する
if agent.check_ground_unstable():
    agent.alert()
agent.move(FORWARD, 1)

