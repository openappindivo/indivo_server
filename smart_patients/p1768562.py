
from indivo.models import *
a = Account.objects.order_by('?')[0]
record = Record(owner=a, label='Stephan Moore')
record.save()
problems = []
meds = []
labs = []
demographics = []

demographics.append("""
<Demographics xmlns="http://indivo.org/vocab/xml/documents#">
    <dateOfBirth>1939-08-20</dateOfBirth>
    <gender>male</gender>
    <language>EN</language>
</Demographics>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>222</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.4</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.5</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.6</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30934-4"><![CDATA[BNP SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>834</value>
        <unit type="http://unitsofmeasure.org/#" value="pg/mL">pg/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>17</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>89</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.69</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.5</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>14.2</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>107</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.2</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>140</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.3</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>30.2</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>90.7</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-11-30T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11580-8"><![CDATA[TSH SerPl DL<=0.005 mU/L-aCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="mcU/mL">mcU/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2093-3"><![CDATA[Cholest SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>141</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>207</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>107</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.1</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>15</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>140</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13457-7"><![CDATA[LDLc SerPl Calc-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>90</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>112</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2085-9"><![CDATA[HDLc SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>31</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.19</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>93.7</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.2</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.9</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-01T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2571-8"><![CDATA[Trigl SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>84</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>180</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>91.9</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>32.2</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>35.1</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>138</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>107</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.3</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.4</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.82</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>86</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>16</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.1</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.4</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2003-12-02T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.4</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>215</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1920-8"><![CDATA[AST SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>25</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1975-2"><![CDATA[Bilirub SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1751-7"><![CDATA[Albumin SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.6</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2885-2"><![CDATA[Prot SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.7</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="6768-6"><![CDATA[ALP SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>99</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.8</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>29.5</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>87.2</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>138</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11580-8"><![CDATA[TSH SerPl DL<=0.005 mU/L-aCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.33</value>
        <unit type="http://unitsofmeasure.org/#" value="mcU/mL">mcU/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.96</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>86</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>24</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>14.6</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.5</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.2</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1742-6"><![CDATA[ALT SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.3</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.5</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>101</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>137</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>99</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.2</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>23</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>90</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-06T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2004-01-03T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30522-7"><![CDATA[CRP SerPl HS-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.4</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/L">mg/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="49436004">Atrial fibrillation</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="29857009">Chest pain</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="88223008">Chronic pulmonary heart disease</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="82523003">Congestive rheumatic heart failure</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="233817007">Coronary arteriosclerosis</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="83521008">Dilated cardiomyopathy secondary to alcohol</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="297242006">FH: Cardiac disorder</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="64715009">Hypertensive heart disease, unspecified, without heart failure</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="36083008">Sinus node dysfunction</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2003-11-30T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="89765005">Tobacco dependence syndrome</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2004-01-03T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="85898001">Cardiomyopathy</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2004-01-03T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="35489007">Depressive disorder</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2004-01-03T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="8517006">History of tobacco use</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2004-01-03T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="55822004">Hyperlipidemia</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2004-09-15T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="13645005">Chronic obstructive lung disease</name>
</Problem>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-07-30</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="200033">carvedilol 25 MG Oral Tablet</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-07-30</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="309889">Digoxin 0.25 MG Oral Tablet [Lanoxin]</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-07-30</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="828348">Cyclobenzaprine hydrochloride 10 MG Oral Tablet</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="3 /d">3 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 tid prn</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-07-30</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="855334">Warfarin 5 MG Oral Tablet [Coumadin]</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-08-22</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="213469">celecoxib 200 MG Oral Capsule [Celebrex]</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2008-08-28</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="261962">Ramipril 10 MG Oral Capsule</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2009-01-03</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="197606">Digoxin 0.25 MG Oral Tablet</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2009-02-05</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="310429">Furosemide 20 MG Oral Tablet</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily</instructions>
  </prescription>
</Medication>
""".encode())


# so we know which record we're adding this to
print "adding SMART data to Record %s - %s" % (record.id, record.label)

from indivo.views.documents.document import _document_create

# create some demographics for that poor record
demographics_doc = _document_create(record.owner, demographics[0], None, record)
from indivo.views.documents.special_documents import set_special_doc
set_special_doc(record, 'demographics', demographics_doc)

for doc in problems + meds + labs:
    print doc
    _document_create(record.owner, doc, None, record)

