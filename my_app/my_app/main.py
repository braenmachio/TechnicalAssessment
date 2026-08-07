import os
import sys
import time

import psycopg


def get_conn_info() -> str:
    return (
        f"host={os.environ.get('PGHOST', 'localhost')} "
        f"port={os.environ.get('PGPORT', '5432')} "
        f"dbname={os.environ.get('PGDATABASE', 'postgres')} "
        f"user={os.environ.get('PGUSER', 'postgres')} "
        f"password={os.environ.get('PGPASSWORD', 'postgres')}"
    )


def main() -> None:
    conninfo = get_conn_info()
    print(f"psycopg version: {psycopg.__version__}")
    print(f"Connecting with: {conninfo}")

    # Retry loop: gives the Postgres container time to become ready
    last_err = None
    for attempt in range(1, 11):
        try:
            with psycopg.connect(conninfo, connect_timeout=3) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT version();")
                    row = cur.fetchone()
                    print(f"Connected successfully. Server says: {row[0]}")
                    return
        except psycopg.OperationalError as e:
            last_err = e
            print(f"Attempt {attempt}/10 failed, retrying in 2s...")
            time.sleep(2)

    print(f"Could not connect to Postgres: {last_err}")
    sys.exit(1)


if __name__ == "__main__":
    main()
