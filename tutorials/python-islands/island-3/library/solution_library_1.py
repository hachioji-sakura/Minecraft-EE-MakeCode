# 本棚の各列ごとに実行する。ホイッスルで列の間を移動できる
for i in range(5):
    if agent.check_book_on_shelf(FORWARD) == True:
        player.say("Found the book!")
        agent.mark_book(FORWARD)
    else:
        player.say("No book here!")
    agent.move(UP, 1)