import os
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from datetime import datetime
import re
import concurrent.futures
import time
from requests.exceptions import RequestException, ConnectionError, HTTPError

# Disable the Hugging Face symlink warning
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Function to scrape Google search results
def google_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    
    # Extract and clean URLs from search results
    for g in soup.find_all('a'):
        link = g.get('href')
        if link and link.startswith("/url?q="):
            clean_link = re.search(r'/url\?q=(https?://[^&]+)', link)
            if clean_link:
                url = clean_link.group(1)
                # Filter out irrelevant URLs
                if not any(s in url for s in ["maps.google", "images.google", "youtube.com"]):
                    links.append(url)
    
    return links[:50]  # Limit to 50 results

# Function to scrape and summarize content from a URL
def scrape_and_summarize(url, summarizer, retries=3, delay=5):
    headers = {"User-Agent": "Mozilla/5.0"}
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join([para.text for para in paragraphs])
            
            if not text.strip():
                return f"No relevant content found to summarize for {url}."
            
            # Summary with max_length of 1000 tokens
            summary = summarizer(text, max_length=1000, min_length=100, do_sample=False)[0]['summary_text']
            
            # Convert the summary into bullet points
            bullet_points = "\n".join([f"- {sentence.strip()}" for sentence in summary.split('.') if sentence.strip()])
            return bullet_points
        
        except (RequestException, ConnectionError, HTTPError) as e:
            print(f"Error fetching content from {url}: {e}. Retrying in {delay} seconds...")
            attempt += 1
            time.sleep(delay)
    
    return f"Failed to fetch content from {url} after {retries} attempts."

# Function to save summary to a file
def save_summary(topic, summary, folder_path):
    # Create a folder for the topic if it doesn't exist
    folder_name = os.path.join(folder_path, f"Research_{topic.replace(' ', '_')}")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create a timestamped file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(folder_name, f"{timestamp}.txt")
    
    # Save the summary to the file
    with open(file_name, 'w') as file:
        file.write(summary)
    
    print(f"Summary saved to {file_name}")

# Main function to perform the research
def research_topic(topic, folder_path):
    summarizer = pipeline("summarization")
    links = google_search(topic)
    
    # Use concurrency to handle multiple requests simultaneously
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scrape_and_summarize, url, summarizer) for url in links]
        for future in concurrent.futures.as_completed(futures):
            summary = future.result()
            save_summary(topic, summary, folder_path)

if __name__ == "__main__":
    topic = input("Enter the topic to research: ")
    folder_path = input("Enter the folder path where the research should be stored: ")
    research_topic(topic, folder_path)
