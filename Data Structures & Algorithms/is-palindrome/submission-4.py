#test: Racecar,  , tab a cat, bob on the job


class Solution:
    def isPalindrome(self, s: str) -> bool:   
        s_clean = [c.lower() for c in s if c.isalnum()]
        return s_clean == s_clean[::-1]

        # test
        # s = Racecar
        # s_clean = "racecar "
        # racecar == racecar
        
        # tab a cat
        # s = "tab a cat"
        # s_clean = "tabacat "
        # tabacat = tacabat
        # True

        #bob on the job
        # s = "Bob on the job"
        # s_clean = "bobonthejob"
        # bobonthejob == bojehtnobob
        #False 