# SQLi

```php
'%1'; DROP TABLE users;'
```

[htb](https://academy.hackthebox.com/module/33/section/194)

table:
| char | encoded |
|------|---------|
| ' | %27 |
| " | %22 |
| # | %23 |
| ; | %3B |
| ) | %29 |

```sql
SELECT * FROM logins WHERE username=''' AND password = 'something';
```

```sql
admin' or '1'='1
```

## SQL Map

[repo](https://github.com/sqlmapproject/sqlmap)
