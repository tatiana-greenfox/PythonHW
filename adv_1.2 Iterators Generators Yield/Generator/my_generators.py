import hashlib

def my_generators(path):
    with open(path, encoding='utf-8') as file_:
        for line in file_:
            line = line.strip()
            md5_hash = hashlib.md5(line.encode())
            yield f"{line} - {md5_hash.hexdigest()}"
               
if __name__ == '__main__':
    for line in my_generators('test_file.txt'):
        print(line)