data = open("randomDataRAW.txt","r");

dataString = data.read()

dataList = dataString.split("\n")



for i in range(0, len(dataList),1):
    #Big Skill: Casting
    dataList[i] = dataList[i].replace(",","")
    dataList[i] = float(dataList[i])

print (dataList)

