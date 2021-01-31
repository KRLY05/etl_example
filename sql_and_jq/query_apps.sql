-- using window function to get most recent unique values from table with duplicates
-- space complexity O(n)
SELECT
    pk,
    id,
    title,
    rating,
    last_update_date
FROM
    (
    SELECT
        pk,
        id,
        title,
        rating,
        last_update_date,
        RANK () OVER (
            PARTITION BY id
            ORDER BY last_update_date DESC
            ) recent_rank
    FROM apps
) ranked
WHERE recent_rank = 1