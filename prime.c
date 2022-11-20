#include <math.h>
#include <stdio.h>
#include <stdbool.h>

bool isprime(int n) {
    
    for (int i = 2; i < (int)round(sqrt(n))+1; i++) {//Complex math only need to go to sqrt(n)+1
        if (n%i==0) {//Check for a remainder
            return false;//NOT PRIME
        }
    }
    return true;//If it gets through loop, it is prime.
}

long calcprimes(int n) {
    long x = 0;//X may get very large
    int l = 0;//Prime counter, kept as int for comparison with n
    while (1) {//Infinite Loop
        x++;//Increment X
        if (x==1) {
            continue;//If X is one, skip because of error
        }
        if (isprime(x)==0) {//Checking for prime
            continue;//Not prime
        }
        //Prime
        l++;//Increment primt counter
        if (l==n) {//Prime is n:
            return x;
        }
    }

}

int main() {
    int lookup = 3;
    printf("Optimized Prime Calculator: What Prime Number do you want to look up?: ");
    scanf("%i",&lookup);//Getting input
    printf("%ld \n",calcprimes(lookup));
}