from src.__shared.domain.serializer import CustomSerializer


class CustomCategoryRules(CustomSerializer):
    name = "string|required|max_length:255"
    description = "required|max_length:5"
    is_active = "boolean|required"
    created_at = "required"
