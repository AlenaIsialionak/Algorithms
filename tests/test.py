import pytest
from LinkedList_leetcode import LinkedList as l

@pytest.mark.parametrize(
    "list1, expected",
    [
        (l.from_iterable([1, 1, 2]), [1, 2]),
        (l.from_iterable([]), []),
        (l.from_iterable([1,  1]), [1]),
        (l.from_iterable([1, 1, 2, 3, 3, 3]), [1, 2, 4])
    ]
)

# @pytest.fixture
# def test_lists():
#     """Fixture for linked list tests."""
#     # list1 = l()
#     # for item in [1, 2, 3, 4, 4]:
#     #     list1.append(item)
#     list1 = l.from_iterable([1, 2, 3])
#     return list1

def test_deleteDuplicates1(list1, expected):
    res_ = l().deleteDuplicates1(list1, l())
    res = res_.list_print()
    assert res == expected

