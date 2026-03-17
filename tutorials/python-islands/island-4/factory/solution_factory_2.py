while agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR:
    # 上の while ループを完成させる
    # ステップ 1
    agent.move(FORWARD, 1)
    # ステップ 2
    while agent.inspect(AgentInspection.BLOCK, DOWN) == AIR:
        agent.move(DOWN, 1)
    # ステップ 3
    agent.collect_all()
    # ステップ 4
    while agent.get_position().get_value(Axis.Y) != 157:
        agent.move(UP, 1)
    # ステップ 5
    agent.set_slot(1)
    agent.place(DOWN)