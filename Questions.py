class Question:
    def Question(self):
       questionList=[]
       def getQuestion(i):
           return questionList[i]
       def setQuestion(i,data):
           questionList[i]=data
       def add(data):
           questionList.append(data)
           print(f"{data} added to tests data base")
       def remove(i):
           print(f"{questionList.pop(i)} removed")
       def view():
           print(questionList)
