# Problems log – exploration of July 2024

| # | Table | What we found | How many rows | Idea for a fix |
|1 | ridership | Ridership station complex ID is stored as a text while the complex_id in the stations table is a number so this will create a problem of matching in the join | all rows (2 156 907) | we should convert the station_comple_id to a number before joining the two tables and we count the rows that fail in the coversion 
|

|2 | ridership | ridership meaning the number of people is a decimal number (for example 3.0 , 1.0 etc) instead of a whole number | all rows (2 156 907) | We sould check that no value has decimals for example 2.5 or 3.1 etc and that no value is negative, then we convert to a whole number |


|3 | ridership | in a row we have one station + one hour + one fare class category for that the same station and hour appears on multiple rows |  all rows (2 156 907) | add up the fare class categories to get one row per station and hour |


|4 | ridership | The file also contained the Roosevelt Island tram and the Staten Island Railway which are not subway lines | on 17,902 rows | we keep only the Subway as a transit mode so we keep only transit_mode = Subway