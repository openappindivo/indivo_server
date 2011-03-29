## 
## add a medication
## 

from indivo.models import *

a = Account.objects.get(email = 'benadida@informedcohort.org')

r = a.records_owned_by.get(label = 'Ben Adida')

from indivo.views.documents.document import _document_create

_document_create(a, """
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2009-02-05</dateStarted>
  <dateStopped>2010-02-10</dateStopped>
  <name type="http://indivo.org/codes/meds#" abbrev="c2i" value="COX2 Inhibitor">COX2 Inhibitor</name>
  <brandName type="http://indivo.org/codes/meds#" abbrev="vioxx" value="Vioxx">Vioxx</brandName>
  <dose>
    <value>3</value>
    <unit type="http://indivo.org/codes/units#" value="pills" abbrev="p" />
  </dose>
  <route type="http://indivo.org/codes/routes#" value="PO">By Mouth</route>
  <strength>
    <value>100</value>
    <unit type="http://indivo.org/codes/units#" value="mg" abbrev="mg" />
  </strength>
  <frequency type="http://indivo.org/codes/frequency#" value="daily">daily</frequency>

  <prescription>
    <by>
      <name>Dr. Ken Mandl</name>
      <institution>Children's Hospital Boston</institution>
    </by>

    <on>2009-02-01</on>
    <stopOn>2010-01-31</stopOn>

    <dispenseAsWritten>true</dispenseAsWritten>
    
    <!-- this duration means 2 months -->
    <duration>P2M</duration>
    
    <!-- does this need more structure? -->
    <refillInfo>once a month for 3 months</refillInfo>
    
    <instructions>don't take them all at once!</instructions>
    
  </prescription>
</Medication>
""", pha = None, record = r)

_document_create(a, """
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2010-01-25</dateStarted>
  <dateStopped>2010-03-12</dateStopped>
  <name type="http://indivo.org/codes/meds#" abbrev="c2i" value="COX2 Inhibitor">COX2 Inhibitor</name>
  <brandName type="http://indivo.org/codes/meds#" abbrev="cel" value="Celebres">Celebrex</brandName>
  <dose>
    <value>2</value>
    <unit type="http://indivo.org/codes/units#" value="pills" abbrev="p" />
  </dose>
  <route type="http://indivo.org/codes/routes#" value="PO">By Mouth</route>
  <strength>
    <value>150</value>
    <unit type="http://indivo.org/codes/units#" value="mg" abbrev="mg" />
  </strength>
  <frequency type="http://indivo.org/codes/frequency#" value="daily">daily</frequency>

  <prescription>
    <by>
      <name>Dr. Zak Kohane</name>
      <institution>Children's Hospital Boston</institution>
    </by>

    <on>2010-01-11</on>
    <stopOn>2011-01-31</stopOn>

    <dispenseAsWritten>true</dispenseAsWritten>
    
    <!-- this duration means 2 months -->
    <duration>P5M</duration>
    
    <!-- does this need more structure? -->
    <refillInfo>once a month for 3 months</refillInfo>
    
    <instructions>don't take them all at once!</instructions>
    
  </prescription>
</Medication>
""", pha = None, record = r)
