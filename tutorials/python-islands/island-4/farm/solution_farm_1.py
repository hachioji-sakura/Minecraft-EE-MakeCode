# 1列分のヒナゲシをすべて取得するために実行する
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
    if agent.check_flower(DOWN) == POPPY:
        agent.destroy(DOWN)

# エージェントを次の列に移動させる（LEFT を RIGHT に変える必要がある場合あり）
agent.turn_left()
agent.turn_left()
agent.move(LEFT, 1)