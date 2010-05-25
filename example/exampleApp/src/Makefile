TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

#LIBRARY_IOC += xxx

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# xxxRecord.dbd will be installed into <top>/dbd
#DBD += xxx.dbd

# The following are compiled and added to the support library
#xxx_SRCS += xxxCodeA.c
#xxx_SRCS += xxxCodeB.c

# We need to link against the EPICS Base libraries
#xxx_LIBS += $(EPICS_BASE_IOC_LIBS)

SCRIPTS=stExample-gui

# ------------------------
# Build an IOC Application
# ------------------------

PROD_IOC = example

PROD_IOC_Linux = example_sim

# example.dbd will be installed into <top>/dbd
DBD += example.dbd
DBD += example_sim.dbd

# example.dbd will be created from these files
example_DBD += base.dbd
example_DBD += stream.dbd
example_DBD += drvAsynSerialPort.dbd
example_DBD += drvAsynIPPort.dbd

example_sim_DBD += base.dbd
example_sim_DBD += stream.dbd
example_sim_DBD += drvAsynSerialPort.dbd
example_sim_DBD += drvAsynIPPort.dbd
##example_sim_DBD += PythonEmbed.dbd

# example_registerRecordDeviceDriver.cpp will be created
# example.dbd
example_SRCS += example_registerRecordDeviceDriver.cpp
example_sim_SRCS += example_sim_registerRecordDeviceDriver.cpp

# These two lines are needed for non-vxWorks builds, such as Linux
example_SRCS_DEFAULT += exampleMain.cpp
example_SRCS_vxWorks += -nil-
example_sim_SRCS_DEFAULT += exampleMain.cpp
example_sim_SRCS_vxWorks += -nil-

# Add locally compiled object code
#example_SRCS +=

# The following adds object code from base/src/vxWorks
example_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# This line says that this IOC Application depends on the
# xxx Support Module
#example_LIBS += xxx
example_LIBS += asyn
example_LIBS += stream

example_sim_LIBS += asyn
example_sim_LIBS += stream
##example_sim_LIBS += PythonEmbed

# We need to link this IOC Application against the EPICS Base libraries
example_LIBS += $(EPICS_BASE_IOC_LIBS)
example_sim_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

USES_DB = $(TOP)/db/example.db
parser-example : $(USES_DB) 
	@echo "Installing postprocessor files $(USES_DB)" 
	epicsparser.py $(USES_DB) -r example > $@ 
	xmllint --schema $(GDA)/data/genericBeamlineSchema.xsd example-gda-interface.xml > /dev/null 
	@echo "Installing postprocessor files" 
	@$(INSTALL_PRODUCT) -d -m 555 example* $(INSTALL_DATA)
         
#buildInstall: parser-example

