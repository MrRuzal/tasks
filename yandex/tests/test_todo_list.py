from sprint12.todo_list import print_todo_list


def test_todo_list(capsys):
    list_todo = ['one', 'two', 'three', 'four', 'five']
    expected_output = 'one\ntwo\nthree\nfour\nfive\n'
    print_todo_list(list_todo)
    captured_output = capsys.readouterr()
    assert captured_output.out == expected_output
