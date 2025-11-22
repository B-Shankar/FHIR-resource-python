import json

from fhir.resources.patient import Patient

# Patient Object Data: JSON
patient_obj_data = {
  "resourceType": "Patient",
  "name": [
    {
      "use": "official",
      "text": "Bhimashankar Holkundi",
      "family": "Holkundi",
      "given": [
        "Bhimashankar"
      ],
      "prefix": [
        "Mr."
      ]
    }
  ],
  "telecom": [
    {
      "system": "email",
      "value": "learn.bhimashankar@gmail.com"
    },
    {
      "system": "phone",
      "value": "(55) 555-5555"
    }
  ],
  "gender": "male",
  "address": [
    {
      "use": "home",
      "city": "Sultanpur",
      "district": "Gulbarga",
      "state": "Karnataka",
      "postalCode": "585109",
      "country": "India"
    }
  ]
}

validate_patient = Patient.model_validate_json(json.dumps(patient_obj_data))
print("Validated Patient:", validate_patient.model_dump_json(indent=2))