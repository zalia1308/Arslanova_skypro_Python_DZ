import pytest
from StringUtils import StringUtils

StringUtils = StringUtils()

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("skypro", "Skypro"),
        ("тест", "Тест"),
        ("тест с пробелом", "Тест с пробелом"),
        ("skypro125", "Skypro125"),
        ("залияЗАЛИЯЗалиязалиязалиязалиязалиязалиязалиязалиязалия", "Залиязалиязалиязалиязалиязалиязалиязалиязалиязалиязалия"),
    ],
)
def test_positive_capitilize(input_text, expected_output):
    assert StringUtils.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
       ("", ""),
       (" ", " "),
    ],
)
def test_negative_capitilize(input_text, expected_output):
    assert StringUtils.capitilize(input_text) == expected_output





@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("       skypro", "skypro"),
        ("               тест", "тест"),
        ("  тест с пробелом", "тест с пробелом"),
        ("   skypro125", "skypro125"),
        ("       skypro   ", "skypro   "),

    ],
)
def test_positive_trim(input_text, expected_output):
    assert StringUtils.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
       ("", ""),
       ("         ", ""),
    ],
)
def test_negative_trim(input_text, expected_output):
    assert StringUtils.trim(input_text) == expected_output






@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (("a,b,c,d", ","), ["a", "b", "c", "d"]),
        (("1:2:3", ":"), ["1", "2", "3"]),
        (("рио-де-жанейро", "-"), ["рио", "де", "жанейро"]),
        (("1,5:2,9:3,4", ":"), ["1,5", "2,9", "3,4"]),
    ],
)
def test_positive_to_list(input_text, expected_output):
    assert StringUtils.to_list(input_text[0], input_text[1]) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
       ("", []),
       ("         ", []),
       ("тест", ['тест']),
    ],
)
def test_negative_to_list(input_text, expected_output):
    assert StringUtils.to_list(input_text) == expected_output






@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "S", True),
        ("4857632", "7", True),
        ("Тест", "с", True),

    ],
)
def test_positive_contains(input_text, symbol, expected_output):
    assert StringUtils.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "Sипп", False),
        ("SkyPro", "  ", False),
        ("SkyPro", "g", False),
        ("75412", "6", False),
    ],
)
def test_negative_contains(input_text, symbol, expected_output):
    assert StringUtils.contains(input_text, symbol) == expected_output



@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro   2", "Pro", "Sky   2"),
        ("Тест_тест", "т", "Тес_ес"),
        ("12453", "45", "123"),
    ],
)
def test_positive_delete_symbol(input_text, symbol, expected_output):
    assert StringUtils.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "  ", "SkyPro"),
        ("тест         ", "", "тест         "),
        ("", " ", ""),
        ("  ", " ", ""),
    ],
)
def test_negative_delete_symbol(input_text, symbol, expected_output):
    assert StringUtils.delete_symbol(input_text, symbol) == expected_output






@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "S", True),
        ("4857632", "48", True),
        ("Тест", "Т", True),
        ("SkyPro_ggdfjd", "Sky", True),
        ("Тест_жил-был", "Тест", True),
    ],
)
def test_positive_starts_with(input_text, symbol, expected_output):
    assert StringUtils.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
       ("    ", "S", False),
       ("", "p", False),
       ("SkyPro", "p", False),
       ("SkyPro", "  ", False),
    ],
)
def test_negative_starts_with(input_text, symbol, expected_output):
    assert StringUtils.starts_with(input_text, symbol) == expected_output






@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "o", True),
        ("4857632", "32", True),
        ("Тест", "т", True),
        ("SkyPro_ggdfjd", "fjd", True),
        ("Тест_жил-был", "был", True),
    ],
)
def test_positive_end_with(input_text, symbol, expected_output):
    assert StringUtils.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
       ("    ", "S", False),
       ("", "p", False),
       ("SkyPro", "p", False),
       ("SkyPro", "  ", False),
    ],
)
def test_negative_end_with(input_text, symbol, expected_output):
    assert StringUtils.end_with(input_text, symbol) == expected_output





@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", True),
        ("  ", True),
    ],
)
def test_positive_is_empty(input_text, expected_output):
    assert StringUtils.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
       ("S", False),
       ("1245", False),
       ("Т", False),
       ("SkyPro_ggdfjd", False),
       ("Тест_жил-был", False),
    ],
)
def test_negative_is_empty(input_text, expected_output):
    assert StringUtils.is_empty(input_text) == expected_output




@pytest.mark.parametrize(
    "lst, joiner, expected_output",
    [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ":", "Sky:Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        ([1, 2, 3, 4], ":", "1:2:3:4"),
        (["рио", "де", "жанейро"], "-", "рио-де-жанейро"),
        ([1.7, 2.8, 3.7, 4.4], ", ", "1.7, 2.8, 3.7, 4.4"),
    ]
)
def test_positive_list_to_string(lst, joiner, expected_output):
    res = StringUtils.list_to_string(lst, joiner)
    assert res == expected_output



@pytest.mark.parametrize(
    "lst, joiner, expected_output",
    [
        ([], ",", ""),
        ([   ], ",", ""),
    ],
)
def test_negative_list_to_string(lst, joiner, expected_output):
    res = StringUtils.list_to_string(lst, joiner)
    assert res == expected_output