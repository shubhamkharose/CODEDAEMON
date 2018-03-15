
#include <stdio.h>

void insertionSortRecursive(int arr[], int n)
{
    if (n <= 1)
        return;
    int i=0;
    int tmp=arr[n-1];
    while(i<n)
    {
        if(arr[i]<tmp)
        {    
            tmp=arr[i];
            arr[i]=arr[n-1];
            arr[n-1]=tmp;
        }
        i++;
    }
    insertionSortRecursive(arr,n-1);
}

void printArray(int arr[], int n)
{
	int i;
    for(i=0; i < n; i++)
        printf("%d ",arr[i]);
}

int main()
{
	
 	int n;
	scanf("%d",&n);
 	int arr[n],i;
 	for( i=0;i<n;i++)
 	{
 		scanf("%d",&arr[i]);
	}
    insertionSortRecursive(arr, n);
    printArray(arr, n);
    return 0;
}