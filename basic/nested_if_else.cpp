#include<bits/stdc++.h>
using namespace std;

int main(){
    int age;
    cout<<"Please enter your age : ";
    cin>>age;

    if(age<18){
        cout<<"You are not eligible to vote"<<endl;
    }else if(age>=18){
        cout<<"You are eligible to vote"<<endl;

        if(age>=55 && age<=57){
            cout<<"Retirement soon";
        }else if(age>57){
            cout<<"RETIRE"<<endl;
        }

    }
}

