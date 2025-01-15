import os
import hashlib

def calculate_md5(file_path):
    """计算文件的 MD5 哈希值"""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)  # 读取 4KB 的数据块
                if not chunk:
                    break
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def get_all_files_md5(directory):
    """获取指定目录下所有文件的 MD5 哈希值"""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            md5_value = calculate_md5(file_path)
            if md5_value:
                print(f"{file_path} : {md5_value}")

if __name__ == "__main__":
    target_directory = r"D:\python全"  # 指定要查找的目录
    get_all_files_md5(target_directory)
