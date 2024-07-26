import pytest
import allure
from utils.docker import run_docker_container
from utils.assertions import assert_equal


@allure.feature("Multiply Operation")
class TestMultiplyOperation:

    @pytest.mark.parametrize(
        "operation,expected_result",
        [
            ("123456 0", 0),
            ("5 5", 25),
            ("-10 -10", 100),
            ("5.4 5.4", 29.16),
        ],
    )
    def test_multiply_operation(self, operation, expected_result):
        result = run_docker_container(f"multiply {operation}")
        assert_equal(result, expected_result)
