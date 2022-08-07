Note the KEY statement from the description: No two characters may map to the same character.
The goal is then to verify this rule is not broken.
The statement can break down to two scenarios we need to cover:
1st: two different keys are mapped to the same char, e.g.,
'a' -> 'a'
'b' -> 'a'
It's covered in the first 'if' statement in the code below.
In order to verify that, we use a string 'val' to keep track of the dict values.
If the value is already in the string 'val', (like the example above, the value 'a' is aleady in the string 'val') then it breaks the rule, return False.
2nd: the same key is mapped to two different chars, e.g.,
'o' -> 'a'
'o' -> 'r'
It's covered in the second 'if' statement in the code.