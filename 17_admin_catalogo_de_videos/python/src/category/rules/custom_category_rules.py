from __shared.rules.serializer import Serializer


class CustomCategoryRules(Serializer):
    name = "string|required|max_length:255"
    description = "required|max_length:5"
    is_active = "boolean|required"
    created_at = "required"
