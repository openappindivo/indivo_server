<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:Lab">
    <facts>
      <fact>
        <date_measured><xsl:value-of select='indivodoc:dateMeasured/text()' /></date_measured>
        <lab_type><xsl:value-of select='indivodoc:labType/text()' /></lab_type>
        <lab_name><xsl:value-of select='indivodoc:laboratory/indivodoc:name/text()' /></lab_name>
        <lab_address><xsl:value-of select='indivodoc:laboratory/indivodoc:address/text()' /></lab_address>
        <lab_comments><xsl:value-of select='indivodoc:comments/text()' /></lab_comments>

	<xsl:if test="indivodoc:labPanel">
	  <first_panel_name><xsl:value-of select='indivodoc:labPanel/indivodoc:name/text()' /></first_panel_name>
	</xsl:if>

	<xsl:choose>
	  <xsl:when test="indivodoc:labTest">
	    <first_lab_test_name><xsl:value-of select='indivodoc:labTest/indivodoc:name/text()' /></first_lab_test_name>
	    <xsl:apply-templates select='indivodoc:labTest[1]/indivodoc:result' />
	  </xsl:when>
	  <xsl:otherwise>
<!--	    <xsl:if test="count(indivodoc:labPanel/indivodoc:labTest) = 1">
	      <first_lab_test_name><xsl:value-of select='indivodoc:labPanel/indivodoc:labTest/indivodoc:name/text()' /></first_lab_test_name>
	      <xsl:apply-templates select='indivodoc:labPanel/indivodoc:labTest[1]/indivodoc:result' />
	    </xsl:if>-->
	  </xsl:otherwise>
	</xsl:choose>
      </fact>

      <xsl:apply-templates select='indivodoc:labTest' />

      <xsl:apply-templates select='indivodoc:labPanel/indivodoc:labTest' />

    </facts>
  </xsl:template>

  <xsl:template match="indivodoc:labTest">
    <fact>
      <type>labresult</type>
      <date_measured><xsl:value-of select='indivodoc:dateMeasured/text()' /></date_measured>
      <name><xsl:value-of select='indivodoc:name/text()' /></name>
      <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
      <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
      <is_final><xsl:value-of select='indivodoc:final/text()' /></is_final>
      <xsl:if test="indivodoc:result/indivodoc:valueAndUnit">
	<result_value>
	  <xsl:choose>
	    <xsl:when test="indivodoc:result/indivodoc:valueAndUnit/indivodoc:value">
	      <xsl:value-of select="indivodoc:result/indivodoc:valueAndUnit/indivodoc:value/text()" />
	    </xsl:when>
	    <xsl:otherwise>
	      <xsl:value-of select="indivodoc:result/indivodoc:valueAndUnit/indivodoc:textValue/text()" />
	    </xsl:otherwise>
	  </xsl:choose>
	</result_value>
	<result_unit><xsl:choose><xsl:when test='indivodoc:result/indivodoc:valueAndUnit/indivodoc:unit/text()'><xsl:value-of select='indivodoc:result/indivodoc:valueAndUnit/indivodoc:unit/text()' /></xsl:when><xsl:otherwise><xsl:value-of select='indivodoc:result/indivodoc:valueAndUnit/indivodoc:unit/@value' /></xsl:otherwise></xsl:choose></result_unit>
	<result_unit_type><xsl:value-of select='indivodoc:result/indivodoc:valueAndUnit/indivodoc:unit/@type' /></result_unit_type>
	<result_unit_value><xsl:value-of select='indivodoc:result/indivodoc:valueAndUnit/indivodoc:unit/@value' /></result_unit_value>
	<xsl:if test="indivodoc:result/indivodoc:flag">
	  <flag_type><xsl:value-of select='indivodoc:result/indivodoc:flag/@type' /></flag_type>
	  <flag_value><xsl:value-of select='indivodoc:result/indivodoc:flag/@value' /></flag_value>
	</xsl:if>
      </xsl:if>
      <xsl:call-template name="ranges">
	<xsl:with-param name="result" select="indivodoc:result" />
      </xsl:call-template>
    </fact>
  </xsl:template>

  <xsl:template match="indivodoc:result">
    <first_lab_test_value>
    <xsl:if test="indivodoc:valueAndUnit">
      <xsl:choose>
	<xsl:when test="indivodoc:valueAndUnit/indivodoc:value">
	  <xsl:value-of select="indivodoc:valueAndUnit/indivodoc:value/text()" />  <xsl:value-of select="indivodoc:valueAndUnit/indivodoc:unit/text()" />
	</xsl:when>
	<xsl:otherwise>
	  <xsl:value-of select="indivodoc:valueAndUnit/indivodoc:textValue/text()" />
	</xsl:otherwise>
      </xsl:choose>
    </xsl:if>
    <xsl:if test="indivodoc:value">
      <xsl:value-of select="indivodoc:value" />
    </xsl:if>
    </first_lab_test_value>
    
    <xsl:if test="indivodoc:valueAndUnit or indivodoc:value">
      <xsl:call-template name="ranges">
	<xsl:with-param name="result" select="." />
      </xsl:call-template>
    </xsl:if>
  </xsl:template>

  <xsl:template name="ranges">
    <xsl:param name="result" />
    <xsl:if test="$result/indivodoc:normalRange/indivodoc:minimum">
      <normal_range_minimum><xsl:value-of select="$result/indivodoc:normalRange/indivodoc:minimum/text()"/>
	<xsl:if test="$result/indivodoc:normalRange/indivodoc:unit">
	  <xsl:value-of select="$result/indivodoc:normalRange/indivodoc:unit/@indivodoc:abbrev"/>
	</xsl:if>
      </normal_range_minimum>
    </xsl:if>
    
    <xsl:if test="$result/indivodoc:normalRange/indivodoc:maximum">
      <normal_range_maximum><xsl:value-of select="$result/indivodoc:normalRange/indivodoc:maximum/text()"/>
	<xsl:if test="$result/indivodoc:normalRange/indivodoc:unit">
	  <xsl:value-of select="$result/indivodoc:normalRange/indivodoc:unit/@indivodoc:abbrev"/>
	</xsl:if>
      </normal_range_maximum>
    </xsl:if>
    
    <xsl:if test="$result/indivodoc:nonCriticalRange/indivodoc:minimum">
      <non_critical_range_minimum><xsl:value-of select="$result/indivodoc:nonCriticalRange/indivodoc:minimum/text()"/>
	<xsl:if test="$result/indivodoc:nonCriticalRange/indivodoc:unit">
	  <xsl:value-of select="$result/indivodoc:nonCriticalRange/indivodoc:unit/@indivodoc:abbrev"/>
	</xsl:if>
      </non_critical_range_minimum>
    </xsl:if>
    
    <xsl:if test="$result/indivodoc:nonCriticalRange/indivodoc:maximum">
      <non_critical_range_maximum><xsl:value-of select="$result/indivodoc:nonCriticalRange/indivodoc:maximum/text()"/>
	<xsl:if test="$result/indivodoc:nonCriticalRange/indivodoc:unit">
	  <xsl:value-of select="$result/indivodoc:nonCriticalRange/indivodoc:unit/@indivodoc:abbrev"/>
	</xsl:if>
      </non_critical_range_maximum>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
