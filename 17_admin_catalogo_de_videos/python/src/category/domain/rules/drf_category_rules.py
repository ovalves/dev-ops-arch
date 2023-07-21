from rest_framework import serializers
from src.__shared.domain.validators.drf_validator_adapter import (
    DRFStrictBooleanField,
    DRFStrictCharField,
)


class DRFCategoryRules(serializers.Serializer):
    name = DRFStrictCharField(max_length=255)
    description = DRFStrictCharField(required=False, allow_null=True, allow_blank=True)
    is_active = DRFStrictBooleanField(required=False)
    created_at = serializers.DateTimeField(required=False)
