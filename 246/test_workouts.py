import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("test_input,expected",
        [('upper','Mon, Thu\n'),
         ('lower','Tue, Fri\n'),
         ('cardio','Wed\n'),
         ('body','Mon, Tue, Thu, Fri\n'),
         ('30 min', 'Wed\n'),
         ('none', 'No matching workout\n')
        ])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    out, err = capsys.readouterr()
    assert out == expected
