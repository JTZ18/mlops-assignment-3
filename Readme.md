# MLOps Assignment 3

This repository contains the code for MLOps Assignment 3.

## Setup

To set up the project, you need to run the `setup.sh` script. This script will download the necessary `data`, `faiss_index`, and `cache` folders for you and place them into the repository. This will speed up your workflow as you won't have to chunk and embed the data which is time consuming on the edu cluster.

To run the script, open a terminal in the repository directory and type:

```bash
./setup.sh
```

This will start the download and extraction process. Once the script finishes running, you should see the data, faiss_index, and cache folders in your repository directory.

## Usage
This assignment is divided into two parts: `assignment_03-Part1.ipynb` and `assignment_03-Part2.ipynb`.

### Part 1

The first part of the assignment contains all our answers to the questions, including the interview questions and Value Proposition Canvas. It also contains the original code and model for the Retrieval-Augmented Generation (RAG) without any upgraded modifications.

### Part 2

The second part of the assignment contains our solution to trying different methods to improve the quality of RAG answers. Here's what we did:

1. **Web Scraping**: We scraped all related links to `https://sutd.edu.sg`. This gave us a total of 7036 links, which can be found in the file `scraped/sutd_full_url.txt`.

2. **Link Pruning**: We pruned the links to 6204 links by sorting the links by domain and by tree depth level to observe the relevance of a URL link. The pruned links can be found in the file `scraped/cleaned_urls.txt`.

3. **Scrapy Scraper**: We used a Scrapy scraper to scrape the web pages. The code for the scraper can be found in the `SUTD-crawler` folder.

4. **Different Model**: We tried a different model, `vicuna-7b-v1.5`, to see if it could improve the quality of the answers.

5. **Improved RAG Pipeline**: We tried implementing a better RAG pipeline using Hypothetical Document Embeddings (HyDE). This approach generates hypothetical document embeddings to perform similarity search for relevant documents based on a query.
