from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.asyn import Asyn
from iocbuilder.arginfo import *

class ILM201(AutoSubstitution):
    # Substitution attributes
    TemplateFile = 'ILM201.template'


class cryojetITC503S(AutoSubstitution, AutoProtocol):
    # Substitution attributes
    TemplateFile = 'cryojetITC503S.template'

    # AutoProtocol attributes
    ProtocolFiles = ['cjet.proto']


class cryojet(AutoSubstitution, AutoProtocol):
    # Substitution attributes
    TemplateFile = 'cryojet.template'

    # AutoProtocol attributes
    ProtocolFiles = ['cjet.proto']


class MercuryiTC_SCPI(AutoSubstitution):
    
    def __init__(self, P, Q, PORT):
        self.P = P
        self.Q = Q
        self.PORT = PORT

        heater = MercuryiTC_SCPI_heater(P=P, Q=Q, PORT=PORT)
        loop1 = MercuryiTC_SCPI_loop(P=P, Q=Q + ':LOOP', PORT=PORT, UID='DB4.T1')
        loop2 = MercuryiTC_SCPI_loop(P=P, Q=Q + ':LOOP2', PORT=PORT, UID='DB7.T1')
        system = MercuryiTC_SCPI_system(P=P, Q=Q, PORT=PORT)
        tempSensor = MercuryiTC_SCPI_tempSensor(P=P, Q=Q, PORT=PORT)


    ArgInfo = makeArgInfo(__init__,
        P   = Simple('Main PV address', str),
        Q     = Simple('Device Identifier', str),
        PORT   = Simple('AsynIP port to connect to', str))


class MercuryiTC_SCPI_heater(AutoSubstitution, AutoProtocol):
    Dependencies = (Asyn, Calc)
    # Substitution attributes
    TemplateFile = 'MercuryiTC-SCPI_heater.template'

    # AutoProtocol attributes
    ProtocolFiles = ['MercuryiTC-SCPI.proto']


class MercuryiTC_SCPI_loop(AutoSubstitution, AutoProtocol):
    Dependencies = (Asyn, Calc)

    # Substitution attributes
    TemplateFile = 'MercuryiTC-SCPI_loop.template'

    # AutoProtocol attributes
    ProtocolFiles = ['MercuryiTC-SCPI.proto']


class MercuryiTC_SCPI_system(AutoSubstitution, AutoProtocol):
    Dependencies = (Asyn, Calc)
    # Substitution attributes
    TemplateFile = 'MercuryiTC-SCPI_system.template'

    # AutoProtocol attributes
    ProtocolFiles = ['MercuryiTC-SCPI.proto']


class MercuryiTC_SCPI_tempSensor(AutoSubstitution, AutoProtocol):
    Dependencies = (Asyn, Calc)
    # Substitution attributes
    TemplateFile = 'MercuryiTC-SCPI_tempSensor.template'

    # AutoProtocol attributes
    ProtocolFiles = ['MercuryiTC-SCPI.proto']

