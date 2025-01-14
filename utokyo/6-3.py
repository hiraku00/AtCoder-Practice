class HelloForEver:
    def readline(self):
        return 'Hello.\n'

f = HelloForEver()
print(f)
print(type(f))
print(f.readline())

print(f'==================================')

class HelloFile:
    def __init__(self, n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return 'Hello.\n'

f = HelloFile(3)
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())

print(f'==================================')

class HelloFile2(HelloForEver):
    def __init__(self, n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return super().readline()

f = HelloFile2(3)
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())
print(f.n)
print(f.readline())

print(f'==================================')

class HelloFileIterator(HelloFile):
    def __iter__(self):
        return self
    def __next__(self):
        line = self.readline()
        if line == '':
            raise StopIteration
        return line

f = HelloFileIterator(3)
print(f is iter(f))
for line in f:
    print(line)

print(f'==================================')

class EmptyFile(HelloFileIterator):
    def readline(self):
        return ''

f = EmptyFile(3)
# next(f)

print(f'================================== Practice1')

class StringFileIterator(HelloFileIterator):
    def __init__(self, s, n):
        self.s = s
        self.n = n

    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return self.s

f = StringFileIterator('abc', 3)
print(list(f) == ['abc','abc','abc'])
