class dataNodes:
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
            yield '''
            <DataNode>
		<Name>{}{}</Name>
            <StringId>2:SimulationExamples.Functions.{}{}</StringId>
	    </DataNode>'''.format(self.name, i, self.name, i)

    def next(self):
        for i in range(self.nb):
            yield '''
            <DataNode>
		<Name>{}{}</Name>
            <StringId>2:SimulationExamples.Functions.{}{}</StringId>
	    </DataNode>'''.format(self.name, i, self.name, i)

    def get_beginning(self):
        return ''
    
    def toString(self):
        str = self.get_beginning()
        for sub in next(self):
            str += sub
        return str

    def printer(self):
        with open(self.filename, "w") as f:
            f.write(self.get_beginning())
            for sub in next(self):
                f.write(sub)
