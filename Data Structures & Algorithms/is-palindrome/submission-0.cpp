#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string rs = "";
        for(auto c : s)
        {
            if(isalnum(c)) rs +=tolower(c);
        }

        string rstr = rs;
        reverse(rstr.begin(), rstr.end());

        return rstr == rs;
    }
};
