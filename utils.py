def read_last_id(file_name):
    file_read = open(file_name, 'r')
    last_id = int(file_read.read().strip())
    file_read.close()
    return last_id

def store_last_id(file_name, id):
    file_write = open(file_name, 'w')
    file_write.write(str(id))
    file_write.close()