# how to configure sql

#### create new user
```bash
sudo -u postgres createuser <username> --pwprompt --interactive
```
#### add database to it
```bash
sudo -u postgres createdb <dbName> -O <username>
```

#### test the connection
```bash
psql postgres://<username>:<password>@localhost:5432/<dbName>
```
- then add it to nvim using vim-dadbod-ui
