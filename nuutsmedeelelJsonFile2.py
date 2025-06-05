import json

user = {
    "нэр": "Tuvshin",
    "имэйл": "tuvshin@example.com",
    "нууц_үг": "minii_nuuts"
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=4)
