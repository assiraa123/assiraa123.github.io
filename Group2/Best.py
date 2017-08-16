grade=[]
while 1==1:
    score = input("Enter a score")
    if score >=80 and score <=100:
            grade="A" 

           
    elif score >=70 and score <=79:
           grade+=  "B"
        
    elif score >=60 and score <=69:
        grade+= "C"
        
    elif score >=50 and score <=59:
        grade+= "D"
       
    elif score >=45 and score <=49:
        grade+="E"
        
    else:
        grade+= "F"
 
    stop=raw_input("Do you want to stop?")    
    if stop == "yes":
        print"Bye, have a nice day "
        break
    print "Your grades were :"
    print grade