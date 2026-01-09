import pytest
from fizzbuzz import fizzbuzz, fizzbuzz_range


class TestFizzBuzz:
    """fizzbuzz関数のテストクラス"""

    def test_fizzbuzz_normal_number(self):
        """通常の数値を渡した場合"""
        assert fizzbuzz(1) == 1
        assert fizzbuzz(2) == 2
        assert fizzbuzz(4) == 4

    def test_fizzbuzz_divisible_by_3(self):
        """3で割り切れる数値を渡した場合"""
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(6) == "Fizz"
        assert fizzbuzz(9) == "Fizz"

    def test_fizzbuzz_divisible_by_5(self):
        """5で割り切れる数値を渡した場合"""
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(10) == "Buzz"
        assert fizzbuzz(20) == "Buzz"

    def test_fizzbuzz_divisible_by_15(self):
        """15で割り切れる数値を渡した場合"""
        assert fizzbuzz(15) == "FizzBuzz"
        assert fizzbuzz(30) == "FizzBuzz"
        assert fizzbuzz(45) == "FizzBuzz"

    def test_fizzbuzz_type_error_string(self):
        """文字列を渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz("3")

    def test_fizzbuzz_type_error_float(self):
        """浮動小数点数を渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz(3.5)

    def test_fizzbuzz_type_error_none(self):
        """Noneを渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz(None)

    def test_fizzbuzz_value_error_zero(self):
        """0を渡した場合にValueErrorが発生"""
        with pytest.raises(ValueError, match="引数は正の整数である必要があります"):
            fizzbuzz(0)

    def test_fizzbuzz_value_error_negative(self):
        """負の数を渡した場合にValueErrorが発生"""
        with pytest.raises(ValueError, match="引数は正の整数である必要があります"):
            fizzbuzz(-1)
        with pytest.raises(ValueError, match="引数は正の整数である必要があります"):
            fizzbuzz(-10)

    def test_fizzbuzz_type_error_bool(self):
        """bool型を渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz(True)
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz(False)

    def test_fizzbuzz_type_error_list(self):
        """リストを渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz([1, 2, 3])

    def test_fizzbuzz_type_error_dict(self):
        """辞書を渡した場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="引数は整数である必要があります"):
            fizzbuzz({"num": 3})

    def test_fizzbuzz_overflow_error_large_number(self):
        """非常に大きな数値を渡した場合にOverflowErrorが発生"""
        with pytest.raises(OverflowError, match="引数が大きすぎます"):
            fizzbuzz(10**9 + 1)
        with pytest.raises(OverflowError, match="引数が大きすぎます"):
            fizzbuzz(10**15)

    def test_fizzbuzz_edge_case_max_valid(self):
        """有効な最大値をテスト"""
        result = fizzbuzz(10**9)
        assert result == "Buzz"  # 10^9は5で割り切れる


class TestFizzBuzzRange:
    """fizzbuzz_range関数のテストクラス"""

    def test_fizzbuzz_range_1_to_15(self):
        """1から15までの範囲のテスト"""
        expected = [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            14,
            "FizzBuzz",
        ]
        assert fizzbuzz_range(1, 15) == expected

    def test_fizzbuzz_range_single_value(self):
        """単一の値の範囲のテスト"""
        assert fizzbuzz_range(3, 3) == ["Fizz"]
        assert fizzbuzz_range(5, 5) == ["Buzz"]

    def test_fizzbuzz_range_type_error_start(self):
        """startが文字列の場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="start と end は整数である必要があります"):
            fizzbuzz_range("1", 10)

    def test_fizzbuzz_range_type_error_end(self):
        """endが文字列の場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="start と end は整数である必要があります"):
            fizzbuzz_range(1, "10")

    def test_fizzbuzz_range_value_error_zero_start(self):
        """startが0の場合にValueErrorが発生"""
        with pytest.raises(
            ValueError, match="start と end は正の整数である必要があります"
        ):
            fizzbuzz_range(0, 10)

    def test_fizzbuzz_range_value_error_negative_start(self):
        """startが負の数の場合にValueErrorが発生"""
        with pytest.raises(
            ValueError, match="start と end は正の整数である必要があります"
        ):
            fizzbuzz_range(-1, 10)

    def test_fizzbuzz_range_value_error_start_greater_than_end(self):
        """startがendより大きい場合にValueErrorが発生"""
        with pytest.raises(
            ValueError, match="start .* は end .* より小さい必要があります"
        ):
            fizzbuzz_range(10, 5)

    def test_fizzbuzz_range_type_error_bool_start(self):
        """startがbool型の場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="start と end は整数である必要があります"):
            fizzbuzz_range(True, 10)

    def test_fizzbuzz_range_type_error_bool_end(self):
        """endがbool型の場合にTypeErrorが発生"""
        with pytest.raises(TypeError, match="start と end は整数である必要があります"):
            fizzbuzz_range(1, False)

    def test_fizzbuzz_range_overflow_error_large_range(self):
        """範囲が大きすぎる場合にOverflowErrorが発生"""
        with pytest.raises(OverflowError, match="範囲が大きすぎます"):
            fizzbuzz_range(1, 10**6 + 1)

    def test_fizzbuzz_range_edge_case_max_valid_range(self):
        """有効な最大範囲の境界テスト"""
        # 範囲が10^6個の場合は成功する
        result = fizzbuzz_range(1, 10**6)
        assert len(result) == 10**6
        assert result[0] == 1
        assert result[2] == "Fizz"
        assert result[-1] == "Buzz"  # 10^6は5で割り切れる

    def test_fizzbuzz_range_value_error_zero_end(self):
        """endが0の場合にValueErrorが発生"""
        with pytest.raises(
            ValueError, match="start と end は正の整数である必要があります"
        ):
            fizzbuzz_range(1, 0)
