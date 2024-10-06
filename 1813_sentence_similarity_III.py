#You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.
#
#Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.
#
#For example,
#
#s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
#s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
#Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
#
# 
#
#Example 1:
#
#Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
#
#Output: true
#
#Explanation:
#
#sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
#
#Example 2:
#
#Input: sentence1 = "of", sentence2 = "A lot of words"
#
#Output: false
#
#Explanation:
#
#No single sentence can be inserted inside one of the sentences to make it equal to the other.
#
#Example 3:
#
#Input: sentence1 = "Eating right now", sentence2 = "Eating"
#
#Output: true
#
#Explanation:
#
#sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
#
# 
#
#Constraints:
#
#1 <= sentence1.length, sentence2.length <= 100
#sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
#The words in sentence1 and sentence2 are separated by a single space.
#

# using deque
class solution:
    def areSentenceSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque1 = deque(sentence1.spilt())
        deque2 = deque(sentence2.spilt())

        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()

        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()

        return not deque1 or not deque2

            
        

# using two pointer 

class solution:
    def areSentenceSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1list = sentence1.spilt(" ")
        s2list = sentence2.spilt(" ")
        
        if len(s1list) > len(s2list):
            self.areSentenceSimilar(sentence2, sentence1)

        start,end1, end2 = 0, len(s1list) - 1, len(s2list)

        while start < len(s1list) and s1list[start] == s2list[start]:
            start += 1

        while end1 >= 0 and s1list[end1] == s2list[end]:
            end1 -= 1
            end2 -= 1

        return end1 < start












