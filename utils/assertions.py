from assertpy import assert_that


def assert_equal(current_result: str, expected_result: str):
    assert_that(str(current_result)).contains(f"Result: {expected_result}")
