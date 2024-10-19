class Player:
    def __init__(self, name, avg, single, double, triple, hr):
        self.name = name
        self.avg = avg
        self.single = single
        self.double = double
        self.triple = triple
        self.hr = hr

    def __repr__(self):
        return "Name: {} AVG:{} 1B{} 2B{}, 3B{}, HR{}".format(self.name, self.avg, self.single, self.double, self.triple, self.hr)



