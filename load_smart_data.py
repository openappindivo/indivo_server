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

# labs
labs_1 = """
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2009-07-16T12:00:00Z</dateMeasured>
  <labType>hematology</labType>
  <laboratory>
    <name>Quest</name>
    <address>300 Longwood Ave, Boston MA 02215</address>
  </laboratory>

  <labPanel>
    <name type="http://codes.indivo.org/labs/panels#" abbrev="cbc" value="CBC">CBC</name>
    
  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2009-07-16T12:23:00Z</dateMeasured>
    <name type="http://codes.indivo.org/labs/tests#" abbrev="Hct" value="evf">evf</name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <flag type="http://codes.indivo.org/hl7/abnormal-flags#" abbrev="A" value="abnormal" />
      <valueAndUnit>
	<value>49</value>
	<unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage">%</unit>
      </valueAndUnit>
      <normalRange>
	<minimum>44</minimum>
	<maximum>48</maximum>
	<unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage" />
      </normalRange>
      <nonCriticalRange>
	<minimum>42</minimum>
	<maximum>50</maximum>
	<unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage" />
      </nonCriticalRange>
    </result>
    
  </labTest>

    <labTest xsi:type="SingleResultLabTest">
      <dateMeasured>2009-07-16T12:23:00Z</dateMeasured>
      <name type="http://codes.indivo.org/labs/tests#" abbrev="Hct" value="evf" />
      <final>true</final>
      <result xsi:type="ResultInRange">
	<flag type="http://codes.indivo.org/hl7/abnormal-flags#" abbrev="A" value="abnormal" />
	<valueAndUnit>
	  <value>49</value>
	  <unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage" />
	</valueAndUnit>
	<normalRange>
	  <minimum>44</minimum>
	  <maximum>48</maximum>
	  <unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage" />
	</normalRange>
	<nonCriticalRange>
	  <minimum>42</minimum>
	  <maximum>50</maximum>
	  <unit type="http://codes.indivo.org/units#" abbrev="%" value="percentage" />
	</nonCriticalRange>
      </result>

    </labTest>

    <labTest xsi:type="SingleResultLabTest">
      <dateMeasured>2009-07-16T12:23:00Z</dateMeasured>
      <name type="http://codes.indivo.org/labs/tests#" abbrev="hiv" value="HIV" />
      <final>true</final>
      <result xsi:type="ResultInSet">
	<!-- there could be a flag here -->
	<!-- <flag type="http://codes.indivo.org/hl7/abnormal-flags#" abbrev="A" value="abnormal" /> -->
	<value>negative</value>

	<!-- these options may not be listed, given that flag may be raised -->
	<option normal="false">positive</option>
	<option normal="true">negative</option>
	<option normal="true" description="insufficient sample">inconclusive</option>
      </result>
    </labTest>
  </labPanel>

  <comments>was looking pretty sick</comments>

</Lab>
"""

# demographics
demographics_xml = """
<Demographics xmlns="http://indivo.org/vocab/xml/documents#">
    <dateOfBirth>1960-05-15</dateOfBirth>
    <gender>Female</gender>
    <ethnicity>Basque</ethnicity>
    <language>EN</language>
    <maritalStatus>Married</maritalStatus>
    <income>65,000 USD</income>
    <highestEducation>High School</highestEducation>
    <organDonor>true</organDonor>
</Demographics>
"""

record = Record.objects.all()[0]

# so we know which record we're adding this to
print "adding SMART data to Record %s - %s" % (record.id, record.label)

from indivo.views.documents.document import _document_create

# create some demographics for that poor record
if not record.demographics:
    demographics_doc = _document_create(record.owner, demographics_xml, None, record)
    from indivo.views.documents.special_documents import set_special_doc
    set_special_doc(record, 'demographics', demographics_doc)

for doc in [problem_1, medication_1, labs_1]:
    _document_create(record.owner, doc, None, record)

