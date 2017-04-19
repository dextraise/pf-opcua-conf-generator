import dataSubs
import dataNodes
import kepFuncts

class confOpc:
    def __init__(self, nb, name, freq, prefix, server):
        self.nb = nb
        self.name = name
        self.freq = freq
        self.i = 0
        self.prefix = prefix
        self.server = server
        self.datasubs = dataSubs.dataSubs(nb, self.prefix, freq)
        self.datanodes = dataNodes.dataNodes(nb, self.prefix, freq)
        self.kepFuncts = kepFuncts.kepFuncts(nb, self.prefix, freq, prefix + "_" + str(nb) + "_functions.csv")

    def printLoads(self):
        ret = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<OPCUAMachineAdapterConfig>
    <OPCUAClientConfig>
        <AppName>PredixMachine_OPCUAAdapter</AppName>
        <ServerUri>opc.tcp://{}:49320</ServerUri>
        <AppUri>urn:localhost:UA:PredixMachine_OPCUAAdapter</AppUri>
        <ProductUri>urn:ge.com:UA:PredixMachine_OPCUAAdapter</ProductUri>
    </OPCUAClientConfig>
    <DataNodeConfigs>
        {}
    </DataNodeConfigs>
    <DataSubscriptionConfigs>
        {}
    </DataSubscriptionConfigs>
</OPCUAMachineAdapterConfig>
'''.format(self.server, self.datanodes.toString(), self.datasubs.toString())
        with open("machineadapter_"+str(self.nb)+".opcua.xml", "w") as f:
            f.write(ret)
        self.kepFuncts.printer()
