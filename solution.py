
"""
Joseph Wu
CMSC389O section 0301
uid: 118956183
I pledge on my honor that I have not given or received any unauthorized 
assistance on this assignment/examination.

Homework 2 Assignment:
Given a string, find the length of the longest substring without repeating 
characters.
*Note that the answer must be a substring (e.g. "abcd" is a subsequence of 
“abbbcccd”, not a substring).
Examples:
“abcabcbb” → 3 ("abc", with the length of 3)
“bbbbb” → 1 ("b", with the length of 1.)
“pwwkew” → 3 ("wke", with the length of 3)

The problem my code solves:
The point of this code is to find the longest consecutive substring that does
not contain any same letters. I assumed that the input will contain only 
letters from the alphabet and no special character or spaces will be in the 
input (although, I am  confident my code will also be able to hand these 
cases). 

How does my code work?
I used the use sliding window technique to solve this problem. I used two
pointers initally set to the first element of the string s, a variable 
longest_length to keep track of how long the longest valid substring is, and 
a set to keep track of what letters are inside the longest valid substring.
As I iterate through the list using the while loop, the right pointer named
right checks to see if the letter at that index is inside of my set. If it
isn't, it adds that letter to the set and goes to the next letter. It then
also updates/calculates how long the longest substring is. However, if the 
right pointer points to a letter that is already in the substring, it removes
the letter from the set and left index is

Time Complexity Analysis:
The time complexity of this program is O(n). Everything not inside of the 
while loop takes some constant time (the variable declarations, the if 
statement and the return statement). The while loop runs while right is less 
than the length of the input string s. Inside the if part of the if statement,
the variable right is incremented. Inside the else part of the if statement, 
the variable left is incremented and the variable right is set to left. So
since left is never decremented and cannot go backwards, the whole thing will 
in the worst case take 2n + c. This is O(n) by definition.
"""

# this function takes in a string input
def longestString(s):   
    # declare/initialize the pointers and variables
    left = 0            #used as the left pointer
    right = 0           #used as the right pointer
    letters = set()     #tracks of which letters are in the longest substring
    longest_length = 0  #keep tracks of how long the longest substring is

    #sliding window used to find length of longest substring
    while right < len(s):
        #if this letter is not in the set
        if s[right] not in letters: 
            #add the letter to set
            letters.add(s[right]) 
            #update/calculate longest length string
            longest_length = max(longest_length, (right - left + 1))
            #go to pointer right to the next letter
            right += 1 
        #if the letter is in the set
        else: 
            #remove the letter from set
            letters.remove(s[left])
            #move pointer left to the next letter
            left += 1
            #reset right pointer to left so start a new substring
            right = left
        
    #returns the length of the longest substring without repeating letters
    return longest_length



"""
This is my like 7th python program (6? from in class) so a lot of the syntax 
and naming conventions are probably off. Please let me know so I don't do it 
again.
"""