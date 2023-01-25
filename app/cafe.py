import datetime
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        if (not visitor.get("wearing_a_mask")
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
