import json

from fhir.resources.practitioner import Practitioner

Practitioner_Obj = {
  "resourceType": "Practitioner",
  "active": True,
  "name": [
    {
      "family": "Doe",
      "given": [
        "John"
      ],
      "prefix": [
        "Dr"
      ]
    }
  ],
  "address": [
    {
      "city": "New York",
      "postalCode": "10001",
      "country": "USA"
    }
  ],
  "qualification": [
    {
      "code": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0360",
            "code": "MD",
            "display": "Doctor of Medicine"
          }
        ],
        "text": "Medical Doctor"
      }
    }
  ]
}

print(Practitioner.model_validate_json(json.dumps(Practitioner_Obj)))
print("JSON:", Practitioner.model_validate_json(json.dumps(Practitioner_Obj)).model_dump_json(indent=2))