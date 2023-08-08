from ...utils import get_graphql_content

PROMOTION_CREATE_MUTATION = """
mutation CreatePromotion ($name: String!,
$rules:[PromotionRuleInput!]!) {
  promotionCreate(
    input: {
        name: $name,
        rules:$rules,
        }
  )
  {errors {
    message
    field
    }
  promotion {
    name
    id
    rules {
        cataloguePredicate
        rewardValueType
        rewardValue
        }
        }
    }
}
"""


def create_promotion(
    staff_api_client,
    promotion_name,
    promotion_rules,
):
    variables = {"name": promotion_name, "rules": promotion_rules}

    response = staff_api_client.post_graphql(
        PROMOTION_CREATE_MUTATION,
        variables,
    )
    content = get_graphql_content(response)

    data = content["data"]["promotionCreate"]
    assert data["promotion"]["id"] is not None

    assert data["promotion"]["rules"] == promotion_rules

    return data
