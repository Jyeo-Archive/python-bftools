import sys

class Parser():
    def __init__(self, e):
        self.e = e
        s, self.m = [], {}
        for i, c in enumerate(self.e):
            if c == '[': s.append(i)
            elif c == ']':
                t = s.pop()
                self.m[i], self.m[t] = t, i

    def b(self, i):
        return self.m[i]

    def exe(self, log=False):
        i, p, v = 0, 0, {}
        result = []
        while i < len(self.e):
            c = self.e[i]
            try: v[p] 
            except: v[p] = 0
            if c == '+':
                v[p] += 1 if v[p] < 255 else 0
                if log: print('+ v[%d] = %d'%(p,v[p]))
            elif c == '-':
                v[p] -= 1 if v[p] > 0 else 255
                if log: print('- v[%d] = %d'%(p, v[p]))
            elif c == '>':
                p += 1
                if log: print('> p = %d'%p)
            elif c == '<':
                p -= 1
                if log: print('< p = %d'%p)
            elif c == '.':
                if log: print('. v[%d] => '%p, [chr(v[p])])
                result += chr(v[p])
            elif c == ',':
                v[p] = ord(sys.stdin.read(1))
                if log: print(', v[%d] => '%p, [chr(v[p])])
            elif c == '[':
                if (v[p] == 0): 
                    if log: print('[, going to', self.b(i))
                    i = self.b(i)
                    continue
                else: 
                    if log: print('[')
                    pass
            elif c == ']':
                if (v[p] != 0): 
                    if log: print('], going to', self.b(i))
                    i = self.b(i)
                    continue
                else: 
                    if log: print(']')
                    pass
            i += 1
        return ''.join(result)

if __name__ == '__main__':
    e = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
    sys.stdout.write(Parser(e).exe())
