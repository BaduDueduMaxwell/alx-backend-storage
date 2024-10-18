-- This script creates a function SafeDiv that divides a by b and returns 0 if b is 0
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 4)
DETERMINISTIC
BEGIN
    -- Check if b is 0 to avoid division by zero
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN CAST(a AS DECIMAL(10, 4)) / CAST(b AS DECIMAL(10, 4));
    END IF;
END $$

DELIMITER ;
