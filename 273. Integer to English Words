class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        one_map = {
            1 : "One",
            2 : "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five", 
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 : "Eleven", 
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
        }
        twenty_map = {
            20 : "Twenty",
            30 : "Thirty",
            40 : "Forty",
            50 : "Fifty",
            60 : "Sixty",
            70 : "Seventy",
            80 : "Eighty",
            90 : "Ninety"
        }

        def get_str(num):
            res = []
            hund = num //  100 
            if hund:
                res.append(one_map[hund] + " Hundred")
            last_two = num % 100
            if last_two >= 20:
                tens, ones = last_two // 10 , last_two % 10
                res.append(twenty_map[tens * 10 ])
                if ones:
                    res.append(one_map[ones])
            elif last_two:
                res.append(one_map[last_two])
            return " ".join(res)

        prefix = [""," Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            last_three = num % 1000
            ans = get_str(last_three) 
            if ans:
                res.append(ans + prefix[i])
            i += 1
            num =  num // 1000
        res.reverse()
        return " ".join(res)



       
