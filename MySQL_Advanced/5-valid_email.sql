-- Create a trigger to reset valid_email when email is updated
DELIMITER //
CREATE TRIGGER reset_valid_email_after_email_update
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email column has been updated
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
