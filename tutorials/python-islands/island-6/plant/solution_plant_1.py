# 植物ごとに1回、計3回実行する。正しい情報を送信するとエージェントが自動的に移動する。
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(blocks.name_of_block(block))

hydration = scientist.get_hydration(block)
nutrition = scientist.get_nutrition(block)
strength = scientist.get_strength(block)

plant_info = [block, hydration, nutrition, strength]

scientist.submit(plant_info)

