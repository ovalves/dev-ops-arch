from dataclasses import dataclass
from domain.entity.event import Event

@dataclass()
class Ticket:
    event_code: str
    total: int
    status: str

    def __init__(
        self,
        ticket_code: str,
        participant_name: str,
        participant_email: str,
        credit_card_number: str,
        credit_card_cvv: str,
        credit_card_expire: str,
        event: Event
    ):
        self.event_code = event.code
        self.total = event.price
        self.status = "waiting_payment"
