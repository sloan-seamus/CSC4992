class person():

    first_name = ""
    last_name = ""

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def __eq__(self, other):
        if self.first_name == other.first_name:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.last_name == other.last_name:
            return True
        else:
            return False


Me = person("Seamus", "Sloan")
Friend = person("Seamus", "NULL")

print(Me.__eq__(Friend))
