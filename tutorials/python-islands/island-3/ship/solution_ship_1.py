# ホイッスルでエージェントをハッチのすぐ前のブロックに移動させる
# コードを実行する（ハッチの各列ごとに繰り返す）
for count in range(6):
    agent.move(FORWARD, 1)
    agent.place(DOWN)