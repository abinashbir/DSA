#include<bits/stdc++.h>
using namespace std;

int print(int &num){
    num=num+5;
    cout<<num<<endl;
    num=num+5;
    cout<<num<<endl;
    num=num+5;
    cout<<num<<endl;
    return num;
}

int main(){
    int num = 7;
    print(num);
    cout<<num<<endl;

    

}