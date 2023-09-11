#include <iostream>
using namespace std;

int fib(int n) {
    if(n < 2) {
        return n;
    } else {
        return fib(n - 2) + fib(n - 1);
    }
}

int main() {
    int i;
    cout << "Enter number: " << endl;
    cin >> i;
    cout << fib(i) << endl;
}

