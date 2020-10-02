"""
# A Very Fast Implementation for prime number generator..
Author : Satyam Rai
Example usage:
    1. primeGenerator(n) -> returns a generator object that goes through n numbers..
    2. primeGenerator() same as primeGenerator(0) -> returns a gen obj that goes through all prime numbers (almost infinite) 
    3. primeGenerator(lessThan = k) -> returns a gen object that produces all primes less than k.
"""



def primeGenerator(no = 0,lessThan = None ):
    """A prime numbers iterator \n
        no: int  -> Returns $no number of  primes  (if 0 => inf)
        lessThan : int -> returns all primes lessthan $lessThan
        if ($n == 0 and $lessThan is valid ) => limited by $lessThan
        """
    
    prmd  = {2:1,3:2}
    sqrtn = 2
    l = 1
    count = 0
    #or (no==-1 and not lessThan) l < no or:
    # print("no", no)
    while ((no!=0 and count < no) or ( (no==0) and (lessThan and l<lessThan ) or (not lessThan ) ))and (l<4) :
        if l in prmd:
            count += 1
            yield l
        l+=1
    l=5
    add = 2
    
    while (no!=0 and count < no) or ( (no==0) and ( (lessThan and l<lessThan ) or (not lessThan )) ) :  #check only 6n-1 and 6n+1
        if l > sqrtn**2:
            sqrtn = l**0.5
        for i in prmd:
            if i > sqrtn:
                prmd[l] = len(prmd)
                add = 2 if add==4 else 2
                count +=1
                yield l
                break
            if l%i ==0 :  
                break
        l+=add
if __name__ == "__main__":
    n = int(input("Enter how many primes do you want (0-> inf): "))
    for i in primeGenerator(n):
        print(i,end = " ")
