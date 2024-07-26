import pytest
import allure
from utils.docker import run_docker_container
from utils.assertions import assert_equal


@allure.feature("Divide Operation")
class TestDivideOperation:

    @pytest.mark.parametrize(
        "operation,expected_result",
        [
            ("10 2", 5),
            ("1000000000 3", 333333333.3333333),
        ],
    )
    def test_divide_operation(self, operation, expected_result):
        result = run_docker_container(f"divide {operation}")
        assert_equal(result, expected_result)
