import requests

def main():
    input(url)
    r = requests.get(url)
    with open('test.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)
 
if __name__ == '__main__':
    main()
