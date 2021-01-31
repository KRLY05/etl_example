CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS staging.apps (
id varchar(256),
title varchar(256),
description varchar(2000),
published_timestamp varchar(256),
last_update_timestamp varchar(256)
);

TRUNCATE staging.apps;

CREATE TABLE IF NOT EXISTS public.apps (
pk integer identity(0, 1) PRIMARY KEY,
id varchar(256),
title varchar(256),
description varchar(2000),
published_timestamp timestamp,
last_update_timestamp timestamp
);