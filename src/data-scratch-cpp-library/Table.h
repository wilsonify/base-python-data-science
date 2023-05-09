class Table
{
    Table(columns);
    double representation();
    double insert(row_values);
    double update(updates, predicate);
    double delete(predicate);
    double select(*this, keep_columns = None, additional_columns = None);
    double where(*this, predicate);
    double limit(*this, num_rows = None);
    double group_by(*this, group_by_columns, aggregates, having = None);
    double order_by(*this, order);
    double join(*this, other_table, left_join = False);
}