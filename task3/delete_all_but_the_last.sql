-- Проверено на PostgreSQL 9.5.6 + Ubuntu 16.04
DELETE FROM something
WHERE id NOT IN (
  SELECT id FROM something
  ORDER BY date DESC
  LIMIT 5);
