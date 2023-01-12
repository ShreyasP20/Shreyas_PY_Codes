listDir = []
listFiles = []

class Composite:

    def __init__(self, data):
        self.data = data
        self.child = []


class Leaf:

    def __init__(self, data):
        self.data = data
        self.read = False
        self.write = False
        self.exec = False


def NewLeaf(key):
    temp = Leaf(key)
    return temp


def NewComposite(key):
    temp = Composite(key)
    return temp


def NewFile(root, F_name):
    Ch = input("Do you want to add the File in {} directory? (y/n): ".format(root.data))
    if Ch == 'y':
        NewFile = NewLeaf(F_name)
        root.child.append(NewFile)
        print("File Permissions are:\nRead:{}  Write:{}  Execute:{} ".format(
            NewFile.read, NewFile.write, NewFile.exec))
        change = input(
            "Do you want to change File permissions? \n1.Read\n2.Write\n3.Execute\n4.None")
        if change == '1':
            NewFile.read = True
        elif change == '2':
            NewFile.write = True
        elif change == '3':
            NewFile.exec = True
        print("\nFile Permissions are:\nRead:{}  Write:{}  Execute:{} ".format(
            NewFile.read, NewFile.write, NewFile.exec))
        return
    else:
        print("Available directories are:")
        for i in root.child:
            if i in listDir:
                print(i)
        child_name = input(
            "Enter The name of Directory you want to add the File{}: ".format(F_name))
        for i in root.child:
            if i == child_name:
                print("Entering Directory {}".format(child_name))
                NewFile(i, F_name)


def Directory(root, Dir_name):
    Ch = input(
        "Do you want to add the Directory in {} directory? (y/n): ".format(root.data))
    if Ch == 'y':
        NewDir = NewComposite(Dir_name)
        root.child.append(NewDir)
        return
    else:
        print("Available directories are:")
        for i in root.child:
            if i in listDir:
                print(i)
        dir_name = input("Enter the name of Directory you want to add: ")
        for i in root.child:
            if i == Dir_name:
                print("Entering Directory {}".format(Dir_name))
                Directory(i, Dir_name)


def RemDir(root,Dir_name):
    if Dir_name in root.child:
        in1=input("Do you want to remove the Directory{} in {} directory? (y/n): ".format(Dir_name,root.data))
        if in1 == 'y':
            print("Removing Directory {}".format(Dir_name))
            root.child.remove(Dir_name)
            return
    else:
        print("Available directories are:")
        for i in root.child:
            if i in listDir:
                print(i)
        dr=input("Enter the Directory to be searched:")
        if dr in root.child:
            RemDir(root.child.index(dr),Dir_name)
        else:
            print("Enter A Valid Directory Name")
             
def RemFile(root,F_name):
    if F_name in root.child:
        in1=input("Do you want to remove the Directory{} in {} directory? (y/n): ".format(F_name,root.data))
        if in1 == 'y':
            print("Removing Directory {}".format(F_name))
            root.child.remove(F_name)
            return
    else:
        print("Available directories are:")
        for i in root.child:
            if i in listDir:
                print(i)
        dr=input("Enter the Directory to be searched:")
        if dr in root.child:
            RemFile(root.child.index(dr),F_name)
        else:
            print("Enter A Valid Directory Name")    
             
if __name__ == "__main__":
    root = Composite('/')
    listDir.append(root)
    Cont= True
    while(Cont == True):
        New1 = input(
            "Do You Want To Create a New Directory or a New File? \n1.File \n2.Directory ")
        if New1 == "1":
            F_name = input("Enter the name of the file to be created: ")
            if F_name in listFiles:
                print("File already exists")
            else:
                listFiles.append(F_name)
                NewFile(root, F_name)

        elif New1 == "2":
            Dir_name = input("Enter the name of the file to be created: ")
            if Dir_name in listDir:
                print("Directory already exists")
                exit()
            else:
                listDir.append(Dir_name)
                Directory(root, Dir_name)
        New2 = input("Do You Want To Delete a Directory or a File? \n1.Directory \n2.File ")
        if New2 == "1":
            Dir_name = input("Enter the name of the directory to be deleted: ")
            if Dir_name in listDir:
                listDir.remove(Dir_name)
                RemDir(root,Dir_name)
            else:
                print("Directory does not exist")
        elif New2 == "2":
            F_name = input("Enter the name of the file to be deleted: ")
            if F_name in listFiles:
                listFiles.remove(F_name)
                RemFile(root,F_name)
            else:
                print("File does not exist")
        Choice = input("Do You Want To Continue? \n1.Yes \n2.No")
        if Choice == "1":
            Cont = True
        elif Choice == "2":
            Cont = False