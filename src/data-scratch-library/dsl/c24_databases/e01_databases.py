"""
Example: SQL-like operations using the Table class.
"""

import logging
from logging.config import dictConfig

from dsl.c24_databases.databases import Table
from dsl.c24_databases.data import users_data, user_interests_data


def main() -> None:
    users = Table(["user_id", "name", "num_friends"])
    for row in users_data:
        users.insert(row)

    logging.info("users =\n%s", users)
    logging.info("select all =\n%s", users.select())
    logging.info("limit 2 =\n%s", users.limit(2))
    logging.info("select user_id =\n%s", users.select(keep_columns=["user_id"]))
    logging.info(
        "Dunn's user_id =\n%s",
        users.where(lambda r: r["name"] == "Dunn").select(keep_columns=["user_id"]),
    )

    name_len = lambda r: len(r["name"])
    logging.info(
        "name_length =\n%s",
        users.select(keep_columns=[], additional_columns={"name_length": name_len}),
    )

    min_uid = lambda rows: min(r["user_id"] for r in rows)
    stats = (
        users.select(additional_columns={"name_len": name_len})
        .group_by(
            group_by_columns=["name_len"],
            aggregates={"min_user_id": min_uid, "num_users": len},
        )
    )
    logging.info("stats by name length =\n%s", stats)

    first_letter = lambda r: r["name"][0] if r["name"] else ""
    avg_friends = lambda rows: sum(r["num_friends"] for r in rows) / len(rows)
    enough = lambda rows: avg_friends(rows) > 1

    avg_by_letter = (
        users.select(additional_columns={"first_letter": first_letter})
        .group_by(
            group_by_columns=["first_letter"],
            aggregates={"avg_num_friends": avg_friends},
            having=enough,
        )
    )
    logging.info("avg friends by letter =\n%s", avg_by_letter)

    friendliest = avg_by_letter.order_by(lambda r: -r["avg_num_friends"]).limit(4)
    logging.info("friendliest letters =\n%s", friendliest)

    # JOIN
    interests = Table(["user_id", "interest"])
    for row in user_interests_data:
        interests.insert(row)

    sql_users = (
        users.join(interests)
        .where(lambda r: r["interest"] == "SQL")
        .select(keep_columns=["name"])
    )
    logging.info("SQL users =\n%s", sql_users)

    count_interests = lambda rows: len([r for r in rows if r["interest"] is not None])
    interest_counts = users.join(interests, left_join=True).group_by(
        group_by_columns=["user_id"],
        aggregates={"num_interests": count_interests},
    )
    logging.info("interest counts =\n%s", interest_counts)


if __name__ == "__main__":
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "simple": {
                    "format": "%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                }
            },
            "root": {"handlers": ["console"], "level": logging.DEBUG},
        }
    )
    main()
