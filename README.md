# WebScrapeSummarizer

 Python-based tool designed to automate the process of researching topics by scraping web content and summarizing it. This project was developed to streamline the research workflow and provide concise, actionable insights from a large number of sources. Throughout the development of this tool, I gained valuable experience and insights into web scraping, natural language processing, and concurrency handling.

## Experience 
In working on the WebScrapeSummarizer project, I focused on creating an efficient and automated system for gathering and summarizing information from the web. The project involved several key learning areas:

- **Web Scraping:** I implemented methods to extract relevant URLs from Google search results and fetch content from these pages using the `requests` and `BeautifulSoup` libraries.
- **Natural Language Processing (NLP):** I integrated Hugging Face's `transformers` pipeline to summarize web content. This taught me about the practical applications of NLP models and how to leverage them for generating summaries.
- **Concurrency Handling:** To handle multiple web requests simultaneously and improve performance, I used Python's `concurrent.futures` library. This experience enhanced my understanding of concurrent programming.
- **Error Handling:** Implementing robust error handling mechanisms, including retries and delays, was crucial for dealing with network issues and ensuring the reliability of the tool.
- **File Management:** I developed a method for organizing and saving summaries with timestamped filenames, which helped in managing research outputs efficiently.

## Features

- **Google Search Integration:** Automatically performs a Google search for the given topic and extracts relevant URLs.
- **Web Scraping:** Fetches and parses content from the extracted URLs.
- **Content Summarization:** Utilizes Hugging Face's `transformers` pipeline for summarizing the content of web pages.
- **Bullet Point Formatting:** Converts summaries into easy-to-read bullet points.
- **Error Handling:** Includes retries and delays for robust error handling in case of network issues.
- **Timestamped File Saving:** Saves the summaries with timestamped filenames for better organization.
- **Concurrency Support:** Uses `ThreadPoolExecutor` to handle multiple requests concurrently for improved efficiency.

## Technologies Used

- **Python:** The programming language used for scripting and automation.
- **Requests:** Library for making HTTP requests to fetch web content.
- **BeautifulSoup:** Used for parsing HTML and extracting relevant information from web pages.
- **Transformers:** Hugging Face's library for natural language processing, specifically for summarization.
- **Concurrent Futures:** Handles multiple requests concurrently to speed up the process.
- **OS & Datetime:** For file management and timestamping.

## Workflow

1. **Search:** The tool performs a Google search for the given topic and retrieves up to 50 URLs from the search results.
2. **Scrape:** For each URL, the tool fetches the content and extracts text from paragraphs.
3. **Summarize:** The extracted text is summarized using the `transformers` summarization pipeline.
4. **Format:** The summary is converted into bullet points for clarity.
5. **Save:** Each summary is saved in a timestamped file within a topic-specific folder.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `transformers`, `concurrent.futures`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ancodernova/WebScrapeSummarizer.git
    cd WebScrapeSummarizer
    ```

2. **Install dependencies:**

    ```bash
    pip install requests beautifulsoup4 transformers
    ```

### Usage

1. **Run the script:**

    ```bash
    python WebScrapeSummarizer.py
    ```

2. **Input the topic:** Enter the topic you want to research when prompted.
3. **Specify folder path:** Enter the path where you want the research summaries to be saved.

### Example

```bash
Enter the topic to research: WebDev
Enter the folder path where the research should be stored: /path/to/save/summary
```

## Error Handling

The script includes error handling for common issues such as network errors and HTTP errors. It will retry fetching content up to three times with a five-second delay between attempts.

