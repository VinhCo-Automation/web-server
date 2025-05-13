import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="b3tctusvlvharcpxgk0x-mysql.services.clever-cloud.com",
        user="uutfyaq5terklpid",
        password="hmFL9JYj9speFoLSuw1d",
        database="b3tctusvlvharcpxgk0x"
    )
db_config = {
    "host": "b3tctusvlvharcpxgk0x-mysql.services.clever-cloud.com",
    "user": "uutfyaq5terklpid",
    "password": "hmFL9JYj9speFoLSuw1d",
    "database": "b3tctusvlvharcpxgk0x"
}
