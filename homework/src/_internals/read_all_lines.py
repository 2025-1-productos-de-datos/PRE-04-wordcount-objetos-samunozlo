import os

class ReadAllLinesMixin:
    def read_all_lines(self):
        """Read all lines from all files in the input folder."""
        self.lines = []

        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.lines.extend(f.readlines())
