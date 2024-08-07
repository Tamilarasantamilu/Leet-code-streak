class Solution:

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return 'Zero'

        literals = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }

        # extend for bigger units beyond billion
        units = ['', 'Thousand', 'Million', 'Billion'][::-1]

        limit = len(units) * 3

        num = str(num).zfill(limit)

        result = ""

        for i, j in enumerate(range(0, limit, 3)):
            chunk = num[j:j+3]

            if int(chunk):
                if (hundreds := int(chunk[0])):
                    result += f"{literals[hundreds]} Hundred "
                if (tens := int(chunk[1:3])):
                    if tens < 20:
                        result += f"{literals[tens]} "
                    else:
                        result += f"{literals[int(chunk[1])*10]} "
                        try:
                            result += f"{literals[int(chunk[2])]} "
                        except Exception:
                            ...
                result += f"{units[i]} "

        return result.strip()
