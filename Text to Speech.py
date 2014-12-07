class Solution:
    def __init__(self):
        self.digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        self.teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.bigs = ["", "thousand", "million"]

    def readNumber(self, number):
        if number == 0: return 'zero'
        if number < 0: return 'negative '+self.readNumber(-number)
        cnt = 0; string = ""
        while number>0:
            if number%1000 !=0:
                string = self.readNumber100(number%1000)+self.bigs[cnt]+" "+string
            number/=1000
            cnt+=1
        return string

    def readNumber100(self, number):
        string = ""
        if number >=100:
            string += self.digits[number/100-1]+" hundred "
            number %= 100
        if number >=11 and number<=19:
            return string + self.teens[number-11]+" "
        if number == 10 or number >=20:
            string += self.tens[number/10-1]+" "
            number%=10
        if number >=1 and number<=9:
            string += self.digits[number-1]+" "
        return string

if __name__ == "__main__":
    s = Solution()
    print s.readNumber(1234)

