from dot_asterix import count_lines


def main():
    with open(r'C:\Users\USER\Documents\alice30.txt') as text:
        text_to_be_sent = text.read()
        print(count_lines(text_to_be_sent))


if __name__ == '__main__':
    main()
