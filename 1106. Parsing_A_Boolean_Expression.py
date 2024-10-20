class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        def parse_not(e):
                if e == '0':
                  return '1'
                elif e == '1':
                  return '0'
            
        def parse_or(e):
            val = False
            for i in e:
                val =  val or int(i)
            return str(val)
        
        def parse_and(e):
            val = True
            for i in e:
                val =  val and int(i)
            return str(val)


        def parse(exp,op):
            s = ''
            res = ''
            for i in exp:
                if i == 'f':
                    s += '0'
                elif i == 't':
                    s +='1'
            if op == '!':
                res = parse_not(s)
            if op == '&':
                res = parse_and(s)
            if op == '|':
                res = parse_or(s)

            if res == '0' or 0:
                return 'f'
            elif res == '1' or 1:
                return 't'

        operator = []
        operand = []
        res = []
        i = 0
        for i in range(len(exp)):
            if exp[i] in "&|!":
                operator.append(exp[i])
            else:
                if exp[i] ==',':
                    continue
                else:
                    operand.append(exp[i])

                if exp[i] == ')':
                    operand.pop()
                    j = len(operand)-1
                    e = ''
                    while j>=0:
                        if operand[j] == '(':
                            operand.pop()
                            break
                        else:
                            e += operand[j]
                            operand.pop()
                            j-=1
                    p = parse(e[::-1],operator[-1])
                    operator.pop()
                    res.append(p)
                    operand.append(p)

        if res[-1] == 'f':
            return False
        else:
            return True 
        
