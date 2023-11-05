-- Average score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE total_score FLOAT;
  DECLARE total_count INT;

  SELECT SUM(score) INTO total_score
  FROM corrections
  WHERE user_id = user_id;

  SELECT COUNT(*) INTO total_count
  FROM corrections
  WHERE user_id = user_id;

  IF total_count > 0 THEN
    UPDATE users
    SET average_score = total_score / total_count
    WHERE id = user_id;
  END IF;
END;
//
DELIMITER ;
