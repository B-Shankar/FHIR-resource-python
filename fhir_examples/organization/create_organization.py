from fhir.resources.organization import Organization
from fhir.resources.extendedcontactdetail import ExtendedContactDetail
from fhir.resources.virtualservicedetail import VirtualServiceDetail
from fhir.resources.coding import Coding
from fhir.resources.availability import Availability

organization = Organization(
    name="Good Life Clinic",
    active=True
)

contact = ExtendedContactDetail(
    purpose={"text": "Reception"},
    telecom=[{"system": "phone", "value": "+1-456789"}]
)

organization.contact = [contact]

# vsd = VirtualServiceDetail(
#     channelType=Coding(
#         system="http://terminology.hl7.org/CodeSystem/service-channel-type",
#         code="video",
#         display="Video Conference"
#     ),
#     addressString="https://meet.example.com/doctor123"
# )
#
# organization.virtualService = [vsd]

# availability = Availability(
#     availableTime=[
#         {
#             "daysOfWeek": ["mon", "tue", "wed", "thu", "fri"],
#             "availableStartTime": "09:00:00",
#             "availableEndTime": "17:00:00"
#         }
#     ]
# )
#
# organization.availability = [availability]

print(organization.json(indent=2))
