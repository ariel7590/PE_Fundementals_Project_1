class Test:
    def Test(self):
       testList=[]
       def getTest(i):
           return testList[i]
       def setTest(i,data):
           testList[i]=data
       def add(data):
           testList.append(data)
           print(f"{data} added to tests data base")
       def remove(i):
           print(f"{testList.pop(i)} removed")
       def view():
           print(testList)
