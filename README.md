# WebsiteScrapeAndRank
A small repo that has a mini flask service and seperate python programs to scrape and rank keywords from websites (only one page scraped) with TF-IDF scores and ngrams (mono,bi,tri)
This repo can be used to extract keywords and rank them based on TF-IDF scores, create, mono,bi and trigrams and analyze the keywords for tasks such as SEO.
We can also generate word-clouds from the text analyzed.

There are three ways to analyze textual data
 1. Launch the small flask webservice (It only has a basic page) and upload a HTML file or copy paste the text
 2. Inside the "Tests" folder use text_analyzer_test.py - used for file analysis
 3. Inside the "Tests" folder use url_analyizer.py - used for url analysis


Note that some websites will not allow access to the service, In that case download the html page and use one of the analyzers in the test folder

Below outputs are from https://visitduabi.com/en/ @12/10/2021 using url analyzer

![dawn_cloud](https://user-images.githubusercontent.com/2294224/136968819-12b83e5f-26e7-4c64-baba-70095d79ee16.png)
![dawn_mono](https://user-images.githubusercontent.com/2294224/136968822-a41950d0-6a8b-4970-824c-f2c69a04faa7.png)
![dawn_bi](https://user-images.githubusercontent.com/2294224/136968816-fb01601a-22ec-42ca-9faf-5d11255837f6.png)
![dawn_tri](https://user-images.githubusercontent.com/2294224/136968823-554e4a72-eedd-4b13-9994-3f6c90ad79b7.png)



|    | Keyword       |   Frequency |
|---:|:--------------|------------:|
|  0 | dubai         |          33 |
|  1 | al            |          16 |
|  2 | jumeirah      |           6 |
|  3 | visit         |           5 |
|  4 | discover      |           5 |
|  5 | travel        |           4 |
|  6 | login         |           4 |
|  7 | things        |           4 |
|  8 | new           |           4 |
|  9 | food          |           4 |
| 10 | barsha        |           4 |
| 11 | businessdubai |           3 |
| 12 | culture       |           3 |
| 13 | arts          |           3 |
| 14 | get           |           3 |
| 15 | drink         |           3 |
| 16 | find          |           3 |
| 17 | visa          |           3 |
| 18 | guide         |           3 |
| 19 | hearstory     |           3 |
| 20 | fromeyes      |           3 |
| 21 | ofpeople      |           3 |
| 22 | seef          |           3 |
| 23 | advisory      |           2 |
| 24 | register      |           2 |

|    | Bi-gram               |   Frequency |
|---:|:----------------------|------------:|
|  0 | visit dubai           |           4 |
|  1 | visa guide            |           3 |
|  2 | hearstory discover    |           3 |
|  3 | discover dubai        |           3 |
|  4 | dubai fromeyes        |           3 |
|  5 | fromeyes ofpeople     |           3 |
|  6 | al seef               |           3 |
|  7 | login register        |           2 |
|  8 | dubai businessdubai   |           2 |
|  9 | businessdubai travel  |           2 |
| 10 | travel trade          |           2 |
| 11 | trade study           |           2 |
| 12 | study dubai           |           2 |
| 13 | dubai retiredubai     |           2 |
| 14 | retiredubai corporate |           2 |
| 15 | dubai get             |           2 |
| 16 | toin dubai            |           2 |
| 17 | dubai presents        |           2 |
| 18 | related sites         |           2 |
| 19 | palm jumeirah         |           2 |
| 20 | downtown dubai        |           2 |
| 21 | dubai marina          |           2 |
| 22 | bur dubai             |           2 |
| 23 | al barsha             |           2 |
| 24 | barsha heights        |           2 |

|    | Tri-gram                                                             |   Frequency |
|---:|:---------------------------------------------------------------------|------------:|
|  0 | hearstory discover dubai                                             |           3 |
|  1 | discover dubai fromeyes                                              |           3 |
|  2 | dubai fromeyes ofpeople                                              |           3 |
|  3 | visit dubai businessdubai                                            |           2 |
|  4 | dubai businessdubai travel                                           |           2 |
|  5 | businessdubai travel trade                                           |           2 |
|  6 | travel trade study                                                   |           2 |
|  7 | trade study dubai                                                    |           2 |
|  8 | study dubai retiredubai                                              |           2 |
|  9 | dubai retiredubai corporate                                          |           2 |
| 10 | dubai international financial                                        |           2 |
| 11 | international financial centre                                       |           2 |
| 12 | dubai design district                                                |           2 |
| 13 | jumeirah lakes towers                                                |           2 |
| 14 | official tourism boarddubaisafetyour                                 |           1 |
| 15 | tourism boarddubaisafetyour priority                                 |           1 |
| 16 | logincreateaccountsavefavouritesreceive personalised recommendations |           1 |
| 17 | login register loginlike                                             |           1 |
| 18 | register loginlike sign                                              |           1 |
| 19 | loginlike sign inregisterlikecontent                                 |           1 |
| 20 | sign inregisterlikecontent login                                     |           1 |
| 21 | inregisterlikecontent login register                                 |           1 |
| 22 | login register visit                                                 |           1 |
| 23 | register visit dubai                                                 |           1 |
| 24 | retiredubai corporate aa                                             |           1 |

| keywords    |   tf-df score |
|:------------|--------------:|
| visit dubai |         0.668 |
| visit       |         0.635 |
| dubai       |         0.387 |
| 24 | culture sport                   |           2 |


