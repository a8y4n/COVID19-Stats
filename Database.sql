-- Create a database with the following code.
-- You can enter your own preferred names too but make sure you make changes in the main file completely.
-- CREATE DATABASE csproj; 

CREATE TABLE stat (
    srno INT PRIMARY KEY,
    state_ut VARCHAR(20),
    confirmed_cases INT,
    active_cases INT,
    cured INT,
    death INT
);
