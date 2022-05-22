SELECT ID as id,
case
WHEN P_ID IS NULL THEN 'Root'
WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
ELSE 'Leaf'
end AS type FROM TREE;