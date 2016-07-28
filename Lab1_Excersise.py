# Write a python script that reads in the names of your group members and the theme of their projects and
# saves this information into a text file called GroupMembers.txt


class MyGroup:
    """Group member names and projects"""

    members = {}

    def __init__(self):
        pass

    def add(self, name, project):
        self.members[name] = project

    def remove(self, name):
        del self.members[name]

    def save(self, filename):
        f = open(filename, 'a')
        for m, p in self.members.items():
            f.write("Name: " + m + " Project: " + p + '\n')
        f.close()

myGroup = MyGroup()

for i in range(0, 4):
    name = raw_input("Name " + str(i) + ":")
    project = raw_input("Project Theme " + str(i) + ":")
    myGroup.add(name,project)

myGroup.save('GroupMembers.txt')
