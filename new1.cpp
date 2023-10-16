#include <iostream>
using namespace std;

bool isOddLengthPalindrome(int num) {
    string strNum = to_string(num);
    int length = strNum.length();
    
    for (int i = 0; i < length/2; ++i) {
        if (strNum[i] != strNum[length - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (isOddLengthPalindrome(num)) {
        cout << num << " is an odd-length palindromic number." << endl;
    } else {
        cout << num << " is not an odd-length palindromic number." << endl;
    }

    return 0;
}
