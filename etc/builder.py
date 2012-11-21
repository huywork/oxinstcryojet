from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

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


