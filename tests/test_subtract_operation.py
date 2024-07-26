import pytest
import allure
from utils.docker import run_docker_container
from utils.assertions import assert_equal


@allure.feature("Subtract Operation")
class TestSubtractOperation:

    @pytest.mark.parametrize(
        "operation,expected_result",
        [
            ("10 5", 5),
            ("1.000000000000001 1.000000000000000", 1.1102230246251565e-15),
            ("-10 -10", 0),
            ("-10.45 -32.34", 21.89),
            ("5 10", -5),
            ("1000000000 1", 999999999),
        ],
    )
    def test_subtract_operation(self, operation, expected_result):
        result = run_docker_container(f"subtract {operation}")
        assert_equal(result, expected_result)
