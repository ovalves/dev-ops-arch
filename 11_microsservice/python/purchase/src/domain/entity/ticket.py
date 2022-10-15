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
        event: Event,
    ):
        self.event_code = event.code
        self.total = event.price
        self.status = "waiting_payment"
        self.ticket_code = ticket_code
        self.participant_name = participant_name
        self.participant_email = participant_email
        self.credit_card_number = credit_card_number
        self.credit_card_cvv = credit_card_cvv
        self.credit_card_expire = credit_card_expire
