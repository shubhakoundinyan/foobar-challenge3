#! /usr/bin/python

def answer(plaintext):

    #   Saves the values as a dictionary

    #   dict1 = {'a':"100000", 'b':"101000", 'c':"110000",'d':"110100",'e':"100100",'f':"111000",'g':"111100",'h':"101100",'i':"011000",'j':"011100"}

    #   Braille Inputs being defined below

    inputs = ["100000","110000","100100","100110","100010","110100","110110","110010","010100","010110"]
    
    #   The given input is saved
    
    a = []
    
    #   Stores the output
    #   Setting a flag to keep a check on capitalization

    set = 0
    
    a1 = []
    a = plaintext
    length = len(plaintext)
    for i in a:
        t1= i
        
        #   Checks for blanks
        
        if t1== " ":
            t2= "000000"
            a1.append(t2)
        else:

             #  Taking the alphabetical value for an alphabet i.e a = 1 , b = 2, etc.
             
             value = ord(t1)%32
             if t1=="w" or t1 =="W":
               if t1 == "W":
                       t2 ="000001"+"010111"
                       a1.append(t2)
                     
                     #  Print t2
               else:
                        t2 = "010111"
                        a1.append(t2)
             else:     
               if t1.isupper() == False and t1!="w":
                 if value>=1 and value<=10:
                     t2 =inputs[value-1]
                     
                     #  Print t2
                     
                     a1.append(t2)
                 elif value>=11 and value<=20:
                     t3= inputs[value-1-10]
                     t2 = t3[0:2]+'1'+t3[3:]
                    
                    #   Print t2
                     
                     a1.append(t2)
                 elif value>=20 and value<=26:
                     if value>=20 and value<=26:
                      t3 =inputs[value-1-20]
                      t2 =t3[0:2]+'1'+t3[3:5]+'1'
                      a1.append(t2)
                     elif value>=24 and value<=26:
                      t3 =inputs[value-1-20-1]
                      t2 =t3[0:2]+'1'+t3[3:5]+'1'
                      a1.append(t2)
                    
                    #   Print t2

               else:
                 if value>=1 and value<=10:
                     t2 ="000001"+inputs[value-1]
                     a1.append(t2)
                    
                    #   Print t2
                 
                 elif value>=11 and value<=20:
                     t3=inputs[value-1-10]
                     t2 = "000001"+t3[0:2]+'1'+t3[3:]
                     a1.append(t2)
                    
                    #   Print t2
                 
                 elif value>=20and value<=26:
                   if value>=20and value<=22:
                     t3 =inputs[value-1-20]
                     t2 ="000001"+t3[0:2]+"1"+t3[3:5]+'1'
                     a1.append(t2)

                   elif value>=24 and value<=26:
                     t3 =inputs[value-1-20-1]
                     t2 =t3[0:2]+'1'+t3[3:5]+'1'
                     a1.append(t2)
                    
                    #   Print t2
             
                  
    print ''.join(a1)

#   Print "Output:"
#   Print a1

answer("The quick brown fox jumped over the lazy dog")
