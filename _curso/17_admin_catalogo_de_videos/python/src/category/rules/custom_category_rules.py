class Serializer:
    __rules = {}
    __errors = []

    STRING_COMPARE = "string"
    BOOLEAN_COMPARE = "boolean"
    INTEGER_COMPARE = "integer"
    FLOAT_COMPARE = "float"
    REQUIRED_COMPARE = "required"
    MAX_LENGTH_COMPARE = "max_length"

    def __init__(self, data: any):
        self.data = data
        if "data" in self.data:
            self.data = self.data["data"]

        for key, value in self.data.items():
            self.parse_rules(key, getattr(self, key), value)

        self.validate()

    def parse_rules(self, key, rule, value):
        __rules = rule.split("|")
        self.__rules[key] = {"value": value, "rules": []}
        for __rule in __rules:
            self.__rules[key]["rules"].append(__rule.split(":"))

    def validate(self):
        for rule in self.__rules.items():
            for __rule in rule[1]["rules"]:
                [rule_name, *rule_value] = __rule
                compare_value = rule[1]["value"]
                compare_key = rule[0]
                self.apply_rule(rule_name, rule_value, compare_key, compare_value)

    def apply_rule(self, rule_name, rule_value, compare_key, compare_value):
        if rule_name == self.STRING_COMPARE:
            self.string(compare_key, compare_value)

        if rule_name == self.REQUIRED_COMPARE:
            self.required(compare_key, compare_value)

        if rule_name == self.BOOLEAN_COMPARE:
            self.boolean(compare_key, compare_value)

        if rule_name == self.MAX_LENGTH_COMPARE:
            self.max_length(compare_key, compare_value, int(rule_value[0]))

    def string(self, key: str, value: str) -> None:
        if value is not None and not isinstance(value, str):
            self.__errors.append({"message": f"The {key} must be a string"})

    def required(self, key: str, value: str) -> None:
        if value is None or value == "":
            self.__errors.append({"message": f"The {key} is required"})

    def max_length(self, key, value, max_length: int) -> None:
        if value is not None and len(value) > max_length:
            self.__errors.append(
                {"message": f"The {key} must be less than {max_length} characters"}
            )

    def boolean(self, key, value) -> None:
        if value is not None and value is not True and value is not False:
            self.__errors.append({"message": f"The {key} must be a boolean"})

    @property
    def is_valid(self):
        return not self.__errors

    @property
    def errors(self):
        return self.__errors


class CustomCategoryRules(Serializer):
    name = "string|required|max_length:255"
    description = "required|max_length:5"
    is_active = "boolean|required"
    created_at = "required"
