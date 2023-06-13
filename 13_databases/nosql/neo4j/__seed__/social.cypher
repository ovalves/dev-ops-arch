MATCH (n) DETACH DELETE n;

CREATE CONSTRAINT FOR (node:User) REQUIRE (node.user_id) IS UNIQUE;

CALL db.awaitIndexes(300);

// Users
UNWIND [
    {user_id:"123", properties:{email:"angie@sample.com", registered_on:date('2023-03-27')}},
    {user_id:"456", properties:{email:"bob@sample.com", registered_on:date('2023-03-27')}},
    {user_id:"789", properties:{email:"alice@sample.com", registered_on:date('2023-03-27')}}
] AS row
CREATE (n:User{user_id: row.user_id}) SET n += row.properties;

// Users FOLLOWING Relationship
UNWIND [
    {start: {user_id:"123"}, end: {user_id:"456"}, properties:{following_since:date('2023-03-27')}},
    {start: {user_id:"123"}, end: {user_id:"789"}, properties:{following_since:date('2023-03-27')}},
    {start: {user_id:"456"}, end: {user_id:"789"}, properties:{following_since:date('2023-03-27')}}
] AS row
MATCH (start:User{user_id: row.start.user_id})
MATCH (end:User{user_id: row.end.user_id})
CREATE (start)-[r:FOLLOWING]->(end) SET r += row.properties;

// Users FOLLOWED Relationship
UNWIND [
    {start: {user_id:"456"}, end: {user_id:"123"}, properties:{following_since:date('2023-03-27')}},
    {start: {user_id:"789"}, end: {user_id:"123"}, properties:{following_since:date('2023-03-27')}},
    {start: {user_id:"789"}, end: {user_id:"456"}, properties:{following_since:date('2023-03-27')}}
] AS row
MATCH (start:User{user_id: row.start.user_id})
MATCH (end:User{user_id: row.end.user_id})
CREATE (start)-[r:FOLLOWED]->(end) SET r += row.properties;