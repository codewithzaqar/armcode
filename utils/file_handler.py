class FileHandler:
    @staticmethod
    def new_file():
        return ""  # Placeholder for new file content

    @staticmethod
    def open_file(filepath):
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error: {str(e)}"
        
    @staticmethod
    def save_file(filepath, content):
        try:
            with open(filepath, 'w') as f:
                f.write(content)
            return True
        except Exception as e:
            return f"Error: {str(e)}"