file_counts = {"Apple":1, "Banana":2, "Orange":3}
# print(file_counts)
for abc in file_counts:
    print(abc)

for ext, amount in file_counts.items():
    print("Key : {} ,Value: {} ".format(ext,amount))
