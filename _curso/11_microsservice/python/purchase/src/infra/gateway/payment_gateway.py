from dataclasses import dataclass

@dataclass()
class Input:
    external_code: str
    credit_card_number: str
    credit_card_cvv: str
    credit_card_exp_date: str
    total: int

@dataclass()
class Output:
    external_code: str
    success: bool

@dataclass()
class PaymentGateway:
    http_client: None

    def execute(self, input: Input) -> Output:
        return self.http_client.post("http://localhost:5001/transactions", input)
