# Dictionary syntax
band = {
    'vocals': 'plants',
    'guiter': 'page'
}

print(band)

# Access item
print(band["vocals"])
print(band.get("guiter"))

# List all items
print(band.keys())

# List of all key/value pairs as tuple
print(band.items())

# Verify a key exits
print("guiter" in band)
print("DJ" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove item
print(band.pop('bass'))
print(band)

band["drum"] = 'Bonham'

print(band.popitem())
print(band)

# Copy Dictionary
band2 = {}

band2 = band.copy()
band2["vocal"] = "Kingsley"
print(band2)

# Nested Dictionaries
member1 = {
    "name": "plant",
    "instrument": "vocals"
}
member2 = {
    "name": "page",
    "instrument": "guiter"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


# Delete and clear
band["drum"] = 'Bonham'

del band["vocals"]
print(band)

band.clear()
print(band)