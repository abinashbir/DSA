#include<bits/stdc++.h>
using namespace std;

int main(){
    int s;

    cout<<"Enter the size of the array : ";
    cin>>s;

    int arr[s];

    for(int i=0;i<s;i++){
        cout<<"Enter the "<<i<<"th index : ";
        cin>>arr[i];
    }

    cout<<"The array is : ";
    for(int i =0;i<s;i++){
        cout<<arr[i]<<" ";
    }

    //modify the arr

    arr[4]+=67;
} 

