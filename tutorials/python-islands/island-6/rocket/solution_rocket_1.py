accepted_blocks = [COAL_BLOCK,
    CONCRETE,
    GRAY_STAINED_GLASS,
    BLOCK_OF_QUARTZ,
    QUARTZ_STAIRS,
    IRON_BARS]
for i in range(26):
    block = agent.inspect(AgentInspection.BLOCK, FORWARD)
    if block in accepted_blocks:
        # 上の if 文を完成させる
        player.say("Accept")
        agent.accept()
    else:
        player.say("Deny")
        agent.deny()
    agent.move(UP, 1)