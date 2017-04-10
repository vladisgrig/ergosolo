SELECT name, COUNT(course_id) from (
  SELECT user_id, course_id, count(*) as ex_count
  FROM saves
  GROUP BY user_id, course_id
)
JOIN users on users.id = user_id
WHERE ex_count > 100
GROUP BY name;
