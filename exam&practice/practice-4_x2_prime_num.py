sum = 0
for digit in range(2, 100+1):
    isPrime = True
    for i in range(2, digit):
        if digit % i == 0:
            isPrime = False
            break
    if isPrime is True:
        print(digit)
        sum += digit
print(sum)

# refer to C language []
'''

#include <stdio.h> 
void main()
{
	int m,n;
	int i;
	int cnt=0;
	int sum=0;
	scanf("%d %d",&m,&n);
	
	if(m==1)
		m=2;
	for(i=m;i<=n;i++){
		int isPrime=1;
		int k;
		for(k=2;k<i;k++){
			if(i%k==0){
				isPrime=0;
				break;
			}
		}
		if(isPrime==1){
			cnt++;
			sum+=i;
			printf("%d ",i);
		}
	}
	printf("\n");
	printf("cnt=%d,sum=%d\n",cnt,sum);
} 

'''