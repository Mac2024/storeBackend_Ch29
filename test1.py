

def run_test():
    print("Test 1 - dictionaries")


me = {
    "first": "Mario",
    "last": "McGrady",
    "age": 37,
    "hobbies": [],
    "address": {
        "street": "evergreen",
        "number": "22-B",
        "city": "springfield",
        "state": "CA",
        "zip": "92101"
    }
}


print(me)

print(me["first"])

# print full name
print(me["first"] + " " + me["last"])


# change values
me["age"] = me["age"] + 1
me["age"] = 99

# add new keys
me["preferred_color"] = "Gray"
print(me)

# read if exist
if "middle_name" in me:  # checks for existence
    print(me["middle_name"])

# print the full address on a single line
address = me["address"]
print("--------- address ---------")
print(address)
print(type(address))

print(f'{address["street"]} #{address["number"]}, {address["city"]}, {address["state"]}, {address["zip"]}')


run_test()
