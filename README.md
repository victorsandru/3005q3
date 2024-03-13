# 3005q3

steps to run

1. create user with name 'postgres' and password 'admin'
   1a. if you dont want to create a new user, go to line 6, and 7 and change the user string and password string respectively to your user

2. create db by running these in your shell
   sudo -u postgres psql -c 'create database a3;'
   sudo -u postgres psql -c 'grant all privileges on database a3 to (your username here);'

3. create table and fill with init data by running this command on your shell
   psql -U (your username) -d q3 -f a3q1.sql
4. run main.py with your uncommented lines of code to test each specific function
