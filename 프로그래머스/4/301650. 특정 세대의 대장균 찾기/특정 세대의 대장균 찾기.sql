# WITH RECURSIVE generations AS (
#     SELECT
#         ID,
#         PARENT_ID,
#         1 AS generation
#     FROM
#         ECOLI_DATA
#     WHERE
#         PARENT_ID IS NULL
#     UNION ALL
#     SELECT
#         e.ID,
#         e.PARENT_ID,
#         g.generation + 1
#     FROM
#         ECOLI_DATA e
#     INNER JOIN generations g ON e.PARENT_ID = g.ID
# )
# SELECT
#     ID
# FROM
#     generations
# WHERE
#     generation = 3
# ORDER BY
#     ID;

SELECT
    ID
FROM
    (
        SELECT
            ID,
            PARENT_ID,
            1 AS generation
        FROM
            ECOLI_DATA
        WHERE
            PARENT_ID IS NULL
        UNION ALL
        SELECT
            e.ID,
            e.PARENT_ID,
            g.generation + 1
        FROM
            ECOLI_DATA e
        INNER JOIN 
            (
                SELECT
                    ID,
                    PARENT_ID,
                    1 AS generation
                FROM
                    ECOLI_DATA
                WHERE
                    PARENT_ID IS NULL
                UNION ALL
                SELECT
                    e.ID,
                    e.PARENT_ID,
                    g.generation + 1
                FROM
                    ECOLI_DATA e
                INNER JOIN 
                    (
                        SELECT
                            ID,
                            PARENT_ID,
                            1 AS generation
                        FROM
                            ECOLI_DATA
                        WHERE
                            PARENT_ID IS NULL
                    ) AS g ON e.PARENT_ID = g.ID
            ) AS g ON e.PARENT_ID = g.ID
    ) AS generations
WHERE
    generation = 3
ORDER BY
    ID;