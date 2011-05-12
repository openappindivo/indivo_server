"""
SMART sample data

"""

from indivo.models import *

##
## Add some meds, problems, and more for testing smart apps
##

# FIXME code this
medication_1 = """<Medication xmlns="http://indivo.org/vocab/xml/documents#"> <dateStarted>2009-02-05</dateStarted> <name type="http://indivo.org/codes/meds#" abbrev="c2i" value="COX2 Inhibitor">COX2 Inhibitor</name>   <brandName type="http://indivo.org/codes/meds#" abbrev="vioxx" value="Vioxx">Vioxx</brandName> <dose> <value>3</value> <unit type="http://indivo.org/codes/units#" value="pills" abbrev="p">pills</unit> </dose> <route type="http://indivo.org/codes/routes#" value="PO">By Mouth</route> <strength> <value>100</value> <unit type="http://indivo.org/codes/units#" value="mg" abbrev="mg">mg</unit> </strength> <frequency type="http://indivo.org/codes/frequency#" value="daily" abbrev="daily">every 12 hours</frequency> <prescription> <by> <name>Dr. Ken Mandl</name> <institution>Children's Hospital Boston</institution> </by> <on>2009-02-01</on> <stopOn>2010-01-31</stopOn> <dispenseAsWritten>true</dispenseAsWritten> <duration>P2M</duration> <refillInfo>once a month for 3 months</refillInfo> <instructions>don't take them all at once!</instructions> </prescription> </Medication>"""

record = Record.objects.all()[0]

from indivo.views.document import _document_create

_document_create(record.owner, medication_1, None, record)
