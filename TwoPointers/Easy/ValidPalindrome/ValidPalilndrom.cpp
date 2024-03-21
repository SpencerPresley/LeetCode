#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(std::string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (!std::isalnum(s[left])) {
                left++;
                continue;
            }

            if (!std::isalnum(s[right])) {
                right--;
                continue;
            }

            if (std::tolower(s[left]) != std::tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
};

/*
Runtime: 4ms (Beats 79.98%)
Memory: 8.67mb (Beats 63.99%)


Explation

left starts at index 0, right starts at the last index of the string (character array)
We only iterate until the two pointers have met, as once they have met we will have checked if all the chars were the same
and if they were the same from the front to middle and back to middle then middle to back and middle to front are the same and thus
a palindrome.

The two initial if statments check if left is not a letter or number and if so skips that character
The second if does the same as the first but for the right side of the string

If the two current characters don't equal each other then we return false otherwise increase left and decrease right and continue

once entire string has been tracersed without returning false we can confidently return true

*/

#include <string>
#include <cctype>

class Solution2 {
public:
    bool isPalindrome2(const std::string& s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !std::isalnum(s[left])) left++;
            while (left < right && !std::isalnum(s[right])) right--;

            if (left < right && std::tolower(s[left]) != std::tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
};

/*
Runtime: 4ms (Beats 79.98%)
Memory: 8.34mb (Beats 99.61%)

Explanation

As with the first solutions we have two integers to act as pointers to index the character array (string)

And we again only iterate until the two pointers meet

Here though we have two while loops to check if the current character is a letter or number and if not we increment the pointer
We do this until left >= right as this will replace all non-alphanumeric characters in both halves of the string
This way imeediately takes care of all the non-alphanumerical characters rather than doing it each iteration. 

Then we make both current characters lowercase and check if they're equal, if they are we continue the loop iterating and decrementing the pointers,
otherwise return false.

Once string has been traversed return true

*/

