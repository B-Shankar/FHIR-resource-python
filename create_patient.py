from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

patient_obj = {
    "resourceType": "Patient",
    "name": "Bhimashankar Holkundi",
    "gender": "male",
    "address": "India",
}

# Patient Resource As per HL7 FHIR Release 5
patient_data = {
    "resourceType": "Patient",
    "name" : [{
        "use" : "official",
        "family" : "Holkundi",
        "given" : ["Bhimashankar"]
    }],
    "gender" : "male",
    "birthDate" : "1974-12-25",
    "address": [{
        "use": "home",
        "type": "both",
        "text": "534 Erewhon St PeasantVille, Rainbow, Vic  3999",
        "line": ["534 Erewhon St"],
        "city": "PleasantVille",
        "district": "Rainbow",
        "state": "Vic",
        "postalCode": "3999",
    }]
}

print("\nPatient Object:", patient_obj)

# Verifying the object FHIR Patient Resource
patient_resource = Patient(**patient_data)
print("\nPatient Resource:", patient_resource)
print("\nPatient Resource JSON:", patient_resource.model_dump_json(indent=2))

# Create HumanName object
human_name = HumanName(use="official", text="Bhimashankar Holkundi", family="Holkundi", given=["Bhimashankar"])

print("\nHumanName:", human_name)
print("\nHumanName JSON:", human_name.model_dump_json(indent=2))

patient_data.update({
    "name": [human_name.model_dump()],
})

print("\nHumanName with Patient Resource:", Patient(**patient_data))
print("\nHumanName with Patient Resource JSON:", Patient(**patient_data).model_dump_json(indent=2))