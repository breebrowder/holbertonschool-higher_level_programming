-- List # of records with same score in table of hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
