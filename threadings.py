#Break up a program and do multiple task at a same time
#eg in messenger-sending messages and listening for messages
import threading
class Messenger(threading.Thread):
    def run(self):#overrding run method of Thread class from threading library #function name must be 'run' .. this is specific.  this function gets called
        for _ in range(100): #just loop ten times .. ie dont use variable
            print(threading.current_thread().getName()) #current_thread() reutrns an object(current object)

x=Messenger(name='Send out Messages')#name represnts name of the thread which is a keyword argument which is call in Thread class of threading library
y=Messenger(name='Receive messages') ##these two objects can run at a same time
x.start() #actually start goes to run()
y.start()



