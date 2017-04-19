import random
class kepFuncts:
    def __init__(self, nb, name, freq, filename):
        self.nb = nb
        self.name = name
        self.freq = freq
        self.i = 0
        self.filename = filename

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.nb):
            yield '"load{}","SINE(1000,{},{},0.5,0)",Float,1,{},100,,,,,,,,,,"short description {}",\n'.format(i, random.randint(-1000, 0), random.randint(0, 1000), random.randint(0, 1000), "RW" if i%5 == 0 else "RO", i)

    def next(self):
        for i in range(self.nb):
            yield '"load{}","SINE(1000,{},{},0.5,0)",Float,1,{},100,,,,,,,,,,"short description {}",\n'.format(i, random.randint(-1000, 0), random.randint(0, 1000), random.randint(0, 1000), "RW" if i%5 == 0 else "RO", i)

    def get_beginning(self):
        return "Tag Name,Address,Data Type,Respect Data Type,Client Access,Scan Rate,Scaling,Raw Low,Raw High,Scaled Low,Scaled High,Scaled Data Type,Clamp Low,Clamp High,Eng Units,Description,Negate Value\n"

    def toString(self):
        str = self.get_beginning()
        for sub in next(self):
            str += sub
        str += self.get_ending()
        return str

    def printer(self):
        with open(self.filename, "w") as f:
            f.write(self.get_beginning())
            for sub in next(self):
                f.write(sub)
