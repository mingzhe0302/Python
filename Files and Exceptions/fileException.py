#3. display_file.py
def main():
    filename = input("Enter a filename: ")

    try: 
        infile = open(filename, "r")

        contents = infile.read()

        print(contents)

        infile.close

    except IOError:
        print("An error occured trying to read the file", filename)

main()