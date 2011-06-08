
from indivo.models import *
a = Account.objects.order_by('?')[0]
record = Record(owner=a, label='George Ross')
record.save()
problems = []
meds = []
labs = []
demographics = []

demographics.append("""
<Demographics xmlns="http://indivo.org/vocab/xml/documents#">
    <dateOfBirth>1960-06-08</dateOfBirth>
    <gender>male</gender>
    <language>EN</language>
</Demographics>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1648-5"><![CDATA[TB Wheal 3D p 5 TU Diam]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mm">mm</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>263</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26511-6"><![CDATA[Neutrophils NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>63</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26478-8"><![CDATA[Lymphocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>17</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26485-3"><![CDATA[Monocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>11</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>15.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6.6</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>98</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>139</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>77.2</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.4</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>35.4</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="735-1"><![CDATA[Variant Lymphs NFr Bld Manual]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>10.9</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.8</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5.82</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13969-1"><![CDATA[CK MB SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6.9</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13969-1"><![CDATA[CK MB SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5.8</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10839-9"><![CDATA[Troponin I SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-12T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>98</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5811-5"><![CDATA[Sp Gr Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.019</value>
        <unit type="http://unitsofmeasure.org/#" value=""></unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5803-2"><![CDATA[pH Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5.5</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5804-0"><![CDATA[Prot Ur Strip-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>30</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1648-5"><![CDATA[TB Wheal 3D p 5 TU Diam]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mm">mm</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>437</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26486-1"><![CDATA[Monocytes NFr CSF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1975-2"><![CDATA[Bilirub SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2342-4"><![CDATA[Glucose CSF-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>60</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2880-3"><![CDATA[Prot CSF-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>159</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26478-8"><![CDATA[Lymphocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>43</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26485-3"><![CDATA[Monocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26450-7"><![CDATA[Eosinophil NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>15.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>11.2</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1742-6"><![CDATA[ALT SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>225</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26498-6"><![CDATA[Myelocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1920-8"><![CDATA[AST SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>152</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>79</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.3</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.2</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="6768-6"><![CDATA[ALP SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>129</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2885-2"><![CDATA[Prot SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.3</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1751-7"><![CDATA[Albumin SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="735-1"><![CDATA[Variant Lymphs NFr Bld Manual]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3298-7"><![CDATA[Acetamin SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="ug/mL">ug/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="9842-6"><![CDATA[Casts #/area UrnS LPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5</value>
        <unit type="http://unitsofmeasure.org/#" value="/[LPF]">/[LPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2069-3"><![CDATA[Chloride Bld-sCnc]]></name>
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
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5796-8"><![CDATA[Hyaline Casts #/area UrnS LPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="/[LPF]">/[LPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1968-7"><![CDATA[Bilirub Direct SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
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
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="770-8"><![CDATA[Neutrophils NFr Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>32</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.1</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.9</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2157-6"><![CDATA[CK SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>341</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1841-6"><![CDATA[Ammonia Ser-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13</value>
        <unit type="http://unitsofmeasure.org/#" value="umol/L">umol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1841-6"><![CDATA[Ammonia Ser-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12</value>
        <unit type="http://unitsofmeasure.org/#" value="umol/L">umol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5821-4"><![CDATA[WBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13945-1"><![CDATA[RBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2614-6"><![CDATA[MetHgb MFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.1</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="806-0"><![CDATA[WBC # CSF Manual]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1550</value>
        <unit type="http://unitsofmeasure.org/#" value="#/mm3">#/mm3</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26454-9"><![CDATA[RBC # CSF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="#/mm3">#/mm3</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10328-3"><![CDATA[Lymphocytes NFr CSF Manual]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>97</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10839-9"><![CDATA[Troponin I SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6.06</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="4024-6"><![CDATA[Salicylates SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>220</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>214</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13969-1"><![CDATA[CK MB SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.5</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10839-9"><![CDATA[Troponin I SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.02</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.51</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.45</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>37</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>121</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.3</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>25.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2947-0"><![CDATA[Sodium Bld-sCnc]]></name>
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
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="6298-4"><![CDATA[Potassium Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.3</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3024-7"><![CDATA[T4 Free SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/dL">ng/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11580-8"><![CDATA[TSH SerPl DL<=0.005 mU/L-aCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.002</value>
        <unit type="http://unitsofmeasure.org/#" value="mcU/mL">mcU/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="20563-3"><![CDATA[COHgb MFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.4</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="38483-4"><![CDATA[Creat Bld-mCnc]]></name>
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
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>99</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2143-6"><![CDATA[Cortis SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>37.9</value>
        <unit type="http://unitsofmeasure.org/#" value="ug/dL">ug/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2158-4"><![CDATA[CK/CK MB SerPl-cRto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value=""></unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3040-3"><![CDATA[Lipase SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>56</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1971-1"><![CDATA[Bilirub Indirect SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.3</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="6299-2"><![CDATA[BUN Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-17T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1863-0"><![CDATA[Anion Gap4 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>340</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.5</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>10.1</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.3</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>117</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>17</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>143</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.6</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>81</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.8</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.2</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
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
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.2</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.7</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2157-6"><![CDATA[CK SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>398</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2157-6"><![CDATA[CK SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>384</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.65</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>179</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>176</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>156</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>130</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>114</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>100</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13969-1"><![CDATA[CK MB SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.8</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13969-1"><![CDATA[CK MB SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.2</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10839-9"><![CDATA[Troponin I SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.04</value>
        <unit type="http://unitsofmeasure.org/#" value="ng/mL">ng/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.46</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.44</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>42</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>35</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>461</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>143</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>28.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>24.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>99</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>100</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2158-4"><![CDATA[CK/CK MB SerPl-cRto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value=""></unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-18T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>118</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>215</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>167</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>164</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>147</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>143</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>125</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>109</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.42</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>35</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>102</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>22.2</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>98</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>-1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="770-8"><![CDATA[Neutrophils NFr Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>57</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.1</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>119</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26478-8"><![CDATA[Lymphocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>24</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26485-3"><![CDATA[Monocytes NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>16</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26450-7"><![CDATA[Eosinophil NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30180-4"><![CDATA[Basophils NFr Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.1</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.5</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.94</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>106</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>24</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>139</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.6</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>80</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.6</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.5</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1648-5"><![CDATA[TB Wheal 3D p 5 TU Diam]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mm">mm</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-19T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>327</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.6</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>79</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.7</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2777-1"><![CDATA[Phosphate SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>289</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.3</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>10.6</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.98</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>102</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>29</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="19123-9"><![CDATA[Magnesium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>175</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="4092-3"><![CDATA[Vancomycin Trough SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.8</value>
        <unit type="http://unitsofmeasure.org/#" value="mcg/mL">mcg/mL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.53</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>103</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.8</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>99</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>245</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>238</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>221</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>206</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>190</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>189</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>178</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
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
  <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-20T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>79</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.8</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="6768-6"><![CDATA[ALP SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>69</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2885-2"><![CDATA[Prot SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6.8</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1751-7"><![CDATA[Albumin SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2.4</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5811-5"><![CDATA[Sp Gr Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.005</value>
        <unit type="http://unitsofmeasure.org/#" value=""></unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5803-2"><![CDATA[pH Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5804-0"><![CDATA[Prot Ur Strip-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>262</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.2</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5769-5"><![CDATA[Bacteria #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.6</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.91</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1742-6"><![CDATA[ALT SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>76</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>103</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>29</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1920-8"><![CDATA[AST SerPl-cCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>40</value>
        <unit type="http://unitsofmeasure.org/#" value="U/L">U/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.7</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.8</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5821-4"><![CDATA[WBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13945-1"><![CDATA[RBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>160</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1975-2"><![CDATA[Bilirub SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0.5</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11558-4"><![CDATA[pH Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7.4</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11557-6"><![CDATA[pCO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>43</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11556-8"><![CDATA[pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>84</value>
        <unit type="http://unitsofmeasure.org/#" value="mm[Hg]">mm[Hg]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="1959-6"><![CDATA[HCO3 Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.6</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2713-6"><![CDATA[SaO2% from pO2 Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>95</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>213</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>178</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>176</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>164</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>161</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>150</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="11555-0"><![CDATA[Base excess Bld-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>2</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-21T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>141</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>79</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.8</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>260</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.6</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.4</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5.08</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>104</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>32</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.4</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.3</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>148</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>181</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>156</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>155</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>152</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>147</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-22T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
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
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>80</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>143</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2160-0"><![CDATA[Creat SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.1</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>288</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.92</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>104</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>31</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.6</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.9</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>148</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>11</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.3</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>166</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>150</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>135</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>131</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-23T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>81</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.6</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34.1</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>275</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.1</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.57</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.1</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>100</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>31</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>141</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.3</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.8</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>113</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.6</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>147</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>120</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>114</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>103</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-24T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>10</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>81</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.1</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.7</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.8</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>296</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.1</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.59</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.8</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>28</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.6</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>102</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.5</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>50</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>167</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>162</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>113</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
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
  <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-25T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>11</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>80</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>27.4</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>34.4</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.8</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5811-5"><![CDATA[Sp Gr Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>1.014</value>
        <unit type="http://unitsofmeasure.org/#" value=""></unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5803-2"><![CDATA[pH Ur Strip]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>5.5</value>
        <unit type="http://unitsofmeasure.org/#" value="[pH]">[pH]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5804-0"><![CDATA[Prot Ur Strip-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>30</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>316</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5769-5"><![CDATA[Bacteria #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>0</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>9.7</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.68</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>100</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>29</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>136</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.6</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
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
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="5821-4"><![CDATA[WBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>6</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="13945-1"><![CDATA[RBC #/area UrnS HPF]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>63</value>
        <unit type="http://unitsofmeasure.org/#" value="/[HPF]">/[HPF]</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>119</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.8</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
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
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>234</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>115</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-26T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30428-7"><![CDATA[MCV RBC]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>79</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="10466-1"><![CDATA[Anion Gap3 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>11</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="785-6"><![CDATA[MCH RBC Qn Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>26.8</value>
        <unit type="http://unitsofmeasure.org/#" value="pg">pg</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="786-4"><![CDATA[MCHC RBC Auto-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>33.9</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="17861-6"><![CDATA[Calcium SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.6</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26515-7"><![CDATA[Platelet # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>336</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="26464-8"><![CDATA[WBC # Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.7</value>
        <unit type="http://unitsofmeasure.org/#" value="10*3/uL">10*3/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="789-8"><![CDATA[RBC # Bld Auto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>4.72</value>
        <unit type="http://unitsofmeasure.org/#" value="10*6/uL">10*6/uL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2823-3"><![CDATA[Potassium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>3.7</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2075-0"><![CDATA[Chloride SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>95</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2028-9"><![CDATA[CO2 SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>28</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2951-2"><![CDATA[Sodium SerPl-sCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>134</value>
        <unit type="http://unitsofmeasure.org/#" value="mmol/L">mmol/L</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="28542-9"><![CDATA[PMV Bld]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>8.9</value>
        <unit type="http://unitsofmeasure.org/#" value="fL">fL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="30385-9"><![CDATA[RDW RBC-Rto]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>13.6</value>
        <unit type="http://unitsofmeasure.org/#" value="%">%</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2345-7"><![CDATA[Glucose SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>122</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="3094-0"><![CDATA[BUN SerPl-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="718-7"><![CDATA[Hgb Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>12.6</value>
        <unit type="http://unitsofmeasure.org/#" value="g/dL">g/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
    <name type="http://loinc.org/codes/"  value="2339-0"><![CDATA[Glucose Bld-mCnc]]></name>
    <final>true</final>
    <result xsi:type="ResultInRange">
      <valueAndUnit>
        <value>147</value>
        <unit type="http://unitsofmeasure.org/#" value="mg/dL">mg/dL</unit>
      </valueAndUnit>
    </result>    
  </labTest>
</Lab>
""".encode())

labs.append("""
<Lab xmlns="http://indivo.org/vocab/xml/documents#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
  <labType>general</labType>

  <labTest xsi:type="SingleResultLabTest">
    <dateMeasured>2006-07-27T00:00:00Z</dateMeasured>
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

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="409622000">Acute respiratory failure</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="195949008">Chronic asthmatic bronchitis</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="34095006">Dehydration</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="44054006">Diabetes mellitus type 2</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="38341003">Essential hypertension</name>
</Problem>
""".encode())

problems.append("""
<Problem xmlns="http://indivo.org/vocab/xml/documents#">
  <dateOnset>2006-07-17T00:00:00Z</dateOnset>
  <name type="http://www.ihtsdo.org/snomed-ct/concepts/" value="55525008">Paralytic ileus</name>
</Problem>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2009-06-09</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="745752">200 ACTUAT Albuterol 0.09 MG/ACTUAT Metered Dose Inhaler [ProAir HFA]</name>
  <dose>
    <value>2</value>
    <unit type="http://unitsofmeasure.org/" value="{puff}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="4 /d">4 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>2 puffs qid prn SOB</instructions>
  </prescription>
</Medication>
""".encode())

meds.append("""
<Medication xmlns="http://indivo.org/vocab/xml/documents#">
  <dateStarted>2009-08-10</dateStarted>
  <name type="http://rxnav.nlm.nih.gov/REST/rxcui/" value="213271">sildenafil 100 MG Oral Tablet [Viagra]</name>
  <dose>
    <value>1</value>
    <unit type="http://unitsofmeasure.org/" value="{tablet}" />
  </dose>
  <frequency type="http://unitsofmeasure.org/" value="1 /d">1 /d</frequency>

  <prescription>
    <dispenseAsWritten>true</dispenseAsWritten>
    <instructions>1 daily prn ED</instructions>
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

