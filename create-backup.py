#!/usr/bin/env python3
import os
import zipfile
import shutil
from pathlib import Path

# 項目目錄
project_dir = Path('/Users/idea3c/myancasino-clone')
output_file = Path('/Users/idea3c/Desktop/myanbetapp-complete-website.zip')

# 要排除的文件和目錄
exclude_patterns = ['.git', '.gitignore', '*.sh', 'create-backup.py']

def should_exclude(file_path):
    """檢查文件是否應該被排除"""
    file_str = str(file_path)
    if '.git' in file_str:
        return True
    if file_path.suffix == '.sh':
        return True
    if file_path.name == 'create-backup.py':
        return True
    return False

# 創建 ZIP 文件
print(f"正在創建備份文件: {output_file}")
with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        # 排除 .git 目錄
        dirs[:] = [d for d in dirs if d != '.git']
        
        for file in files:
            file_path = Path(root) / file
            if should_exclude(file_path):
                continue
            
            # 計算相對路徑
            arcname = file_path.relative_to(project_dir)
            zipf.write(file_path, arcname)
            print(f"已添加: {arcname}")

print(f"\n✅ 備份完成！")
print(f"文件位置: {output_file}")
print(f"文件大小: {output_file.stat().st_size / 1024 / 1024:.2f} MB")

