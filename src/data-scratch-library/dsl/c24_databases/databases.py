"""
An in-memory SQL-like table: SELECT, WHERE, GROUP BY, ORDER BY, JOIN.
"""

from collections import defaultdict
from typing import Any, Callable, Dict, List, Optional


class Table:
    """Simple in-memory row-store table."""

    def __init__(self, columns: List[str]) -> None:
        self.columns = columns
        self.rows: List[Dict[str, Any]] = []

    def __repr__(self) -> str:
        return str(self.columns) + "\n" + "\n".join(str(r) for r in self.rows)

    def insert(self, row_values: List[Any]) -> None:
        """Insert a row given as a list of values (one per column)."""
        if len(row_values) != len(self.columns):
            raise TypeError("wrong number of elements")
        self.rows.append(dict(zip(self.columns, row_values)))

    def update(
        self,
        updates: Dict[str, Any],
        predicate: Callable[[Dict[str, Any]], bool],
    ) -> None:
        """Apply *updates* to every row matching *predicate*."""
        for row in self.rows:
            if predicate(row):
                row.update(updates)

    def delete(
        self, predicate: Callable[[Dict[str, Any]], bool] = lambda row: True
    ) -> None:
        """Delete rows matching *predicate* (default: all)."""
        self.rows = [r for r in self.rows if not predicate(r)]

    def select(
        self,
        keep_columns: Optional[List[str]] = None,
        additional_columns: Optional[Dict[str, Callable]] = None,
    ) -> "Table":
        """Project columns and/or add computed columns."""
        if keep_columns is None:
            keep_columns = self.columns
        if additional_columns is None:
            additional_columns = {}
        result = Table(keep_columns + list(additional_columns.keys()))
        for row in self.rows:
            new_row = [row[c] for c in keep_columns]
            for calc in additional_columns.values():
                new_row.append(calc(row))
            result.insert(new_row)
        return result

    def where(
        self, predicate: Callable[[Dict[str, Any]], bool] = lambda row: True
    ) -> "Table":
        """Return rows matching *predicate*."""
        tbl = Table(self.columns)
        tbl.rows = [r for r in self.rows if predicate(r)]
        return tbl

    def limit(self, num_rows: Optional[int] = None) -> "Table":
        """Return at most *num_rows* rows."""
        tbl = Table(self.columns)
        tbl.rows = self.rows[:num_rows] if num_rows is not None else list(self.rows)
        return tbl

    def group_by(
        self,
        group_by_columns: List[str],
        aggregates: Dict[str, Callable],
        having: Optional[Callable] = None,
    ) -> "Table":
        """Group rows by *group_by_columns* and apply *aggregates*."""
        grouped: Dict[tuple, List[Dict[str, Any]]] = defaultdict(list)
        for row in self.rows:
            key = tuple(row[c] for c in group_by_columns)
            grouped[key].append(row)
        result = Table(group_by_columns + list(aggregates.keys()))
        for key, rows in grouped.items():
            if having is None or having(rows):
                new_row = list(key)
                for agg_fn in aggregates.values():
                    new_row.append(agg_fn(rows))
                result.insert(new_row)
        return result

    def order_by(self, order: Callable) -> "Table":
        """Return a copy of the table sorted by *order*."""
        tbl = self.select()
        tbl.rows.sort(key=order)
        return tbl

    def join(self, other: "Table", left_join: bool = False) -> "Table":
        """Inner or left join with *other* on shared column names."""
        join_cols = [c for c in self.columns if c in other.columns]
        extra_cols = [c for c in other.columns if c not in join_cols]
        result = Table(self.columns + extra_cols)

        for row in self.rows:
            matches = other.where(
                lambda o, _r=row: all(o[c] == _r[c] for c in join_cols)
            ).rows
            for m in matches:
                result.insert(
                    [row[c] for c in self.columns] + [m[c] for c in extra_cols]
                )
            if left_join and not matches:
                result.insert(
                    [row[c] for c in self.columns] + [None] * len(extra_cols)
                )
        return result
