from fhir.resources.practitioner import Practitioner
from fhir.resources.humanname import HumanName
from fhir.resources.address import Address
from fhir.resources.practitioner import PractitionerQualification
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding

# Create practitioner
practitioner = Practitioner(
    active=True,
    name=[HumanName(family="Doe", given=["John"], prefix=["Dr"])],
    address=[Address(city="New York", country="USA", postalCode="10001")]
)

# Add qualification
qualification = PractitionerQualification(
    code=CodeableConcept(
        coding=[
            Coding(
                system="http://terminology.hl7.org/CodeSystem/v2-0360",
                code="MD",
                display="Doctor of Medicine"
            )
        ],
        text="Medical Doctor"
    )
)

practitioner.qualification = [qualification]

print(practitioner.model_dump_json(indent=2))
