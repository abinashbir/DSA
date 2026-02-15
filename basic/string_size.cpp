#include <bits/stdc++.h>
using namespace std;

int main(){
    string b;
    cin >> b;

    int decimal = 0;

    for(char c : b){
        decimal = decimal * 2 + (c - '0');
    }

    cout << decimal;
}
