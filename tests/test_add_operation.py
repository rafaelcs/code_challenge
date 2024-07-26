import pytest
import allure
from utils.docker import run_docker_container
from utils.assertions import assert_equal


@allure.feature("Add Operation")
class TestAddOperation:

    @pytest.mark.parametrize(
        "operation,expected_result",
        [
            ("3 5", 8),
            ("0.3 0.1", 0.4),
            ("-2 -3", -5),
            ("-10.0 -24.40", -34.4),
            ("-000 -301.342", -301.342),
            ("1111111111111111 2", 1111111111111113),
            ("1111111111111111 100.34", 1111111111111211.34),
            ("200.340 1111111111111111.30", 1111111111111311.64),
            ("2e20 -3e40", -29999999999999999999800000000000000000000),
            ("1e30 -1", 999999999999999999999999999999),
            ("0.0 -0.0", 0.0),
        ],
    )
    def test_add_operation(self, operation, expected_result):
        result = run_docker_container(f"add {operation}")
        assert_equal(result, expected_result)
