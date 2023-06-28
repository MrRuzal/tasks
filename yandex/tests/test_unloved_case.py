from sprint12.unloved_case import solution


def test_unloved_case(capsys):
    list_todo = ['one', 'two', 'three', 'four', 'five']
    number = 3
    expected_output = 'one\ntwo\nfour\nfive\n'

    solution(list_todo, number)
    captured_output = capsys.readouterr()
    assert captured_output.out == expected_output
