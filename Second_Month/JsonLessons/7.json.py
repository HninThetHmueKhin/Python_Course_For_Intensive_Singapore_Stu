import json
person_list = []
with open("json_fake_data.json") as jsonFile:
    data = json.load(jsonFile)
    # print(data['name'])
    # print(type(data))
    # print(data['email'])
    # print(data['balance'])

    for item in data:
        name = item['name']
        email = item["email"]
        balance = item["balance"]

        person = {
            'new_name' : name,
            'new_email' : email,
            'new_balance' : balance
        }#dictionary
        person_list.append(person)

    print(person_list)

