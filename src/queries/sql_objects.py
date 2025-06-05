from src.db.connector import DatabaseConnector

def crear_vista_clientes_frecuentes():
    sql = """
    CREATE OR REPLACE VIEW vista_clientes_frecuentes AS
    SELECT customer_id, SUM(quantity) AS total_compras
    FROM sales
    GROUP BY customer_id
    HAVING total_compras > 100;
    """
    db = DatabaseConnector()
    db.execute_statement(sql)

def crear_funcion_total_ventas_por_cliente():
    sql_drop = "DROP FUNCTION IF EXISTS total_ventas_por_cliente;"
    sql_create = """
    CREATE FUNCTION total_ventas_por_cliente(cid INT)
    RETURNS INT
    DETERMINISTIC
    READS SQL DATA
    BEGIN
        DECLARE total INT;
        SELECT SUM(quantity) INTO total
        FROM sales
        WHERE customer_id = cid;
        RETURN IFNULL(total, 0);
    END;
    """
    db = DatabaseConnector()
    db.execute_statement(sql_drop)
    db.execute_statement(sql_create)

def crear_tabla_clientes_frecuentes_log():
    sql = """
    CREATE TABLE IF NOT EXISTS clientes_frecuentes_log (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        total_compras INT,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    db = DatabaseConnector()
    db.execute_statement(sql)

def crear_procedimiento_marcar_clientes_frecuentes():
    db = DatabaseConnector()

    sql_drop = "DROP PROCEDURE IF EXISTS marcar_clientes_frecuentes;"
    db.execute_statement(sql_drop)

    sql_create = """
    CREATE PROCEDURE marcar_clientes_frecuentes()
    BEGIN
        DELETE FROM clientes_frecuentes_log;

        INSERT INTO clientes_frecuentes_log (customer_id, total_compras)
        SELECT customer_id, SUM(quantity) AS total_compras
        FROM sales
        GROUP BY customer_id
        HAVING total_compras > 100;
    END;
    """
    db.execute_statement(sql_create)
