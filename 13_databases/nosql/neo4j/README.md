# Neo4J

## Sample Queries

### Find User nodes
```bash
MATCH (u:User) WITH { name: u.name, id: u.userId, date: u.registered_on} as User RETURN User;
```

### Find users that registered on or after 2023.03.28
```bash
WITH date('2023-03-28') AS registeredDate
MATCH (u:User) WHERE u.registered_on >= registeredDate
RETURN u.userId, u.name, u.registered_on AS registered
ORDER BY u.registered_on DESC;
```

```bash
@neo4j> WITH date('2023-03-28') AS testDate
        MATCH (u:User) WHERE u.registered_on >= testDate
        RETURN u.userId, u.name, u.registered_on AS registered
        ORDER BY u.registered_on DESC;
+---------------------------------+
| u.userId | u.name  | registered |
+---------------------------------+
| "123"    | "Angie" | 2023-03-28 |
| "456"    | "Bob"   | 2023-03-28 |
| "789"    | "Alice" | 2023-03-28 |
+---------------------------------+

3 rows
```

### List all registered users
```bash
MATCH (u:User)
RETURN u.userId, u.name, u.registered_on AS registered
ORDER BY u.registered_on DESC;
```

```bash
@neo4j> WITH date('2023-03-28') AS testDate
        MATCH (u:User) WHERE u.registered_on >= testDate
        RETURN u.userId, u.name, u.registered_on AS registered
        ORDER BY u.registered_on DESC;
+---------------------------------+
| u.userId | u.name  | registered |
+---------------------------------+
| "123"    | "Angie" | 2023-03-28 |
| "456"    | "Bob"   | 2023-03-28 |
| "789"    | "Alice" | 2023-03-28 |
+---------------------------------+

3 rows
```

### Find a user by name
```bash
MATCH (u:User { name: 'Alice' }) RETURN u;
```

### Delete all User nodes and relationships for a user with a specific name
```bash
MATCH (u:User { name: 'Alice' }) DETACH DELETE u;
```