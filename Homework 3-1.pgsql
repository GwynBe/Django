SELECT "name", phone, contact_name FROM customer WHERE address LIKE '%Hà Nội%';

SELECT * FROM product WHERE quantity > 50 AND price > 2000000;

SELECT * FROM product LEFT JOIN order_detail ON product.id = order_detail.product_id WHERE order_detail.product_id IS NULL;

SELECT * FROM product WHERE price = (SELECT MAX(price) FROM product);

SELECT employe
e_id, COUNT(employee_id) AS sale FROM "order" WHERE (ordered_at BETWEEN 01-01-2022 AND 31-03-2022) GROUP BY employee_id ORDER BY sale DESC LIMIT 1;

SELECT employee.id AS id, employee.name AS "name", COUNT("order".employee_id) AS sale FROM "order" JOIN employee ON "order".employee_id = employee.id 
WHERE (ordered_at BETWEEN 01-01-2022 AND 31-03-2022) GROUP BY "order".employee_id ORDER BY sale DESC;   