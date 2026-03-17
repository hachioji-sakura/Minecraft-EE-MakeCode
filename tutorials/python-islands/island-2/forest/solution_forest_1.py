# 5回実行する（巣ごとに1回）
if agent.is_nest():
    agent.next_location()
else:
    agent.harvest()
    agent.next_location()
