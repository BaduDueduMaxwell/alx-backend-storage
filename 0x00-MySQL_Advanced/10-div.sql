-- This script creates a function SafeDiv that divides a by b and returns 0 if b is 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF (b = 0)
    THEN
        RETURN (0);
    ELSE
        RETURN (a / b);
    END IF;
END
$$ 
DELIMITER ;
