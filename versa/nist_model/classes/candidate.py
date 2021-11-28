from datetime import date
from typing import Literal, Optional, List

from pydantic import BaseModel, Field

from .contact_information import ContactInformation
from .external_identifier import ExternalIdentifier
from .intl_text import InternationalizedText
from ..enums.nist import PostElectionStatusEnum, PreElectionStatusEnum
from ..enums.type_tag import TypeTags
from ..util import fieldname_alias, ObjectId, ObjectIdRef


class Candidate(BaseModel):
    obj_type: Literal[TypeTags.CandidateTag] = Field(TypeTags.CandidateTag)
    obj_id: ObjectId

    ballot_name: InternationalizedText
    campaign_slogan: Optional[InternationalizedText]
    contact_information: Optional[ContactInformation]
    external_identifier: List[ExternalIdentifier] = []
    file_date: Optional[date]
    is_incumbent: bool = False
    is_top_ticket: bool = False
    party_id: Optional[ObjectIdRef]
    person_id: Optional[ObjectIdRef]
    post_election_status: Optional[PostElectionStatusEnum]
    pre_election_status: Optional[PreElectionStatusEnum]

    class Config:
        alias_generator = fieldname_alias
