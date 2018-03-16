from tkinter import*

root=Tk()
w=Label(root,text="My Program")
w.pack()

name=[]
idno=[]
dvote={}
voters=open("stud.txt","r+")
voter=voters.readline()
voter=voter[18:]
for i in range(int(voter)):
    v=voters.readline()
    v=v.replace("\n","")
    temp=v
    for j in range(len(v),0,-1):
        if v.isalpha()==True:
            
            name.append(v)
            idn=temp[len(v):100]
            idno.append(idn)
            break
        else:
            v=v[0:j]
for i in range(len(name)):
    dvote[name[i]]=idno[i]

ml=[]
l=[]
cand=open("candidates.txt","r+")
count=cand.readline()
count=count[22:100]
count=int(count)
for i in range(count):
    for j in range(6):
        line=cand.readline()
        if line=="\n":
            s=" "+str(i+1)
            l.remove(s)
            l.append(0)
            ml.append(l)
            l=[]
            
        else:
            line=line.replace("\n","")
            line=line[9:100]
            l.append( line)
    
                 
class vote(object):
    def __init__(self,count,result,candfile,voters,ml,name,idno,dvote,voter):
        self.NOTA=0
        self.inv=0
        self.r=" "
        self.ml=ml
        self.n=voter
        self.w=0
        self.sums=0
        self.voteff=[]
        self.winner=[]
        self.name=name
        self.idno=idno
        self.count=count
        self.dvote=dvote
    def details(self):
        messagebox.showinfo("Choice","Press OK to see the List Of Candidates")
        fc=""
        for i in range(self.count):
            c= "Candidate "+str(i+1)+"\n"
            c+= "name: "+self.ml[i][0]+"\n"
            c+= "sign: "+self.ml[i][3]+"\n"
            fc+=c
        messagebox.showinfo("Candidates",fc)
    def cast(self):
        for d in range(int(self.n)):
            while True:
                messagebox.showinfo("Voting starts!!","Are you ready for voting??")
                name=simpledialog.askstring("Name","Enter your name")
                id=simpledialog.askstring("ID No","Enter your id number")
                if self.dvote.get(name)==id:
                    messagebox.showinfo("Eligible", "You are eligible to vote!!!")
                    self.dvote.pop(name)
                    messagebox.showinfo("Information","If you want to opt for NOTA, press 0")
                    ch=simpledialog.askstring("Your choice","Enter the sign for which you want to vote")
                    messagebox.showinfo("Thank you", "You have voted successfully!!!")
                    for i in range(self.count):
                        if ch in ml[i]:
                            self.ml[i][4]+=1
                            self.r=self.ml[i][3]
                    if ch=='0':
                        self.NOTA+=1
                    elif ch!=self.r:
                        self.inv+=1
                        messagebox.showinfo("Invalid Voting","You have casted an invalid vote")
                    break
                else:
                    messagebox.showinfo("Something's not right","Username or id is incorrect!!")
                    
                    
    def fsum(self):
        for i in range(self.count):
            self.sums+=self.ml[i][4]
        fr="The total number of votes casted for candidates : "+str(self.sums)
        fr+="\nThe number of NOTA : "+str(self.NOTA)
        fr+="\nThe number of invalid votes : "+str(self.inv)
        self.w=max(map(lambda x: x[4], self.ml))
        p=""
        for i in range(self.count):
            p+="The pecentage of votes for candidate "+self.ml[i][0]+" = "+str((int(self.ml[i][4])*100)/int(self.n))+"%\n"
            if self.w in self.ml[i]:
                self.winner=self.ml[i]
        w="The winner is:"
        w+="\nName: "+self.winner[0]
        w+="\nStd : "+str(self.winner[1])
        w+="\nNumber of votes: "+str(self.winner[4])
result=open("winner.txt","r+")
obj=vote(count,result,cand,voters,ml,name,idno,dvote,voter)
obj.details()
obj.cast()
obj.fsum()

totno="The total number of votes casted for candidates : "+str(obj.sums)
nota="The number of NOTA : "+str(obj.NOTA)
invv="The number of invalid votes : "+str(obj.inv)
result.write(totno)
result.write("\n")
result.write(nota)
result.write("\n")
result.write(invv)
result.write("\n")
result.write("\n")
for i in range(obj.count):
    per="The pecentage of votes for candidate "+obj.ml[i][0]+" : "+str((int(obj.ml[i][4])*100)/int(obj.n))+"%"
    result.write(per)
    result.write("\n")
    if obj.w in obj.ml[i]:
        obj.winner=obj.ml[i]
result.write("\n")
result.write("The winner is:")
result.write("\n")
winname="Name: "+obj.winner[0]
winstd= "Std : "+str(obj.winner[1])
winvot="Number of votes: "+str(obj.winner[4])
result.write(winname)
result.write("\n")
result.write(winstd)
result.write("\n")
result.write(winvot)
result.write("\n")

cand.close()
result.close()
voters.close()

