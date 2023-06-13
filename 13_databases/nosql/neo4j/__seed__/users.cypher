// Find User nodes
MATCH (u:User) WITH { email: u.email, id: u.user_id, date: u.registered_on} as User RETURN User;

// Find users that registered on or after 2023.03.28
WITH date('2023-03-28') AS registeredDate
MATCH (u:User) WHERE u.registered_on >= registeredDate
RETURN u.user_id, u.email, u.registered_on AS registered
ORDER BY u.registered_on DESC;

@neo4j> WITH date('2023-03-28') AS testDate
        MATCH (u:User) WHERE u.registered_on >= testDate
        RETURN u.user_id, u.email, u.registered_on AS registered
        ORDER BY u.registered_on DESC;
+---------------------------------------------+
| u.user_id | u.email            | registered |
+---------------------------------------------+
| "123"     | "angie@sample.com" | 2023-03-28 |
| "456"     | "bob@sample.com"   | 2023-03-28 |
| "789"     | "alice@sample.com" | 2023-03-28 |
+---------------------------------------------+

3 rows


// List all registered users
MATCH (u:User)
RETURN u.user_id, u.email, u.registered_on
ORDER BY u.registered_on DESC;

@neo4j> WITH date('2023-03-28') AS testDate
        MATCH (u:User) WHERE u.registered_on >= testDate
        RETURN u.user_id, u.email, u.registered_on AS registered
        ORDER BY u.registered_on DESC;
+---------------------------------------------+
| u.user_id | u.email            | registered |
+---------------------------------------------+
| "123"     | "angie@sample.com" | 2023-03-28 |
| "456"     | "bob@sample.com"   | 2023-03-28 |
| "789"     | "alice@sample.com" | 2023-03-28 |
+---------------------------------------------+

3 rows

// Find a user by email
MATCH (u:User { email: 'alice@sample.com' }) RETURN u;

// Delete all User nodes and relationships for a user with a specific email
MATCH (u:User { email: 'alice@sample.com' }) DETACH DELETE u;