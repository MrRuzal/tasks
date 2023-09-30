# Grade book
# Complete the function so that it finds the average of the three scores passed to it and
# returns the letter value associated with that grade.

# @test.describe("Grade book")
# def fixed_tests():
#     @test.it('should return an A')
#     def a_test_case():
#         test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
#         test.assert_equals(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
#         test.assert_equals(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
#         test.assert_equals(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")
#
#     @test.it("should return a B")
#     def b_test_case():
#         test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
#         test.assert_equals(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
#         test.assert_equals(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")
#
#     @test.it("should return a C")
#     def c_test_case():
#         test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
#         test.assert_equals(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
#         test.assert_equals(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")
#
#     @test.it("should return a D")
#     def d_test_case():
#         test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
#         test.assert_equals(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
#         test.assert_equals(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")
#
#     @test.it("should return an F")
#     def f_test_case():
#         test.assert_equals(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
#         test.assert_equals(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
#         test.assert_equals(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
#         test.assert_equals(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")

def grade_book(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# of
# def get_grade(s1, s2, s3):
#     score = (s1 + s2 + s3) / 3
#     if 90 <= score <= 100:
#         return 'A'
#     if 80 <= score < 90:
#         return 'B'
#     if 70 <= score < 80:
#         return 'C'
#     if 60 <= score < 70:
#         return 'D'
#     if 0 <= score < 60:
#         return 'F'

if __name__ == "__main__":
    grade_book(95, 90, 93) # A
    grade_book(100, 85, 96) # A
    grade_book(92, 93, 94) # A
    grade_book(100, 100, 100) # A
    grade_book(70, 70, 100) # B
    grade_book(82, 85, 87) # B
    grade_book(84, 79, 85) # B
    grade_book(70, 70, 70) # C
    grade_book(75, 70, 79) # C
    grade_book(60, 82, 76) # C
    grade_book(65, 70, 59) # D
    grade_book(66, 62, 68) # D
    grade_book(58, 62, 70) # D
    grade_book(44, 55, 52) # F
    grade_book(48, 55, 52) # F
    grade_book(58, 59, 60) # F
    grade_book(0, 0, 0) # F
    grade_book(100, 100, 100) # F
