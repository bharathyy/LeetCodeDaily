class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str_num1 = str(num1)
        str_num2 = str(num2)
        str_num3 = str(num3)
        
        len_num1 = len(str_num1)
        len_num2 = len(str_num2)
        len_num3 = len(str_num3)
        
        # List of lengths
        lst = [len_num1, len_num2, len_num3]
        max_len = max(lst)
        min_len = min(lst)
        
        output_str = ""
        
        str_num1 = str_num1.zfill(max_len)
        str_num2 = str_num2.zfill(max_len)
        str_num3 = str_num3.zfill(max_len)
        
        for i in range(max_len):
            lst = [int(str_num1[i]), int(str_num2[i]), int(str_num3[i])]
            output_str += str(min(lst))
        
        return int(output_str)


