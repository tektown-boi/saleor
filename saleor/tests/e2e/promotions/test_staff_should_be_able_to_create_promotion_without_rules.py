import pytest

from ..utils import assign_permissions
from .utils.promotion_create import create_promotion


@pytest.mark.e2e
def test_staff_should_be_able_to_create_promotion_without_rules_CORE_2101(
    e2e_staff_api_client,
    permission_manage_discounts,
):
    # Before
    permissions = [permission_manage_discounts]
    assign_permissions(e2e_staff_api_client, permissions)

    # Step 1 - Create a promotion
    promotion_name = "test promotion"
    rules = []
    promotion_data = create_promotion(e2e_staff_api_client, promotion_name, rules)

    assert promotion_data["errors"] == []
    assert promotion_data["promotion"]["id"] is not None
    assert promotion_data["promotion"]["name"] == promotion_name
    assert promotion_data["promotion"]["rules"] == []
