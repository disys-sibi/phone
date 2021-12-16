class Addcontacts:
    
    def __init__(self):
        print("ADD CONTACTS")
        self.phno=input("Enter the Phone No:")
        self.name=input("Enter the name :")
        self.ringtone=input("Set ringtone :")
        #self.firsttransaction=happy

    def opencontacts(self):
        print("new contact")

     
    def phonenumber(self):
         if (len(self.phno)==10):
             print("phonenumber verified")
         else:
             raise ValueError("incorrect phno")



    def username(self):
         if type(self.name)==str:
             if len(self.name)<=20:
                 print("name verified")
             else:
                 raise ValueError("name is not valid")
         else:
             raise TypeError("the printed name cannot be used")



    def ringtune(self):
        if (type(self.ringtone)==str):
            print("ringtone set")
        else:
            raise ValueError("not set the ringtone")


        

jeni=Addcontacts()
jeni.opencontacts()
jeni.phonenumber()
jeni.username()
jeni.ringtune()        
