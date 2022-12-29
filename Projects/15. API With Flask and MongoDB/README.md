# MLH Application Code Snippets

This centralized location links to all the code I am submitting for review.

## Description

These files are a part of my "Grandmaster API" project, which I created as a training exercise while I was a web development intern at Nimble Property. After exploring existing solutions, I wanted to create a user-friendly API that can serve data about the world's top chess players. First, I had to create a (web scraper)[https://github.com/sai-nayunipati/Hallmark-Induction-Projects/tree/main/Projects/14.%20Web%20Scrape%20to%20MongoDB] using the Scrapy Python library to collect the data of [chess.com's top 2500 players](https://www.chess.com/players). Then, I inserted the information into a MongoDB collection. (Although I hadn't used NoSQL databases before, I decided to explore them because relational databases seemed excessive.) Finally, I created a lightweight Flask API to allow other programs to access this data. (There are also the beginnings of human-readable HTML resources built with Bootstrap.) This API includes inserting, updating, and deleting functionality.

Although this project is simple, it gave me the skills to work on more interesting applications. Later, I was part of a team that produced Greengle, which won the "Best Code" award at the _BU Spark!_ sustainability mini-hackathon. The [project](https://github.com/AdiBhan/Greengle) estimates the carbon footprint of Amazon orders. I helped create the relevant calls to external APIs and write its Flask backend. Although the API integration is incomplete, my team plans to finish it in the future. The skills I learned also let me get started on [EasyTrack](https://github.com/sai-nayunipati/EasyTrack). The project is being developed, but it is meant to help Boston University students track fully-booked courses to be notified when a seat opens up. Currently, it features a web scraper which inserts section data from Boston University's course catalog into a MySQL database. Flask was also a gentle introduction to Django, which is the framework I used to create the backend for [Adi](https://github.com/neezacoto/Adi-ai-ads), the overall first-place winner at BostonHacks2022. (Everything under back-end/adi/adi is my contribution. I also wrote the Django-related code in back-end/adi/backend and contributed heavily to the other scripts.)

## Getting Started

### Dependencies

None.

## Version History

* 1.0
    * Initial Release

## License

N/A

## Acknowledgments
None.
