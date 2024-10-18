-- This script creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score)
    INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = input_user_id;
END $$

DELIMITER;