import pytest
from fizzbuzz import fizzbuzz


class TestFizzBuzz:
    """Test suite for the FizzBuzz function"""

    def test_fizzbuzz_single_number(self):
        """Test FizzBuzz with a single number"""
        result = fizzbuzz(1)
        assert result == ["1"]

    def test_fizzbuzz_with_fizz(self):
        """Test that multiples of 3 return Fizz"""
        result = fizzbuzz(3)
        assert result[2] == "Fizz"  # 3 is Fizz

    def test_fizzbuzz_with_buzz(self):
        """Test that multiples of 5 return Buzz"""
        result = fizzbuzz(5)
        assert result[4] == "Buzz"  # 5 is Buzz

    def test_fizzbuzz_with_fizzbuzz(self):
        """Test that multiples of 15 return FizzBuzz"""
        result = fizzbuzz(15)
        assert result[14] == "FizzBuzz"  # 15 is FizzBuzz

    def test_fizzbuzz_sequence(self):
        """Test FizzBuzz for first 15 numbers"""
        result = fizzbuzz(15)
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
            "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        assert result == expected

    def test_fizzbuzz_larger_sequence(self):
        """Test FizzBuzz for first 30 numbers to verify pattern continues"""
        result = fizzbuzz(30)
        assert result[29] == "FizzBuzz"  # 30 is FizzBuzz
        assert result[8] == "Fizz"  # 9 is Fizz
        assert result[19] == "Buzz"  # 20 is Buzz
