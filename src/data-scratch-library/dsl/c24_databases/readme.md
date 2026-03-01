# Chapter 24 – Databases and SQL

A from-scratch relational database engine ("NotQuiteABase") that implements core
SQL operations in Python.

---

## Key Concepts

### Relational Model

Data is stored in **tables** with a fixed schema (column names + types). Tables are
queried and manipulated with SQL-like operations.

### Supported Operations

| SQL | NotQuiteABase method | Description |
|---|---|---|
| `CREATE TABLE` | `Table(columns, types)` | Define schema |
| `INSERT` | `.insert(values)` | Add a row |
| `UPDATE … SET … WHERE` | `.update(updates, predicate)` | Modify matching rows |
| `DELETE … WHERE` | `.delete(predicate)` | Remove matching rows |
| `SELECT` | `.select(keep_columns, additional_columns)` | Project / compute columns |
| `WHERE` | `.where(predicate)` | Filter rows |
| `LIMIT` | `.limit(n)` | First *n* rows |
| `GROUP BY` | `.group_by(columns, aggregates, having)` | Aggregate with optional HAVING |
| `ORDER BY` | `.order_by(order)` | Sort rows |
| `JOIN` | `.join(other, left_join)` | Inner or left join on matching column names |

### Type Aliases

| Alias | Definition |
|---|---|
| `Row` | `Dict[str, Any]` |
| `WhereClause` | `Callable[[Row], bool]` |
| `HavingClause` | `Callable[[List[Row]], bool]` |

---

## Module API

### `Table` class

```python
users = Table(['user_id', 'name', 'num_friends'], [int, str, int])
users.insert([0, "Hero", 0])

results = (
    users
    .where(lambda row: row["num_friends"] > 1)
    .select(keep_columns=["name"])
    .limit(5)
)
```

Key methods: `insert`, `update`, `delete`, `select`, `where`, `limit`,
`group_by`, `order_by`, `join`.

---

## Example

See [`e01_databases.py`](e01_databases.py) for CREATE / INSERT / SELECT /
JOIN / GROUP BY / sub-select demonstrations.

---

## Further Reading

- [SQL – Wikipedia](https://en.wikipedia.org/wiki/SQL)
- [SQLite tutorial](https://www.sqlitetutorial.net/) — lightweight real database
- *Data Science from Scratch*, Chapter 24
