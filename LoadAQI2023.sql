LOAD DATA INFILE 'C:\\daily_aqi_by_county_2023.csv'
INTO TABLE aqi_2023
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS