import os
import data

PRD = 'prd'

def test_document_processing(IndivoClient):
  try:
    admin_client = IndivoClient(data.machine_app_email, data.machine_app_secret)
    admin_client.set_app_id(data.app_email)
    record_id = admin_client.create_record(data=data.demographics).response[PRD]['Record'][0]
    admin_client.set_record_owner(data=data.account['account_id'])

    # SZ: DP shouldn't process app-specific documents
    user_client = IndivoClient(data.app_email, data.app_secret)
    user_client.set_app_id(data.app_email)
    user_client.post_app_document(data=data.measurement00)
    user_client.read_app_document()

    chrome_client = IndivoClient('chrome', 'chrome')
    chrome_client.create_session(data.account)
    chrome_client.read_record(record_id=record_id)

    # SZ: For testing io
    #response = chrome_client.post_document(data=data.lab01, debug=True)
    #chrome_client.read_labs(debug=True)

    doc_id = chrome_client.post_document(data=data.measurement00).response[PRD]['Document'][0]
    chrome_client.read_document()
    chrome_client.read_document_meta()

    chrome_client.replace_document(document_id = doc_id, data=data.measurement01)
    # SZ: Should return 404, can't replace document of an already replaced document
    chrome_client.replace_document(document_id = doc_id, data=data.measurement01)

    medical_documents = [ 
                          data.immunization, 
                          data.lab,
                          data.measurement00,
                          data.measurement01,
                          data.measurement02,
                          data.allergy,
                          data.equipment,
                          data.equipment02,
                          data.vital_sign,
                          data.vital_sign,
                          data.vital_sign,
                          data.procedure,
                          data.procedure_no_code,
                          data.clinical_note
                        ]

    for md in medical_documents:
      response = chrome_client.post_document(data=md)
      if response.response['response_status'] != 200:
        raise Exception("problem posting a document: %s" + response.response['response_data'])

    reports = [ 
                chrome_client.read_equipment(),
                chrome_client.read_procedures(),
                #chrome_client.read_measurements(lab_code='HBA1C', parameters={'limit':1})
                chrome_client.read_measurements(lab_code='HBA1C'),
                chrome_client.read_ccr_experimental(),
              ]

    for report in reports:
      response = report.response
      if response['response_status'] != 200:
        raise Exception, response
  except Exception, e:
    return False, e
  return True

