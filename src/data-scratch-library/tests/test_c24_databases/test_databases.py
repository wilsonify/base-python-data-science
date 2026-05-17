import pytest

from dsl.c24_databases.databases import Table


@pytest.fixture
def users_table():
    table = Table(["user_id", "name", "num_friends"])
    table.insert([0, "Hero", 0])
    table.insert([1, "Dunn", 2])
    table.insert([2, "Sue", 3])
    table.insert([3, "Chi", 3])
    table.insert([4, "Thor", 3])
    table.insert([5, "Clive", 2])
    return table


@pytest.fixture
def empty_table():
    return Table(["id", "value"])


@pytest.fixture
def interests_table():
    table = Table(["user_id", "interest"])
    table.insert([0, "SQL"])
    table.insert([0, "NoSQL"])
    table.insert([2, "SQL"])
    table.insert([2, "MySQL"])
    return table


class TestInsert:
    def test_insert_adds_row(self, empty_table):
        empty_table.insert([1, "hello"])
        assert len(empty_table.rows) == 1

    def test_insert_creates_dict(self, empty_table):
        empty_table.insert([1, "hello"])
        assert empty_table.rows[0] == {"id": 1, "value": "hello"}

    def test_insert_wrong_number_of_elements(self, empty_table):
        with pytest.raises(TypeError):
            empty_table.insert([1])

    def test_insert_too_many_elements(self, empty_table):
        with pytest.raises(TypeError):
            empty_table.insert([1, "hello", "extra"])

    def test_insert_multiple_rows(self, empty_table):
        empty_table.insert([1, "a"])
        empty_table.insert([2, "b"])
        empty_table.insert([3, "c"])
        assert len(empty_table.rows) == 3


class TestUpdate:
    def test_update_matching_rows(self, users_table):
        users_table.update({"num_friends": 99}, lambda row: row["name"] == "Hero")
        hero = [r for r in users_table.rows if r["name"] == "Hero"][0]
        assert hero["num_friends"] == 99

    def test_update_no_matching_rows(self, users_table):
        original_rows = [dict(r) for r in users_table.rows]
        users_table.update({"num_friends": 99}, lambda row: row["name"] == "Nobody")
        assert users_table.rows == original_rows

    def test_update_multiple_columns(self, users_table):
        users_table.update(
            {"name": "Updated", "num_friends": 10},
            lambda row: row["user_id"] == 0,
        )
        row = [r for r in users_table.rows if r["user_id"] == 0][0]
        assert row["name"] == "Updated"
        assert row["num_friends"] == 10


class TestDelete:
    def test_delete_with_predicate(self, users_table):
        users_table.delete(lambda row: row["name"] == "Hero")
        names = [r["name"] for r in users_table.rows]
        assert "Hero" not in names

    def test_delete_all(self, users_table):
        users_table.delete()
        assert len(users_table.rows) == 0

    def test_delete_no_match(self, users_table):
        original_len = len(users_table.rows)
        users_table.delete(lambda row: row["name"] == "Nobody")
        assert len(users_table.rows) == original_len

    def test_delete_preserves_nonmatching(self, users_table):
        users_table.delete(lambda row: row["num_friends"] == 0)
        assert len(users_table.rows) == 5
        assert all(r["num_friends"] != 0 for r in users_table.rows)


class TestSelect:
    def test_select_all_columns(self, users_table):
        result = users_table.select()
        assert result.columns == users_table.columns
        assert len(result.rows) == len(users_table.rows)

    def test_select_specific_columns(self, users_table):
        result = users_table.select(keep_columns=["name"])
        assert result.columns == ["name"]
        assert all("name" in r for r in result.rows)

    def test_select_with_additional_columns(self, users_table):
        result = users_table.select(
            additional_columns={"double_friends": lambda row: row["num_friends"] * 2}
        )
        assert "double_friends" in result.columns
        for row in result.rows:
            assert row["double_friends"] == row["num_friends"] * 2

    def test_select_returns_new_table(self, users_table):
        result = users_table.select()
        assert result is not users_table


class TestWhere:
    def test_where_filters_rows(self, users_table):
        result = users_table.where(lambda row: row["num_friends"] > 2)
        assert all(r["num_friends"] > 2 for r in result.rows)

    def test_where_no_match(self, users_table):
        result = users_table.where(lambda row: row["num_friends"] > 100)
        assert len(result.rows) == 0

    def test_where_all_match(self, users_table):
        result = users_table.where(lambda row: row["num_friends"] >= 0)
        assert len(result.rows) == len(users_table.rows)

    def test_where_returns_new_table(self, users_table):
        result = users_table.where()
        assert result is not users_table

    def test_where_default_returns_all(self, users_table):
        result = users_table.where()
        assert len(result.rows) == len(users_table.rows)


class TestLimit:
    def test_limit_returns_correct_number(self, users_table):
        result = users_table.limit(2)
        assert len(result.rows) == 2

    def test_limit_none_returns_all(self, users_table):
        result = users_table.limit()
        assert len(result.rows) == len(users_table.rows)

    def test_limit_zero(self, users_table):
        result = users_table.limit(0)
        assert len(result.rows) == 0

    def test_limit_exceeds_rows(self, users_table):
        result = users_table.limit(100)
        assert len(result.rows) == len(users_table.rows)

    def test_limit_returns_new_table(self, users_table):
        result = users_table.limit(2)
        assert result is not users_table


class TestGroupBy:
    def test_group_by_count(self, users_table):
        result = users_table.group_by(
            group_by_columns=["num_friends"],
            aggregates={"count": lambda rows: len(rows)},
        )
        assert len(result.rows) > 0
        total = sum(r["count"] for r in result.rows)
        assert total == len(users_table.rows)

    def test_group_by_with_having(self, users_table):
        result = users_table.group_by(
            group_by_columns=["num_friends"],
            aggregates={"count": lambda rows: len(rows)},
            having=lambda rows: len(rows) > 1,
        )
        for row in result.rows:
            assert row["count"] > 1

    def test_group_by_aggregate_values(self, users_table):
        result = users_table.group_by(
            group_by_columns=["num_friends"],
            aggregates={
                "min_user_id": lambda rows: min(r["user_id"] for r in rows),
                "count": lambda rows: len(rows),
            },
        )
        assert "min_user_id" in result.columns
        assert "count" in result.columns


class TestOrderBy:
    def test_order_by_ascending(self, users_table):
        result = users_table.order_by(lambda row: row["num_friends"])
        friends = [r["num_friends"] for r in result.rows]
        assert friends == sorted(friends)

    def test_order_by_descending(self, users_table):
        result = users_table.order_by(lambda row: -row["num_friends"])
        friends = [r["num_friends"] for r in result.rows]
        assert friends == sorted(friends, reverse=True)

    def test_order_by_returns_new_table(self, users_table):
        result = users_table.order_by(lambda row: row["user_id"])
        assert result is not users_table

    def test_order_by_name(self, users_table):
        result = users_table.order_by(lambda row: row["name"])
        names = [r["name"] for r in result.rows]
        assert names == sorted(names)


class TestJoin:
    def test_inner_join(self, users_table, interests_table):
        result = users_table.join(interests_table)
        assert "interest" in result.columns
        assert all(r["interest"] is not None for r in result.rows)

    def test_left_join(self, users_table, interests_table):
        result = users_table.join(interests_table, left_join=True)
        user_ids = {r["user_id"] for r in result.rows}
        original_ids = {r["user_id"] for r in users_table.rows}
        assert original_ids == user_ids

    def test_left_join_none_values(self, users_table, interests_table):
        result = users_table.join(interests_table, left_join=True)
        unmatched = [r for r in result.rows if r["interest"] is None]
        assert len(unmatched) > 0

    def test_join_columns(self, users_table, interests_table):
        result = users_table.join(interests_table)
        expected_cols = users_table.columns + ["interest"]
        assert result.columns == expected_cols

    def test_join_empty_other_table(self, users_table):
        other = Table(["user_id", "hobby"])
        result = users_table.join(other)
        assert len(result.rows) == 0

    def test_left_join_empty_other_table(self, users_table):
        other = Table(["user_id", "hobby"])
        result = users_table.join(other, left_join=True)
        assert len(result.rows) == len(users_table.rows)
        assert all(r["hobby"] is None for r in result.rows)


class TestRepr:
    def test_repr_contains_columns(self, users_table):
        r = repr(users_table)
        assert "user_id" in r
        assert "name" in r

    def test_repr_empty_table(self, empty_table):
        r = repr(empty_table)
        assert "id" in r
