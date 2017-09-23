classmates={'Tony':"Cool but smells",'Emma':"She does the job",'Lucy':"She goes deep"} #classmates is a dictionary with keys and value, eg Tony is a key and its value is Cool  but smells
print(classmates)#notice that the curly brackets are also printed
print(classmates['Emma'])#Emmas value is printed

for k,v in classmates.items(): #notce the use of two variable k,v for keys and values and also calling the function items()
    print(k+"",v)

word="Avash"
word_count={}
word_count[word]=1
word_count["Bishal"]=2
print (word_count)
