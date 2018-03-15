
#include <iostream>
using namespace std;
void insertionSortRecursive(int arr[], int n)
{
    if (n < 1)
        return;
    insertionSortRecursive( arr, n-1 );
    int last = n-1;
    int j = n-2;
    int temp;
    while (j >= 0){
        if(arr[j] > arr[last])
    {
        temp=arr[last];
        arr[last] = arr[j];
        arr[j]=temp;
        last=j;
    }
        j--;
    }
    
}

void printArray(int arr[], int n)
{
    for (int i=0; i < n; i++)
        cout << arr[i] <<" ";
}

int main()
{
	
 	int n;
 	cin >> n;
 	int arr[n];
 	for(int i=0;i<n;i++)
 	{
 		cin >> arr[i];	
	}
    insertionSortRecursive(arr, n);
    printArray(arr, n);
 
    return 0;
}