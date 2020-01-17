
# SNA lab submission

Files for running the SNA project

## Usage
AWS ubuntu instance is recommended for running
  1. Clone the repo
  2. Run `docker-compose build`
  3. Run `docker-compose up`
  4. Open your server (or localhost) in the browser
  5. Send any log message via the loaded menu
  6. Run `docker exec -it docker_momgodb_1 mongo --username root --password pass` to login into the database
  7. Type `use admin` to switch the current database
  8. Type `db.logs.find();` to see collection of logs
