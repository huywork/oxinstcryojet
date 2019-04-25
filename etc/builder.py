from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.calc import Calc
from iocbuilder.modules.asyn import Asyn

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