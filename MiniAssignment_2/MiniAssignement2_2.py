list1 = ["HELLO", "TAKE"]
list2 = ["DEAR", "SIR"]

list3 = []

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        list3.append(list1[i] + list2[j])

print(list3)
