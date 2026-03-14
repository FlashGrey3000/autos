from config import load_configs
import psycopg2 as ps

def getConnection():
    configs = load_configs()
    
    try:
        conn = ps.connect(**configs)
        print("database connected successfully.")

        return conn
    except Exception as e:
        print(e)

if __name__ == "__main__":
    getConnection()