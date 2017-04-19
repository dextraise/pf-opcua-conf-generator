class dataSubs:
    def __init__(self, nb, name, freq):
        self.nb = nb
        self.name = name
        self.freq = freq
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.nb):
            yield "\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name, i)

    def next(self):
        for i in range(self.nb):
            yield "\t<DataNode>\n\t\t<Name>{}{}</Name>\n\t</DataNode>\n".format(self.name, i)

    def get_beginning(self):
        return "<DataSubscriptionConfig>\n\t<Name>{}</Name>\n\t<PublishingInterval>{}</PublishingInterval>\n".format(self.name, self.freq)

    def get_ending(self):
        return "\t</DataSubscriptionConfig>"

    def toString(self):
        str = self.get_beginning()
        for sub in next(self):
            str += sub
        str += self.get_ending()
        return str
