# Redis

## Connection
```
❯ redis-cli

127.0.0.1:6379> ECHO "test..."
"test..."
127.0.0.1:6379>
```

### SET
```
❯ redis-cli

127.0.0.1:6379> SET "total_votes" 95
127.0.0.1:6379> GET "total_votes"
"95"
127.0.0.1:6379>
```

### MSET (Multiple SET)
```
❯ redis-cli

127.0.0.1:6379> MSET "total_votes" 95 "daily_votes" 20
127.0.0.1:6379> GET "age"
"20"
127.0.0.1:6379>
```

### Del
```
❯ redis-cli

127.0.0.1:6379> DEL "total_votes"
(integer) 1
127.0.0.1:6379> GET "total_votes"
(nil)
127.0.0.1:6379>
```

### HSET, HGET (HASH SET, GET)
```
❯ redis-cli

127.0.0.1:6379> HSET "election:2022:04:20" "total_votes" 95
127.0.0.1:6379> HSET "election:2022:04:20" "daily_votes" 20

127.0.0.1:6379> HGET "election:2022:04:20" "total_votes"
"95"

127.0.0.1:6379> HGET "election:2022:04:20" "daily_votes"
"20"
127.0.0.1:6379>
```

### HMSET (Hash Multiple SET)
```
❯ redis-cli

127.0.0.1:6379> HMSET "session:user:1995" "name" "ovalves" "shopping_cart" 10
127.0.0.1:6379> HGET "session:user:1995" "name"
"ovalves"
127.0.0.1:6379>
```

### HDEL (Delete Hash)
```
❯ redis-cli

127.0.0.1:6379> HDEL "election:2022:04:20" "total_votes"
(integer) 1
127.0.0.1:6379>
```

### Keys
```
❯ redis-cli

127.0.0.1:6379> KEYS *
1) "total_votes"
```

### Search Keys

#### Use `*` para buscar a correspondência de um ou mais caracteres dentro de uma chave.

```
127.0.0.1:6379> KEYS "*_votes"
2) "daily_votes"
3) "total_votes"
127.0.0.1:6379>
```

#### Use `?` para buscar a correspondência de qualquer caractere dentro de uma chave

```
127.0.0.1:6379> MSET "count:vote:log:1997-12-21" 97 "count:vote:log:2022-12-21" 95

127.0.0.1:6379> KEYS "count:vote:log:1997-??-??"
1) "count:vote:log:1997-12-21"

127.0.0.1:6379> KEYS "count:vote:log:????-12-??"
1) "count:vote:log:1997-12-21"
2) "count:vote:log:2022-12-21"
```

#### Use `[]` para buscar todas as correspondência de um caractere dentro de uma chave

```
127.0.0.1:6379> MSET "count:vote:log:1997-12-21" 97 "count:vote:log:1997-07-21" 95

127.0.0.1:6379> KEYS "count:vote:log:????-?[27]-??"
1) "count:vote:log:1997-07-21"
2) "count:vote:log:1997-12-21"
3) "count:vote:log:2022-12-21"
```

### Expire - TTL
```
❯ redis-cli

127.0.0.1:6379> EXPIRE "session:user:1995" 10
127.0.0.1:6379> TTL "session:user:1995"
```

### INCR
```
❯ redis-cli

127.0.0.1:6379> INCR "page:home:1995-04-20"
(integer) 1
127.0.0.1:6379> INCR "page:home:1995-04-20"
(integer) 2
127.0.0.1:6379> INCR "page:home:1995-04-20"
(integer) 3
```

### INCRBY
```
❯ redis-cli

127.0.0.1:6379> INCRBY "page:home:1995-04-20" 10
(integer) 11
127.0.0.1:6379> INCRBY "page:home:1995-04-20" 10
(integer) 21
```

### DECR
```
❯ redis-cli

127.0.0.1:6379> DECR "page:home:1995-04-20"
(integer) 3
127.0.0.1:6379> DECR "page:home:1995-04-20"
(integer) 2
127.0.0.1:6379> DECR "page:home:1995-04-20"
(integer) 1
```

### DECRBY
```
❯ redis-cli

127.0.0.1:6379> DECRBY "page:home:1995-04-20" 10
(integer) 21
127.0.0.1:6379> DECRBY "page:home:1995-04-20" 10
(integer) 11
```

### SETBIT - GETBIT - BITCOUNT
```
❯ redis-cli

127.0.0.1:6379> SETBIT "session:1995-04-20:user" 1 1
(integer) 1

127.0.0.1:6379> GETBIT "session:1995-04-20:user" 1
(integer) 1

127.0.0.1:6379> BITCOUNT "session:1995-04-20:user"
(integer) 1
```

### FLUSHALL
```
❯ redis-cli

127.0.0.1:6379> flushall
OK

127.0.0.1:6379> KEYS *
(empty list or set)
```