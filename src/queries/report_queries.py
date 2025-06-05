from src.db.connector import DatabaseConnector

def compras_por_cliente(min_compras: int = 10):
    sql = f"""
    WITH compras_por_cliente AS (
        SELECT customer_id, SUM(quantity) AS total_compras
        FROM sales
        GROUP BY customer_id
    )
    SELECT customer_id, total_compras
    FROM compras_por_cliente
    WHERE total_compras > {min_compras};
    """
    db = DatabaseConnector()
    return db.execute_query(sql)

def ranking_productos_por_categoria():
    sql = """
    WITH ventas_agrupadas AS (
        SELECT
            p.category_id,
            s.product_id,
            p.name AS product_name,
            SUM(s.quantity) AS total_quantity
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.category_id, s.product_id, p.name
    ),
    ranking_cte AS (
        SELECT
            category_id,
            product_id,
            product_name,
            total_quantity,
            RANK() OVER (PARTITION BY category_id ORDER BY total_quantity DESC) AS rnk
        FROM ventas_agrupadas
    )
    SELECT *
    FROM ranking_cte
    WHERE rnk <= 3
    ORDER BY category_id, rnk;
    """
    db = DatabaseConnector()
    return db.execute_query(sql)
