# WebsiteScrapeAndRank
A small repo that has a service and seperate python programs to scrape and rank website pages (only one page) with TF-IDF scores and ngrams (mono,bi,tri)
This repo can be used to extract keywords and rank them based on TF-IDF scores, create, mono,bi and trigrams and analyze the keywords for tasks such as SEO.
We can also generate word-clouds from the text analyzed.

There are three ways to analyze textual data
 1. Launch the small flask webservice (It only has a basic page) and upload a HTML file or copy paste the text
 2. Inside the "Tests" folder use text_analyzer_test.py - used for file analysis
 3. Inside the "Tests" folder use url_analyizer.py - used for url analysis


Note that some websites will not allow access to the service, In that case download the html page and use one of the analyzers in the test folder

"Cloud"
![cloud](https://user-images.githubusercontent.com/2294224/136965127-bcee938c-9219-4541-b160-8320f7a91c28.png)
"Mono"
![monp](https://user-images.githubusercontent.com/2294224/136965071-0c759caa-19c0-4cab-aaac-2d6f0a304e81.png)
"Bi"
![bi](https://user-images.githubusercontent.com/2294224/136965099-8a77726b-131e-47fd-94ab-4829475a3f0d.png)
"Tri"
![tri](https://user-images.githubusercontent.com/2294224/136965110-e7f12682-7003-4801-aa95-d06b727aabdf.png)
