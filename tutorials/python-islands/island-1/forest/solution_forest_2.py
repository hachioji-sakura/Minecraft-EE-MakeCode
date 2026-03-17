# エージェントの開始位置から移動し、最初のリンゴを取得します
agent.move(BACK, 2)
agent.move(DOWN, 1)
agent.move(LEFT, 3)
agent.destroy(UP)

# 上記のコードを実行した後のエージェントの位置（最初のリンゴの下）から移動し、2番目のリンゴを取得します
agent.move(LEFT, 2)
agent.move(FORWARD, 1)
agent.move(UP, 1)
agent.destroy(UP)

# 3番目のリンゴ
agent.move(FORWARD, 3)
agent.destroy(UP)

# 4番目のリンゴ
agent.move(RIGHT, 2)
agent.move(BACK, 1)
agent.destroy(UP)

# 5番目のリンゴ
agent.move(FORWARD, 4)
agent.move(UP, 1)
agent.destroy(UP)
