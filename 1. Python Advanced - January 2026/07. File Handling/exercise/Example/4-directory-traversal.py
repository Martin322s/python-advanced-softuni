import os

def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file):
            save_extensions(file)


directory = input()
extensions = {}

save_extensions(directory)

sorted_extensions = dict(sorted(extensions.items(), key=lambda x: x[0]))

with open("./report.txt", "w") as report_file:
    for extension, files in sorted_extensions.items():
        report_file.write(f".{extension}\n")

        for file in sorted(files):
            report_file.write(f"- - - {file}\n")