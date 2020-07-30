import sys
class Prime():

    print( "NO",len(sys.argv))
    def isMode(self,num,compare):
        print(f"{num}%{compare}")
        if(num%compare==0):
                return True

    def isPrime(self,num):
        if(num<=1):
            return False
        elif(num == 2):
            return True
        elif(self.isMode(num,2)):
            return False
        else:

            for i in range(3,num):
                check=False
                if(self.isMode(num,i)):
                    return False
                else:
                    check= True
            return check
    
pm= Prime()
print(pm.isPrime(int(str(sys.argv[1]))))

        
