import requests
from bs4 import BeautifulSoup
import csv

# Function to extract meta tags
def extract_meta(soup):
    meta_title = soup.find('title').text if soup.find('title') else ''
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description['content'] if meta_description else ''
    return meta_title, meta_description

# Function to extract social media links
def extract_social_media_links(soup):
    social_media_links = []
    for a in soup.find_all('a', href=True):
        if any(s in a['href'] for s in ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'youtube.com']):
            social_media_links.append(a['href'])
    return ', '.join(social_media_links)

# Function to extract tech stack
def extract_tech_stack(soup):
    scripts = soup.find_all('script')
    tech_stack = []
    for script in scripts:
        if 'jquery' in str(script).lower():
            tech_stack.append('jQuery')
        if 'react' in str(script).lower():
            tech_stack.append('React')
        if 'vue' in str(script).lower():
            tech_stack.append('Vue.js')
        if 'angular' in str(script).lower():
            tech_stack.append('Angular')
    return ', '.join(set(tech_stack))

# Function to extract payment gateways
def extract_payment_gateways(soup):
    payment_gateways = []
    if 'paypal' in soup.text.lower():
        payment_gateways.append('PayPal')
    if 'stripe' in soup.text.lower():
        payment_gateways.append('Stripe')
    if 'razorpay' in soup.text.lower():
        payment_gateways.append('Razorpay')
    return ', '.join(payment_gateways)

# Function to extract language
def extract_language(soup):
    language = soup.find('html')['lang'] if soup.find('html') and 'lang' in soup.find('html').attrs else ''
    return language

# Function to determine category (dummy function)
def determine_category(url):
    return 'General'

# Function to scrape a single website
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        meta_title, meta_description = extract_meta(soup)
        social_media_links = extract_social_media_links(soup)
        tech_stack = extract_tech_stack(soup)
        payment_gateways = extract_payment_gateways(soup)
        language = extract_language(soup)
        category = determine_category(url)

        return {
            'url': url,
            'meta_title': meta_title,
            'meta_description': meta_description,
            'social_media_links': social_media_links,
            'tech_stack': tech_stack,
            'payment_gateways': payment_gateways,
            'language': language,
            'category': category
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None

# Main function to scrape multiple websites from a CSV file
def main(csv_file, output_file):
    scraped_data = []
    try:
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                url = row['url'].strip()
                if url:
                    data = scrape_website(url)
                    if data:
                        scraped_data.append(data)

        # Write scraped data to CSV file for SQL table creation
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['url', 'meta_title', 'meta_description', 'social_media_links', 'tech_stack', 'payment_gateways', 'language', 'category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for data in scraped_data:
                writer.writerow(data)

        print(f"Output saved to {output_file}")
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")

if __name__ == "__main__":
    csv_file = 'websites_list.csv'
    output_file = 'scraped_data.csv'
    main(csv_file, output_file)
