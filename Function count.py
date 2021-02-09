# Program to get the frequency of letters in a string

   
def most_frequent():
    user_string=input("Enter a word or string: ")
    user_string =user_string.casefold()
    d={}
    for i in user_string:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
    for key, values in d.items():
        print(key, values)
    print(d.keys())
    print(d.values())
    x=len(d)
    print("length of dictionary is : ", x)
    for i in range(0,x):
        for j in range(1,x):
             if d[i]>d[j]:
                   print(d[i])
                   del d[i]
           
       
def main():
    most_frequent()


if __name__=='__main__':
    main()


      
    
        
     
     
