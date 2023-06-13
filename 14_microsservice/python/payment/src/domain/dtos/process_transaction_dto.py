from pydantic import BaseModel


class ProcessTransactionDTO(BaseModel):
    external_code: str
    credit_card_number: str
    credit_card_cvv: str
    credit_card_exp_date: str
    total: int
