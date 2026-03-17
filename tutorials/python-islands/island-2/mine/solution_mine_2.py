# 坑道の入口まで歩く（Shiftでしゃがんで中に入る）
# ホイッスルでエージェントを呼ぶ
# 以下のコードを実行する（他の坑道でも繰り返す）
agent.move(FORWARD, 4)
if agent.inspect(AgentInspection.BLOCK, FORWARD) == IRON_ORE:
    agent.destroy(FORWARD)