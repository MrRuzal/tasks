# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

# @test.describe('Fixed tests')
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(repeat_str(4, 'a'), 'aaaa')
#         test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
#         test.assert_equals(repeat_str(2, 'abc'), 'abcabc')


def repeat_str(repeat, string):
    result = string * repeat
    return result

if __name__ == '__main__':
    print(repeat_str(6, "I"))
    print(repeat_str(5, "Hello"))
    print(repeat_str(2, "abc"))
