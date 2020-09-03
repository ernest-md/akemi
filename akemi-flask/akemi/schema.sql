DROP TABLE IF EXISTS products;

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price INTEGER NOT NULL,
  src TEXT NOT NULL
);

INSERT INTO products VALUES 
(1, 'Kameco Sport Capless Roller Pen and Pencil Set in Pouch White', 130.00, 'imgs/offer1.png'),
(2, 'Hacoa masking Tape Holder', 22.00, 'imgs/offer2.png'),
(3, 'Hacoa Black Walnut Business Card Holder', 75.50, 'imgs/offer3.png'),
(4, 'Postalco Legal Envelope Navy', 50.99, 'imgs/offer4.png');
