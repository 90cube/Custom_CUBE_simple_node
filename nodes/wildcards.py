import os
import re
import folder_paths

class CLIPTextEncodeWithWildcards:
    def __init__(self):
        self.base_path = os.path.join(folder_paths.base_path, "wildcards")

    def get_available_categories(self):
        """ wildcards 폴더 내부의 폴더 목록을 반환 """
        return [d for d in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, d))]

    def get_files_in_category(self, category):
        """ 특정 폴더(category) 내의 모든 .txt 파일 리스트 반환 """
        category_path = os.path.join(self.base_path, category)
        if not os.path.exists(category_path):
            return []
        return [f[:-4] for f in os.listdir(category_path) if f.endswith(".txt")]  # 확장자 제외

    def read_wildcard(self, category, filename, seed):
        """ 특정 폴더 내에서 선택한 .txt 파일을 읽고 랜덤 값 반환 """
        file_path = os.path.join(self.base_path, category, filename + ".txt")  # 확장자 추가
        if not os.path.exists(file_path):
            return "FILE NOT FOUND"

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        return lines[seed % len(lines)].strip() if lines else "EMPTY"
