# WebScrapping_for_jobs

## Overview

Looking for a job can be quite overwhelming for a great part of us. Thus, this script was written to help a client to visualize in a csv file vacancies available in a specific agency's website. Later, this script was adapted and used as a part of a bot for job application.

This script and some comments are in the client's native language.

## 1. Requirements

To run this project you need the following packages:

```
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv, datetime
```

## 2. Result

The csv file generated at the end of the script:

```
def save(self):
        # csv
        self.filename = 'vagas.csv'
        self.f = open (self.filename, "a")

        headers = "vaga,empresa,area,data,cidade,estado,fonte,link\n"  
        self.f.write (headers)
        self.jobs ()
```

The "headers" command are followed by the title of each column in Portuguese.


## 3. Further Explanation

https://www.youtube.com/watch?v=XQgXKtPSzUI
