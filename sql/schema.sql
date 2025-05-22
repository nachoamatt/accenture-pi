-- Asegurate de estar en la base correcta
USE supermercado;

-- Tabla: countries
CREATE TABLE countries (
    country_id INT PRIMARY KEY,
    name VARCHAR(100),
    code VARCHAR(10)
);

-- Tabla: cities
CREATE TABLE cities (
    city_id INT PRIMARY KEY,
    name VARCHAR(100),
    zipcode VARCHAR(20),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Tabla: categories
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Tabla: products
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    category_id INT,
    modify_date DATE,
    product_class VARCHAR(50),
    resistant VARCHAR(10),
    is_allergic VARCHAR(10),
    vitality_days INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Tabla: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial VARCHAR(10),
    last_name VARCHAR(100),
    address VARCHAR(255),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Tabla: employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    middle_initial VARCHAR(10),
    last_name VARCHAR(100),
    birth_date DATE,
    gender VARCHAR(10),
    hire_date DATE,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Tabla: sales
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    discount DECIMAL(5,2),
    total_price DECIMAL(10,2),
    sale_date DATE,
    transaction_number VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
