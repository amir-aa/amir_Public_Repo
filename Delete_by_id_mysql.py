import mysql.connector

# MySQL connection configuration
mysql_config = {
    'host': '192.168.248.12',
    'user': 'root',
    'password': 'DenZel00@',
    'database': '_smsengine'
}

# Function to execute delete queries in batches using executemany
def delete_in_batches(ids, batch_size=1000):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    total_ids = len(ids)
    for i in range(0, total_ids, batch_size):
        batch_ids = ids[i:i + batch_size]
        query = "DELETE FROM _sent_history_2 WHERE id = %s"

        try:
            cursor.executemany(query, [(id,) for id in batch_ids])
            conn.commit()
            print(f"Batch {i // batch_size + 1} executed successfully.")
        except Exception as e:
            conn.rollback()
            print(f"Error executing batch {i // batch_size + 1}: {e}")

    cursor.close()
    conn.close()

#to read IDs
def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        ids = [line.strip() for line in file]
    return ids

if __name__ == '__main__':
    file_path = 'ids.txt'  # Update with your file path
    ids_to_delete = read_ids_from_file(file_path)

    if ids_to_delete:
        delete_in_batches(ids_to_delete)
    else:
        print("No IDs found in the file.")
