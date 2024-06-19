from knight import Knight

k1 = Knight('Arthur')
print(f"{k1.name = }")
print(f"{k1.title = }")
print(f"{k1.quest = }")

k2 = Knight("Lancelot")
print(f"{k2.name = }")
print(f"{k2.title = }")

winner = k1.joust(k2)
print(f"{winner = }")

winner = k2.joust(k1)
print(f"{winner = }")
