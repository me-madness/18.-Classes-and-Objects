# First task from the lecture

class Email:
    def __init__(self, sender, receiver, content):
       self.sender = sender
       self.receiver = receiver
       self.content = content
       self.is_sent = False
 
    def send(self):
        self.is_sent = True
        
        
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
    

info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    
    info = input()
    
    
            
## Input one
# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2

## Input two
# Anna, Bella, Hi
# Sam, Dany, Okey
# Felix, Mery, Bye
# Stop
# 0



# Second task from me
