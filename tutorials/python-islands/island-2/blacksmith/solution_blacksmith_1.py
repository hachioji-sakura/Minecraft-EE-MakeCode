# 5回実行する（鉄ブロックごとに1回）
if blacksmith.purity(FORWARD) <= 3:
    blacksmith.deny()
else:
    blacksmith.accept()