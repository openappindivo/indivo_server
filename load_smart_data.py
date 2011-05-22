"""
SMART sample data

"""

from indivo.models import *

##
## Add some meds, problems, and more for testing smart apps
##

# FIXME code this
medication_1 = """<Medication xmlns="http://indivo.org/vocab/xml/documents#"> <dateStarted>2009-02-05</dateStarted> <dateStopped>2009-05-12</dateStopped><name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="856845">AMITRIPTYLINE HCL 50 MG TAB</name><dose> <value>3</value><unit type="http://indivo.org/codes/units#" value="pills" abbrev="p">pills</unit> </dose> <route type="http://indivo.org/codes/routes#" value="PO">By Mouth</route> <strength> <value>100</value> <unit type="http://indivo.org/codes/units#" value="mg" abbrev="mg">mg</unit> </strength> <frequency type="http://indivo.org/codes/frequency#" value="daily" abbrev="daily">daily</frequency> <prescription> <by> <name>Dr. Ken Mandl</name> <institution>Children's Hospital Boston</institution> </by> <on>2009-02-01</on> <stopOn>2010-01-31</stopOn> <dispenseAsWritten>true</dispenseAsWritten> <duration>P2M</duration> <refillInfo>once a month for 3 months</refillInfo> <instructions>don't take them all at once!</instructions> </prescription> </Medication>"""

# problems
problem_1 = """<Problem xmlns='http://indivo.org/vocab/xml/documents#'> <dateOnset>2009-05-16T12:00:00Z</dateOnset> <dateResolution>2009-05-16T16:00:00Z</dateResolution> <name type='http://www.ihtsdo.org/snomed-ct/concepts/' value='161891005'>Backache (finding)</name> <comments></comments> <diagnosedBy>Dr. Mandl</diagnosedBy> </Problem>"""

record = Record.objects.all()[0]

from indivo.views.documents.document import _document_create

for doc in [problem_1, medication_1]:
    _document_create(record.owner, doc, None, record)
