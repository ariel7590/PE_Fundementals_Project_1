def answer_type(a_type):
    if a_type:
        return "Full Answer"
    else:
        return "Final Answer"


def answer(answerable):
    if answerable:
        return True
    else:
        return False


def is_from(check):
    if check:
        print("The question is from a Test")
    else:
        print("The question is from a Quiz")


def semester(a_semester):
    print(f"The test is from semester {a_semester}")


def format_of(a_format):
    if a_format == ".doc":
        return "Word"
    elif a_format == ".pdf":
        return "PDF"
    elif a_format == "pptx":
        return "PowerPoint"


def questionList(args):
    pass


class Question:
    """This class identifies Questions"""

    def __init__(self, subject, sub_subject, difficulty, is_from, semester, format_of, answer, answer_type):
        self.questionList = []
        self.subject = subject
        self.sub_subject = sub_subject
        self.difficulty = difficulty
        self.is_from = is_from
        self.semester = semester
        self.format = format_of
        self.answer = answer
        self.answer_type = answer_type

    def getQuestion(i):
        return i.questionList[i]

    def setQuestion(i, data):
        i.questionList[i] = data

    def add(data):
        data.questionList.append(data)
        print(f"{data} added to tests data base")

    def remove(i):
        print(f"{i.questionList.pop(i)} removed")

    def view(self):
        print(self.questionList)

    def subject(self):
        print(f"The category of the questions is : {self.subject}")

    def get_subject(self):
        return self.subject

    def set_subject(self, new_subject):
        self.subject = new_subject

    def sub_subject(self):
        print(f"The sub category of the question is : {self.sub_subject}")

    def get_sub_subject(self):
        return self.sub_subject

    def set_sub_subject(self, new_sub_subject):
        self.sub_subject = new_sub_subject

    def difficulty(self):
        print(f"The rank of the question is : {self.difficulty}")

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty

    def get_is_from(self):
        return self.is_from

    def set_is_from(self, changes):
        self.is_from = changes

    def get_semester(self):
        return self.semester

    def set_semester(self, changes):
        self.semester = changes

    def get_format_of(self):
        return self.format

    def set_format_of(self, new_format):
        self.format = new_format

    def get_answer(self):
        return self.answer

    def set_answer(self, new_answer):
        self.answer = new_answer

    def get_answer_type(self):
        return self.answer_type

    def set_answer_type(self, new_type):
        self.answer_type = new_type
