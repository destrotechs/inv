
CREATE TABLE item_categories (
    category_code varchar(20) unique not null,
    category_name varchar(100) NOT NULL,
    long_desc varchar(255),
    PRIMARY KEY (category_code)
);

CREATE TABLE items (
    item_code varchar(20) unique not null,
	category_code varchar(20) not null,
    item_name varchar(255) NOT NULL,
    long_desc varchar(255),
    PRIMARY KEY (item_code),
    foreign key (category_code) references item_categories(category_code)
);

CREATE TABLE item_stock (
	stock_id serial,
    item_code varchar(20) not null,
    buying_unit_price decimal,
	quantity_in decimal,
    quantity_out decimal,
    long_desc varchar(255),
    stock_date date,
    stock_value decimal,
    PRIMARY KEY (stock_id),
    foreign key (item_code) references items(item_code)
);
CREATE TABLE item_issuance (
	issuance_id serial,
    issued_to varchar(50) not null,
	phone varchar(15),
    issue_date date,
    long_desc varchar(255),
    PRIMARY KEY (issuance_id)
);
CREATE TABLE item_issuance_items (
	item_id serial,
	issuance_id bigint not null,
    item_code varchar(20) not null,
	quantity_issued decimal,
    PRIMARY KEY (item_id),
    foreign key (issuance_id) references item_issuance(issuance_id),
    foreign key (item_code) references items(item_code)
);
CREATE TABLE sales (
	sale_id  serial,
    sold_to varchar(20),
	date_sold date,
    PRIMARY KEY (sale_id)
);
CREATE TABLE sale_items (
	item_id  serial,
	sale_id bigint not null,
    item_code varchar(20) not null,
	quantity_sold decimal,
    sellig_unit_price decimal,
    PRIMARY KEY (item_id),
    foreign key (sale_id) references sales(sale_id),
    foreign key (item_code) references items(item_code)
);
