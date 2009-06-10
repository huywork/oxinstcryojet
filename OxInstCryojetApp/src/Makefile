TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC = OxInstCryojet

# OxInstCryojet.dbd will be installed into <top>/dbd
DBD += OxInstCryojet.dbd

# OxInstCryojet.dbd will be created from these files
OxInstCryojet_DBD += base.dbd
OxInstCryojet_DBD += stream.dbd


OxInstCryojet_LIBS += stream
OxInstCryojet_LIBS += $(EPICS_BASE_IOC_LIBS)

#DATA += OxInstCryojet_sim.py


include $(TOP)/configure/RULES
