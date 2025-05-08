import hashlib
import psycopg2
from psycopg2 import sql
from datetime import datetime

def hash_transaction(transaction):
        record =(f"{transaction['transaction_id']}{transaction['user_ID']}{transaction['amount']}{transaction['timestamp']}{transaction['merchant_id']}")
        return hashlib.sha256(record.encode('utf-8')).hexdigest()

def connect_db():
    
        conn = psycopg2.connect(
        dbname="secure_transaction",
        user="postgres",
        password="saini121",
        host="localhost",
        port="5432"
        )
        return conn
        
def log_transaction(conn, transaction):
        hashed_value= hash_transaction(transaction)

        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO transaction (transaction_id, user_ID, amount, timestamp, merchant_id, hashed_value)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                transaction['transaction_id'],
                transaction['user_ID'],
                transaction['amount'],
                transaction['timestamp'],
                transaction['merchant_id'],
                hashed_value
            ))
            conn.commit()
            print("Transaction logged successfully.")  

               