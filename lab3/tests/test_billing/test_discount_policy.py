from lab3.module_billing.discount_policy import DiscountPolicy

def test_apply():
    policy = DiscountPolicy("DP001", "Senior", 0.15)
    discounted = policy.apply(200.0)
    assert discounted == 170.0