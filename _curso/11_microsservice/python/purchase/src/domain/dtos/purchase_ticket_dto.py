from pydantic import BaseModel


class PurchaseTicketDTO(BaseModel):
    ticket_code: str
    participant_name: str
    participant_email: str
    event_code: str
    credit_card_number: str
    credit_card_cvv: str
    credit_card_exp_date: str
