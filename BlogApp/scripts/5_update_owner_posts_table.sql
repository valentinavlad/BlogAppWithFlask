UPDATE posts p
SET    owner = u.user_id
FROM   users u
WHERE  p.owner_cp = u.name;