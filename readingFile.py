import json

with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)

print("Нэр:", user["нэр"])
print("Имэйл:", user["имэйл"])