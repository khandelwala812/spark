-- Create tables
CREATE TABLE "user" (
    id TEXT PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    email TEXT,
    organization_id TEXT REFERENCES organization(id)
);

CREATE TABLE interview (
    id TEXT PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    name TEXT,
    description TEXT,
    objective TEXT,
    user_id TEXT REFERENCES "user"(id),
    questions JSONB,
    quotes JSONB[],
    insights TEXT[],
    time_duration TEXT
);

-- CREATE TABLE feedback (
--     id SERIAL PRIMARY KEY,
--     created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
--     interview_id TEXT REFERENCES interview(id),
--     email TEXT,
--     feedback TEXT,
--     satisfaction INTEGER
-- );
