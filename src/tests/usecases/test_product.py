import pytest
from uuid import UUID
from typing import List
from src.usecases.product import product_use_case
from src.infra.schemas.product import ProductOut
from src.infra.exceptions.exceptions import NotFoundException


async def test_create_product_use_cases_should_return_success(product_in):
    result = await product_use_case.create(body=product_in)
    assert isinstance(result, ProductOut)


async def test_get_product_use_cases_should_return_success(product_id):
    result = await product_use_case.get(id=UUID("061a5b57-34c0-420c-a2d2-d80ab890356b"))
    assert isinstance(result, ProductOut)


async def test_get_product_use_cases_should_return_not_found(product_id):
    with pytest.raises(NotFoundException) as err:
        await product_use_case.get(id=UUID("061a5b57-34c0-420c-a2d2-d80ab890356b"))

    assert err.value.message == 'PRODUCT_NOT_FOUND: 061a5b57-34c0-420c-a2d2-d80ab890356b'


async def test_list_product_use_cases_should_return_not_found(product_id):
    result = await product_use_case.list()

    assert isinstance(result, List)


async def test_update_product_use_cases_should_return_success(product_up):
    result = await product_use_case.update(
        id=UUID("061a5b57-34c0-420c-a2d2-d80ab890356b"),
        body=product_up
    )
    assert isinstance(result, ProductOut)


async def test_delete_product_use_cases_should_return_success(product_up):
    result = await product_use_case.delete(id=UUID("061a5b57-34c0-420c-a2d2-d80ab890356b"))
    assert isinstance(result, ProductOut)
