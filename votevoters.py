from tkinter import*

root=Tk()
w=Label(root,text="My Program")
w.pack()

voters=open("stud.txt","r+")
class vote(object):
    def __init__(self,voters):
        self.vname=" "
        self.n=0
        self.id=000
        self.voteff=[]
        self.idl=[]
    def voter(self):
        self.n=simpledialog.askinteger("Number Of Students","Enter number of students(voters)")
        for i in range(self.n):
            name="Enter name of student "+ str(i+1)
            self.vname=simpledialog.askstring("Name",name)
            self.voteff.append(self.vname)
            self.id=simpledialog.askinteger("Name","ID no. of the student")
            self.idl.append(self.id)
obj=vote(voters)
obj.voter()
n="Number of voters: "+str(obj.n)
voters.write(n)
voters.write("\n")
for i in range(obj.n):
    vote=obj.voteff[i]+str(obj.idl[i])
    voters.write(vote)
    voters.write("\n")

voters.close()
