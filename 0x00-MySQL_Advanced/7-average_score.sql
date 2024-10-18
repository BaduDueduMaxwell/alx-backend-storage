-- This script creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SELECT AVG(user_id)
    FROM users;
END $$

DELIMITER;