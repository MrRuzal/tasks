from sprint12.caring_mother import solution


def test_caring_mother(capsys):
    list_todo = ['one', 'two', 'three', 'four', 'five']
    # item = 'two'
    # expected_output = 1
    item_and_expected_output = [['two', 1], ['six', -1]]

    for item, expected_output in item_and_expected_output:
        solution(list_todo, item)
        captured_output = capsys.readouterr()
        assert captured_output.out == expected_output
