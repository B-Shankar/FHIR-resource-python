from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address

# Instance of Patient Resource
new_patient = Patient()

# Setting data in Instance created
new_patient.name = [HumanName(use="official", text="Bhimashankar Holkundi", family="Holkundi", given=["Bhimashankar"], prefix=["Mr."])]
new_patient.gender = "male"
new_patient.telecom = [ContactPoint(system="email", value="learn.bhimashankar@gmail.com"), ContactPoint(system="phone", value="(55) 555-5555")]
new_patient.address = [Address(use="home", city="Sultanpur", district="Gulbarga", state="Karnataka", country="India", postalCode="585109")]

# Printing the Validated Patient Resource
print(new_patient.model_dump_json(indent=2))