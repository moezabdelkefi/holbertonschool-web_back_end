-- Create a trigger to update the quantity in the "items" table after adding a new order
CREATE TRIGGER update_item_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the item quantity in the "items" table based on the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
