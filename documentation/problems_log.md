# Problems log – exploration of July 2024

| # | Table | What we found | How many rows | Idea for a fix |

We start with ridership tables : we took july 2024 as a working example

|1 | ridership | Ridership station complex ID is stored as a text while the complex_id in the stations table is a number so this will create a problem of matching in the join | all rows (2 156 907) | we should convert the station_comple_id to a number before joining the two tables and we count the rows that fail in the coversion 
|

|2 | ridership | ridership meaning the number of people is a decimal number (for example 3.0 , 1.0 etc) instead of a whole number | all rows (2 156 907) | We sould check that no value has decimals for example 2.5 or 3.1 etc and that no value is negative, then we convert to a whole number |


|3 | ridership | in a row we have one station + one hour + one fare class category for that the same station and hour appears on multiple rows |  all rows (2 156 907) | add up the fare class categories to get one row per station and hour |


|4 | ridership | The file also contained the Roosevelt Island tram and the Staten Island Railway which are not subway lines | on 17,902 rows | we keep only the Subway as a transit mode so we keep only transit_mode = Subway

Max ridership 14,387 = Grand Central, 5 pm on weekdays (Tuesday's and Wednesdays's normal because it's a rush hour)

0 no-whole ridership so all riderships are in the form 2.0 3.0 etc non of them is has a decimal number like 3.5 so we are fine doing the conversion to whole numbers, 

All timestamps inside July 2024 ( dataset of ridership for july used for testing and first checks). 

We have no duplicate rows (we checked), 

and on finding #1, the only non-number IDs are TRAM1/TRAM2 (9,186 rows) as we have listed, which are removed with the trams already here we are considering only subways and they have IDs which numbers but written as strings after checking with [14]th 

| 5 | ridership | the smallest ridership number we have per hour  is 1, it is never 0: an hour with nobody entering has no row at all | all rows (2 156 907) | a missing row means 0 riders: when computing "normal riders per hour", divide by the number of days, not by the number of rows |


Now we move on to the stations table 

|6 | stations | Ridership station complex ID is stored as a text while the complex_id in the stations table is a number so this will create a problem of matching in the join | all rows (2 156 907) | we should convert the station_comple_id to a number before joining the two tables and we count the rows that fail in the coversion |

| 7 | stations | we have each row representing one stop, one row = one stop, not one station: a complex can have several stations and tehrefore rows (example Times Sq-42 St, complex 611) | 496 rows for which complexes | group the stations by Complex ID before joining with ridership |

| 8 | stations | borough is a code (M, Bk, Q, Bx, SI) while ridership writes in full names (Manhattan, Brooklyn…) | all rows (496) | map each code to its full name |

| 9 | stations | ADA Notes contains the text "NaN" instead of an empty value (a fake / dummy value) | 487 of 496 rows | replace "NaN" with a real empty value (null) |


Now we joing check the ridership table with the stations table: 

| 10 | ridership and stations | join check: 0 ridership complexes without a station; 21 station complexes without subway ridership = the Staten Island Railway which are out of scope | 0 lost | Since there is no problem here we can join on complex_id after converting it to a number |



Now we move on the the weather table 

| 10 | weather | the file has 124 columns, and REPORT_TYPE and SOURCE each appear twice in the header; Spark silently renames them respectively  (REPORT_TYPE2 / REPORT_TYPE95, SOURCE3 / SOURCE96) | for all of the rows | We will check if the two copies are identical then we only keep one and also we only keep the 6 columns we need |
| 11 | weather | Very Iportant issue:  the DATE is in Local Standard Time (UTC−5 all year), not New York clock time: in July DATE 00:51 = 05:51 UTC = 01:51 New York time | all | convert: DATE + 5 h = UTC, then UTC → New York time, before joining with ridership |
| 12 | weather | The weather file has 4 kinds of rows, not only hourly reports. We need one report per hour, but the file also contains extra reports when the weather changes quickly (FM-16), one summary per day (SOD) and one summary for the month (SOM). | 221 extra rows (189 + 31 + 1); 744 hourly rows that we should keep | Keep only the normal hourly reports (FM-15), so each hour has exactly one weather report. |
| 13 | weather | HourlyPrecipitation contains the letter "T" ( it means trace: rain too small to measure, under 0.1 mm) inside a column of numbers | it exists in 50 rows | replace "T" by 0 mm, then convert the column to a number |


