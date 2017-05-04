class dataSubs:
    def __init__(self, nb, name, freq, filename, oneSubPerYield):
        self.nb = nb
        self.name = name
        self.freq = freq
        self.i = 0
        self.filename = filename
        self.oneSub = oneSubPerYield #Integer
        print self.oneSub

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.nb):
            #if(self.oneSub == 0): # One sub per datapoint
            #    yield "<DataSubscriptionConfig><Name>{}{}</Name>\n\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n</DataSubscriptionConfig>\n".format(self.name, i, self.name, i)
            if(self.oneSub > 0): # One sub per self.oneSub datapoints
                if(i % self.oneSub == 0):
                    dn = ""
                    for j in range(self.oneSub):
                        dn += "\n\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name + "yay", i+j)
                    yield "<DataSubscriptionConfig><Name>{}{}</Name>{}</DataSubscriptionConfig>\n".format(self.name, i - 5, dn)
                else:
                    continue;
            else: # One sub to rule them all
                yield "\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name, i)

    def next(self):
        for i in range(self.nb):
            #if(self.oneSub == 0): # One sub per datapoint
            #    yield "<DataSubscriptionConfig><Name>{}{}</Name>\n\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n</DataSubscriptionConfig>\n".format(self.name, i, self.name, i)
            if(self.oneSub > 0): # One sub per self.oneSub datapoints
                if(i % self.oneSub == 0):
                    dn = ""
                    for j in range(self.oneSub):
                        dn += "\n\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name, i+j)
                    yield "<DataSubscriptionConfig><Name>{}{}</Name>{}</DataSubscriptionConfig>\n".format(self.name, i - 5, dn)
                else:
                    continue;
            else: # One sub to rule them all
                yield "\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name, i)

    def get_beginning(self):
        return "" #"<DataSubscriptionConfig>\n\t<Name>{}</Name>\n\t<PublishingInterval>{}</PublishingInterval>\n".format(self.name, self.freq)

    def get_ending(self):
        return "" #"\t</DataSubscriptionConfig>"

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
            f.write(self.get_ending())
            #f.write(self.toString)
