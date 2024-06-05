from uuid import UUID

import pytest
from pydantic import ValidationError
from src.infra.schemas.product import ProductIn
from src.tests.factories import product_data


def tests_schemas_return_success():
    product = ProductIn.model_validate(product_data)
    assert product.name == "Iphone 14 pro Max"
    assert isinstance(product.id, UUID)


def tests_schemas_return_raise():
    data = {
        'name': "Iphone 14 pro Max",
        'quantity': 10,
        'price': 8.500,
    }
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0]
