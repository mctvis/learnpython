def get_gender(sex='Unknown'): #default value for sex argunment.If no value is passed then 'unknown will be used'
    if sex is 'm':
        sex="Male"
    elif sex is 'f':
        sex="Female"
    print (sex)
get_gender('m')#sex takes m
get_gender('f')#sex takes f
get_gender()#no argument passed sex takes 'Unknown value'


