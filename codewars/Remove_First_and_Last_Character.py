# It's pretty straightforward. Your goal is to create a function that removes the
# first and last characters of a string. You're given one parameter, the original string.
# You don't have to worry with strings with less than two characters.

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(remove_char('eloquent'), 'loquen')
#         test.assert_equals(remove_char('country'), 'ountr')
#         test.assert_equals(remove_char('person'), 'erso')
#         test.assert_equals(remove_char('place'), 'lac')
#         test.assert_equals(remove_char('ok'), '')
#         test.assert_equals(remove_char('ooopsss'), 'oopss')


def remove_char(s):
    return s[1:-1]

if __name__ == '__main__':
    remove_char('hello')
    remove_char('world')
    remove_char('eloquent')
