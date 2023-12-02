person = "Kingsley"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left. " % (person, coins)
print(message)

message = "\n{} has {} coins left. ".format(person, coins)
print(message)

message = "\n{0} has {1} coins left. ".format(person, coins)
print(message)

message = "\n{person} has {coins} coins left. ".format(person=person, coins=coins)
print(message)

player = {"person": "Kingsley", "coins": 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)



#############################
#F_STRING FORMAT
message = f"\n{person} has {coins} coins left. "
print(message)

message = f"\n{person} has {2 * 4} coins left. "
print(message)

message = f"\n{player['person']} has {2 * 4} coins left. "
print(message)



