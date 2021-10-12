# WebsiteScrapeAndRank
A small repo that has a mini flask service and seperate python programs to scrape and rank keywords from websites (only one page scraped) with TF-IDF scores and ngrams (mono,bi,tri)
This repo can be used to extract keywords and rank them based on TF-IDF scores, create, mono,bi and trigrams and analyze the keywords for tasks such as SEO.
We can also generate word-clouds from the text analyzed.

There are three ways to analyze textual data
 1. Launch the small flask webservice (It only has a basic page) and upload a HTML file or copy paste the text
 2. Inside the "Tests" folder use text_analyzer_test.py - used for file analysis
 3. Inside the "Tests" folder use url_analyizer.py - used for url analysis


Note that some websites will not allow access to the service, In that case download the html page and use one of the analyzers in the test folder

"Below outputs are from dawn.com @12/10/2021" using url analyzer

![dawn_cloud](https://user-images.githubusercontent.com/2294224/136967634-5acca3ea-9771-40de-9798-c51a5fb50a45.png)
![dawn_tri](https://user-images.githubusercontent.com/2294224/136967561-0807f522-05aa-4849-a151-07acaac064a4.png)
![dawn_bi](https://user-images.githubusercontent.com/2294224/136967564-0a62b9ee-53ad-456c-a043-3699a01334b2.png)
![dawn_mono](https://user-images.githubusercontent.com/2294224/136967566-220dd027-79b6-4dd0-b94d-f82cc1b1f043.png)


|    | Keyword     |   Frequency |
|---:|:------------|------------:|
|  0 | oct         |          27 |
|  1 | pm          |          20 |
|  2 | read        |          17 |
|  3 | published   |          15 |
|  4 | updated     |          14 |
|  5 | afghan      |          12 |
|  6 | papers      |          10 |
|  7 | pakistan    |           9 |
|  8 | minister    |           9 |
|  9 | world       |           8 |
| 10 | says        |           8 |
| 11 | business    |           7 |
| 12 | us          |           7 |
| 13 | dawn        |           5 |
| 14 | taliban     |           5 |
| 15 | wants       |           5 |
| 16 | education   |           5 |
| 17 | case        |           5 |
| 18 | dr          |           5 |
| 19 | health      |           5 |
| 20 | water       |           5 |
| 21 | com         |           4 |
| 22 | live        |           4 |
| 23 | images      |           4 |
| 24 | coronavirus |           4 |

|    | Bi-gram                         |   Frequency |
|---:|:--------------------------------|------------:|
|  0 | afghan taliban                  |           4 |
|  1 | taliban minister                |           4 |
|  2 | minister wants                  |           4 |
|  3 | wants good                      |           4 |
|  4 | good relations                  |           4 |
|  5 | humanitarian crisisfocusitaly   |           4 |
|  6 | crisisfocusitaly hosts          |           4 |
|  7 | afghan summit                   |           4 |
|  8 | namedpandora papers             |           4 |
|  9 | cantaliban suppresspotentthreat |           3 |
| 10 | talkstaliban candidprofessional |           3 |
| 11 | says us                         |           3 |
| 12 | abdul qadeer                    |           3 |
| 13 | sunday magazine                 |           3 |
| 14 | non fiction                     |           3 |
| 15 | herald aurora                   |           2 |
| 16 | classifieds obituaries          |           2 |
| 17 | dawn news                       |           2 |
| 18 | home latest                     |           2 |
| 19 | latest coronavirus              |           2 |
| 20 | coronavirus pakistan            |           2 |
| 21 | pakistan business               |           2 |
| 22 | business opinion                |           2 |
| 23 | opinion culture                 |           2 |
| 24 | culture sport                   |           2 |


