# Redis

## Connection
```
❯ redis-cli

127.0.0.1:6379> ECHO "test..."
"test..."
127.0.0.1:6379>
```

### Set
```
❯ redis-cli

127.0.0.1:6379> SET "total_votes" 95
127.0.0.1:6379> GET "total_votes"
"95"
127.0.0.1:6379>
```

### MSet (Multiple Set)
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