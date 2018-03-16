from tkinter import*

root=Tk()
w=Label(root,text="My Program")
w.pack()


result= open("winner.txt","r+")
candfile=open("candidates.txt","r+")
voters=open("stud.txt","r+")
count=0
class addcand(object):
    l=[]
    def __init__(self,count,result,candfile,voters):
        self.name1=" "
        self.name2=" "
        self.cand_name="Candidate"
        self.standard='0'
        self.gender='gender'
        self.sign='00--'
        self.count=count
        self.candfile=candfile
        self.resultfile=result
        self.votersfile=voters
    def name(self):
        import time
        while True:
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                break
            else:
                time.sleep(1)
                self.name1=simpledialog.askstring("Name 1","What is your first name??")
                self.name2=simpledialog.askstring("Name 2","What is your last name??")
                self.cand_name=self.name1+" "+self.name2
                while True:
                    if self.name1.isalpha()==True and self.name2.isalpha()==True:
                        self.l.insert(0,self.cand_name.upper())
                        break
                    else:
                        messagebox.showinfo("Error", "Enter a name which only contains alphabets.")
                        self.name1=simpledialog.askstring("Name 1","What is your first name??")
                        self.name2=simpledialog.askstring("Name 2","What is your last name??")
                        self.cand_name=self.name1+" "+self.name2
                break
    def std(self):
        import time
        time.sleep(1)
        while True:
            self.standard=simpledialog.askinteger("Standard","Enter your standard.")
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                messagebox.showinfo("Error", "You are not eligible to contest. Only 9th and 11th are eligible.\n Sorry, you cannot contest")
                time.sleep(1)
                break
            elif self.standard in [11 ,9]:
                 self.l.insert(1,self.standard)
                 break
            else:
                messagebox.showinfo("Error","Enter a valid standard")
                
            
    def cgender(self):
        import time
        while True:
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                break
            else:
                time.sleep(1)
                self.gender=simpledialog.askstring("Gender","Enter your gender.\n f-for female\n m-for male")
                while True:
                    if self.gender.upper() not in ['M','F']:
                        messagebox.showinfo("Error","Enter a valid gender")
                        time.sleep(1)
                        self.gender=simpledialog.askstring("Gender","Enter your gender.\n f-for female\n m-for male")
                    else:
                        self.l.insert(2,self.gender.upper())
                        break
            break
    def psign(self):
        import time
        while True:
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                break
            else:
                time.sleep(1)
                self.sign=simpledialog.askstring("Symbol","Enter your Symbol.")
                self.l.insert(3,self.sign)
                break
    def display(self):
        import time
        while True:
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                break
            else:
                name="The details you have provided are:"
                name+="\n Name:"+self.cand_name
                name+="\n Standard:"+str(self.standard)
                name+="\n Gender:"+self.gender
                name+="\n Sign:"+self.sign
                messagebox.showinfo("Details",name)
                break
    def alter(self):
        import time
        while True:
            if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                break
            else:
                time.sleep(1)
                while True:
                    if self.standard in [1,2,3,4,5,6,7,8,10,12]:
                        self.l.remove(self.cand_name)
                        self.l.remove(self.gender)
                        self.l.remove(self.sign)
                        break
                    else:
                        messagebox.showinfo("Choice","If you want to proceed and save: press 0 \nIf you want to change one or more inputs, press 1")
                        choice=simpledialog.askstring("Choice","Enter your choice.")
                        if choice=='0':
                            break
                        elif choice!='0'and choice!='1':
                            messagebox.showinfo("Error", "Enter a valid choice:")
                            choice=simpledialog.askstring("Choice","Enter your choice.")
                        elif choice=="1":
                            messagebox.showinfo("Change","If you want to change the candidate name: press 1 \nIf you want to change the standard: press 2 \nIf you want to change gender: press 3\n If you want to change your sign: press 4")
                            change=simpledialog.askstring("Change","Enter your choice.")
                            if change=='1':
                                self.l.remove(self.cand_name.upper())
                                self.name()
                            elif change=='2':
                                self.l.remove(self.standard)
                                self.std()
                            elif change=='3':
                                self.l.remove(self.gender.upper())
                                self.cgender()
                            elif change=='4':
                                self.l.remove(self.sign)
                                self.psign()
                            else:
                                time.sleep(1)
                                messagebox.showinfo("Error","Enter a valid option")
                                time.sleep(1)
                                change=simpledialog.askstring("Change","Enter your choice.")
                                time.sleep(1)
                            self.display()
    
                break
    def temp(self):
        self.l.append(0)
        self.count+=1
        count= self.count
ml=[]
count=simpledialog.askinteger("Number Of Candidates","Enter number of candidates.")
obj=addcand(count,result,candfile,voters)
number="Number of candidates: "+str(count)
candfile.write(number)
candfile.write("\n")
for i in range(count):
    output="Hello Candidate "+ str(i+1)+" !! Please enter your details."
    messagebox.showinfo("Welcome",output)
    obj.std()
    obj.name()
    obj.cgender()
    obj.psign()
    obj.display()
    obj.alter()
    obj.temp()
    ml.append(addcand.l)
    addcand.l=[]
for i in range(count):
    cand="Candidate "+str(i+1)
    name="Name   : " +ml[i][0]
    std="Std    : "+str(ml[i][1])
    gen="Gender : "+ml[i][2]
    sym="Symbol : "+ml[i][3]
    candfile.write(cand )
    candfile.write("\n")
    candfile.write(name)
    candfile.write("\n")
    candfile.write(std)
    candfile.write("\n")
    candfile.write(gen)
    candfile.write("\n")
    candfile.write(sym)
    candfile.write("\n")
    candfile.write("\n")

candfile.close()
result.close()
voters.close()
