# This is LIST Topic

nameList = ['Omer','Ali','Khan','Bilal','Zafar']
# print(nameList)
# print(nameList[0])
# print(nameList[::-1])
newName = "Jamal"
nameList.append(newName)
# print(nameList)
for index,name in enumerate(nameList):
    # print(f"At {index} name is: {name}")
    if name == "Bilal":
        pass
        # print(f"Reverser name is {name[::-1]}")



listOne = ["A","B","C","D","E"]
listTwo = ["F","G","H","I","J"]
# print(listOne+listTwo)
listOne.insert(2,'CCCC')
# print(listOne)
nums = [1,2,34,4,5,6,7,8,89,989]
print(min(nums))
print(max(nums))
