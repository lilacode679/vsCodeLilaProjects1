import json
user = {
    "нэр": "Tuvshin",
    "имэйл": "tuvshin@example.com",
    "нууц_үг": "minii_nuuts"
}

print(json.dumps(user, ensure_ascii=False, indent=4))