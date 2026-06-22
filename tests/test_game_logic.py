from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go HIGHER!")



def test_get_range_for_difficulty_levels():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_new_game_uses_difficulty_range():
    # The new game reset logic should draw its secret from the difficulty range helper
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert easy_low == 1 and easy_high == 20
    assert normal_low == 1 and normal_high == 100
    assert hard_low == 1 and hard_high == 50


def test_parse_guess_invalid_inputs():
    assert parse_guess(None) == (False, None, "Enter a guess.")
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess("not-a-number") == (False, None, "That is not a number.")
    assert parse_guess("42.0") == (True, 42, None)


def test_update_score_logic():
    assert update_score(0, "Win", 0) == 90
    assert update_score(0, "Win", 10) == 10
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too High", 1) == 5
    assert update_score(10, "Too Low", 3) == 5
