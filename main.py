from datetime import datetime
from Transaction_logger import connect_db, log_transaction

transaction= {
    "transaction_id": "TXN1001",
    "user_ID": "USR123",
    "amount": 10000,
    "timestamp": datetime.now(),
    "merchant_id": "MRC456"
}

if __name__ == "__main__":
    conn = connect_db()
    log_transaction(conn, transaction)
    print("Transaction logged successfully.")
    conn.close()