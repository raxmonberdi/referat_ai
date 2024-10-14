import json

user_input = input("Ismingizni kiriting\t")

def new_user(user_input):
    temp = {
        "user_id": int,
        "limit":5
}

    new_user = temp
    new_user["user_id"] = user_input
    with open('data.json', "r+") as f:
        templates = json.load(f)
        
    templates["users"].append(new_user)


    with open('data.json', "w") as f:
        json.dump(templates, f)