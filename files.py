class Files:
    def _init_(self):

        self.txt_files = []
        self.pdf_files = []
        self.jpeg_files = []
    def add_file(self):
        file_name = input('please enter the name of the file')
        file_format = input('please enter the format of your file')
        if file_format != 'jpeg':
            file_name = file_name + file_format
            if file_format == 'txt':
                my_file = open(file_name, mode="w")
                self.txt_files.append(my_file)
                my_file.close()

            if file_format == 'pdf':
                my_file = open(file_name, mode="w")
                self.pdf_files.append(my_file)
                my_file.close()

        elif file_format == 'jpeg':
            file_name = file_name + file_format
            my_file = open(file_name, mode='wb')
            self.jpeg_files.append(my_file)
            my_file.close()
            self.txt_files

    def clear_list(self, list_format):
        if list_format == 'txt':
            self.txt_files.clear()

        elif list_format == 'pdf':
            self.pdf_files.clear()

        else:
            self.jpeg_files.clear()

    def remove_index(self, index, list_format):
        if list_format == 'txt':
            self.txt_files.pop(index)

        elif list_format == 'pdf':
            self.pdf_files.pop(index)

        else:
            self.jpeg_files.pop(index)

    def remove_all_lists(self):
        key = input('are you sure to delete all your lists?')
        if key == 'yes':
            self.txt_files.clear()
            self.txt_files.clear()
            self.txt_files.clear()

    def get_list_by_format(self, list_format):
        if list_format == 'txt':
            return self.txt_files

        elif list_format == 'pdf':
            return self.pdf_files.pop

        else:
            return self.jpeg_files.pop

    def get_list_with_index(self, list_format, index):
        if index < 0 and index > len(self.txt_files) or index > len(self.pdf_files) or index > len(self.jpeg_files):
            return 'invalid index'

        if list_format == 'txt':
            return self.txt_file[index]

        elif list_format == 'pdf':
            return self.pdf_files[index]

        else:
            return self.jpeg_files[index]



















