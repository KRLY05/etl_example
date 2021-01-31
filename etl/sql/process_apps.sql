-- Delete records which no longer exist
DELETE FROM public.apps
WHERE
id NOT IN (SELECT id from staging.apps);

-- Update record values
UPDATE public.apps target
SET
    title = source.title,
    description = source.description,
    published_timestamp = source.published_timestamp::timestamp,
    last_update_timestamp = source.last_update_timestamp::timestamp
FROM staging.apps source
WHERE
    target.id = source.id;

-- Insert new records
INSERT INTO public.apps (
    id,
    title,
    description,
    published_timestamp,
    last_update_timestamp
)
SELECT
    id,
    title,
    description,
    published_timestamp::timestamp,
    last_update_timestamp::timestamp
FROM staging.apps
WHERE id NOT IN (SELECT id from public.apps);