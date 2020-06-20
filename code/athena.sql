SELECT city, MAX(temperature) as max_temperature_jun_2020
FROM "examples"."weather"
WHERE
  city IN ('Tokyo', 'Beijing', 'Singapore')
  AND year = 2020
  AND month = 6
GROUP BY city
ORDER BY max_temperature_jun_2020
;
