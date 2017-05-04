import dataSubs
import dataNodes
import kepFuncts

class confOpc:
    def __init__(self, nb, name, freq, prefix, server, agg):
        self.nb = nb
        self.name = name
        self.freq = freq
        self.i = 0
        self.prefix = prefix
        self.server = server
        self.datasubs = dataSubs.dataSubs(nb, self.prefix, freq, prefix + "_" + str(nb) + "_dataSubs.xml", agg)
        self.datanodes = dataNodes.dataNodes(nb, self.prefix, freq, prefix + "_" + str(nb) + "_dataNodes.xml")
        self.kepFuncts = kepFuncts.kepFuncts(nb, self.prefix, freq, prefix + "_" + str(nb) + "_functions.csv")

    def printAll(self):
        ret = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<OPCUAMachineAdapterConfig>
    <OPCUAClientConfig>
        <AppName>PredixMachine_OPCUAAdapter</AppName>
        <ServerUri>opc.tcp://{}:49320</ServerUri>
        <AppUri>urn:localhost:UA:PredixMachine_OPCUAAdapter</AppUri>
        <ProductUri>urn:ge.com:UA:PredixMachine_OPCUAAdapter</ProductUri>
    </OPCUAClientConfig>
    <DataNodeConfigs>
        <DataNode>
        <Name>String</Name>
	<StringId>2:SimulationExamples.Functions.User1</StringId>
	</DataNode>
		<DataNode>
			<Name>Bool</Name>
			<StringId>2:SimulationExamples.Functions.Bool1</StringId>
		</DataNode>
		<DataNode>
			<Name>FloatSine</Name>
			<StringId>2:SimulationExamples.Functions.Sine1</StringId>
		</DataNode>
		<DataNode>
			<Name>Long2</Name>
			<StringId>2:SimulationExamples.Functions.Random2</StringId>
		</DataNode>
		<DataNode>
			<Name>Long</Name>
			<StringId>2:SimulationExamples.Functions.Random1</StringId>
		</DataNode>
		<DataNode>
			<Name>Long3</Name>
			<StringId>2:SimulationExamples.Functions.Random3</StringId>
		</DataNode>
		<DataNode>
			<Name>Node3</Name>
			<StringId>2:SimulationExamples.Functions.Ramp1</StringId></DataNode>
		<DataNode>
			<Name>Ramp3</Name>
			<StringId>2:SimulationExamples.Functions.Ramp3</StringId>
		</DataNode>
                <DataNode>
			<Name>gps</Name>
			<StringId>2:SimulationExamples.Functions.GPS</StringId>
		</DataNode>
                
        {}
    </DataNodeConfigs>
    <DataSubscriptionConfigs>
		<DataSubscriptionConfig>
			<Name>sub1</Name>
			<PublishingInterval>5000</PublishingInterval>
			<DataNode>
				<Name>Node3</Name>
			</DataNode>
			<DataNode>
				<Name>Ramp3</Name>
			</DataNode>
		</DataSubscriptionConfig>
		<DataSubscriptionConfig>
			<Name>subGps</Name>
			<PublishingInterval>10000</PublishingInterval>
			<DataNode>
				<Name>gps</Name>
			</DataNode>
		</DataSubscriptionConfig>

		<DataSubscriptionConfig>
			<Name>subLong</Name>
			<PublishingInterval>5000</PublishingInterval>
			<DataNode>
				<Name>Long</Name>
			</DataNode>
			<DataNode>
				<Name>Long2</Name>
			</DataNode>
			<DataNode>
				<Name>Long3</Name>
			</DataNode>
		</DataSubscriptionConfig>

		<DataSubscriptionConfig>
			<Name>subBool</Name>
			<PublishingInterval>10000</PublishingInterval>
			<DataNode>
				<Name>Bool</Name>
			</DataNode>
		</DataSubscriptionConfig>

		<DataSubscriptionConfig>
			<Name>subString</Name>
			<PublishingInterval>9000</PublishingInterval>
			<DataNode>
				<Name>String</Name>
			</DataNode>
		</DataSubscriptionConfig>
        {}
    </DataSubscriptionConfigs>
</OPCUAMachineAdapterConfig>
'''.format(self.server, self.datanodes.toString(), self.datasubs.toString())
        print ret
        with open("machineadapter.opcua.xml", "w") as f:
            f.write(ret)
        self.kepFuncts.printer()

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
