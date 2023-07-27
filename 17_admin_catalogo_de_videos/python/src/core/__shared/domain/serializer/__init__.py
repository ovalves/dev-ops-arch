from typing import Dict, List


class CustomSerializer:
    __rules: Dict = {}
    __errors: List = []

    STRING_COMPARE: str = "string"
    BOOLEAN_COMPARE: str = "boolean"
    INTEGER_COMPARE: str = "integer"
    FLOAT_COMPARE: str = "float"
    REQUIRED_COMPARE: str = "required"
    MAX_LENGTH_COMPARE: str = "max_length"

    def __init__(self, data: any):
        self.data = data
        if "data" in self.data:
            self.data = self.data["data"]

        for key, value in self.data.items():
            try:
                self.parse_rules(key, getattr(self, key), value)
            except Exception:
                continue

        self.validate()

    @property
    def is_valid(self) -> bool:
        return not self.__errors

    @property
    def errors(self) -> List:
        return self.__errors

    def parse_rules(self, key: str, rule: List, value: any) -> None:
        __rules = rule.split("|")
        self.__rules[key] = {"value": value, "rules": []}
        for __rule in __rules:
            self.__rules[key]["rules"].append(__rule.split(":"))

    def validate(self) -> None:
        for rule in self.__rules.items():
            for __rule in rule[1]["rules"]:
                [rule_name, *rule_value] = __rule
                compare_value = rule[1]["value"]
                compare_key = rule[0]
                self.__apply_rule(rule_name, rule_value, compare_key, compare_value)

    def __apply_rule(self, rule_name, rule_value, compare_key, compare_value) -> None:
        if rule_name == self.STRING_COMPARE:
            self.__string(compare_key, compare_value)

        if rule_name == self.REQUIRED_COMPARE:
            self.__required(compare_key, compare_value)

        if rule_name == self.BOOLEAN_COMPARE:
            self.__boolean(compare_key, compare_value)

        if rule_name == self.MAX_LENGTH_COMPARE:
            self.__max_length(compare_key, compare_value, int(rule_value[0]))

    def __string(self, key: str, value: str) -> None:
        if value is not None and not isinstance(value, str):
            self.__errors.append({"message": f"The {key} must be a string"})

    def __required(self, key: str, value: str) -> None:
        if value is None or not value:
            self.__errors.append({"message": f"The {key} is required"})

    def __max_length(self, key, value, max_length: int) -> None:
        if value is not None and len(value) > max_length:
            self.__errors.append(
                {"message": f"The {key} must be less than {max_length} characters"}
            )

    def __boolean(self, key, value) -> None:
        if value is not None and value is not True and value is not False:
            self.__errors.append({"message": f"The {key} must be a boolean"})
