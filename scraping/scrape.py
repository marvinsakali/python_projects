from bs4 import BeautifulSoup
import requests
import csv


# function to scrape books
def scrape(pages):
    # creating a csv file to save the quotes
    with open("quotes.csv", "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])  # column titles        

        # loops through the pages extracting info
        for page in range(1, pages+1):
            url = f"https://quotes.toscrape.com/page/{page}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all("div", class_="quote")
            print(f"Scrapping page {page}...")

            for quote in quotes:
                text = quote.find("span", class_="text").get_text()
                author = quote.find("small", class_="author").get_text()
                tags = [t.get_text()
                        for t in quote.find_all("a", class_="tag")]
                writer.writerow([text, author, ",".join(tags)])
        
        print("DONE!!")


scrape(10)
