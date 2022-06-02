INSERT INTO roles (title) VALUES ('admin'),('manager'),('staff'),('staff');


INSERT INTO users (email,password,first_name,last_name,tel_no,address,roles_id) VALUES 
('staff1@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Olive','Yew','02657810538','No 1 pham van bach lane',3),
('staff2@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Bugg','Aida','02653451038','No 1 pham van bach lane',4),
('admin@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Ray','Sin','02657810425','No 1 pham van bach lane',1),
('manager@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Isabelle','Ringing','0265781048','No 1 pham van bach lane',2),
('customer1@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Wind','Augusta','0572724096','No 20 pham ngoc thach street',NULL),
('customer2@example.com','$2b$12$cfe5bc28b8838b3a28c1fuhzMY6onlDQ8sorSGxhE6HYrI8DxIsNC','Des','Ignayshun','057272240789','No 23 to ngoc van street',NULL);


INSERT INTO staffs (users_id) VALUES (1),(2),(3),(4);


INSERT INTO customers (users_id) VALUES (5),(6);


INSERT INTO carts(purchase_date,paymented,customer_id) VALUES ('2009-8-12',false,'1'),('2009-4-12',false,'2');


INSERT INTO books(store_area,book_name,author,publication_year,publishing_company,sold,price)
VALUES
('c5','Name Of The Mountain','Sly Meedentalfloss','5-10-2010','Green and Schaden',FALSE,552),
('a5','Name Of The river','Patty Furniture','11-30-2012','Hettinger',False,517),
('b7','Cats And Guardians','Chris Anthemum','10-11-1999','Schamberger' ,FALSE,554);


INSERT INTO categorys(title,books_id) VALUES ('architecture',1),('cookbook',2),('economics',3);

INSERT INTO book_cart (carts_id,books_id) VALUES (1,1),(1,2),(1,3),(2,1),(2,2),(2,3);









