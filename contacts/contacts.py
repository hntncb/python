import json

data = [
    {
        "name": "nam1",
        "phone": "0748234"
    },
    {
        "name": "nam2",
        "phone": "1234567"
    }
]
def contacts_white(data):
    with open('contacts/contacts.json', 'w') as file:
        json.dump(data,file)
        print("ghi file thành công")

def contacts_read():
    data = []
    with open('contacts/contacts.json','r') as file:
        data = json.load(file)
    return data

contacts_white(data)
read_data = contacts_read()
print("========Danh Bạ=========")
for contact in read_data:
    print(contact["name"] + ":" + contact["phone"])