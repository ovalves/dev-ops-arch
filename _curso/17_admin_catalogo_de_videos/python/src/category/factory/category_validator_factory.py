from category.validators.category_validator import (
    DRFCategoryValidator,
    CustomCategoryValidator,
)


class CategoryValidatorFactory:  # pylint: disable=too-few-public-methods
    @staticmethod
    def create():
        return DRFCategoryValidator()

    @staticmethod
    def custom():
        return CustomCategoryValidator()
