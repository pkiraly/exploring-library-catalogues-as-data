# Exploring library catalogues as data - a lesson for ProgrammingHistorian

This repository is to support writing activities of a lesson provisionally 
titled as "Exploring library catalogues as data". These activities belong to
ProgramminHistorian's [ENABLAR programme](https://programminghistorian.org/posts/enablar-call-for-participants)
- ENABling Library and Archive participation in digital Research co-learning communities.

The repository will contain not only the text of the lesson and supplementary 
materials (images, tables etc.) but some data and scripts as well.

## Planned topics of the tutorial

Methods/tools:
* MarcEdit (Argula)
* describing some important MARC data elements (Péter)
* programming MARC records with Python [PyMarc] (and showing alternatives) (Péter)
* small/local LLMs? (Michele)
* Gephi for visualisation (Argula)

Data analyses:
* extraction
  * place and personal name extraction and normalisation (with roles)  (Péter)
    * enriching subject indexing/ information (Argula) – adding additional information about named entities in records (Argula) – external data to match with smaller datasets: FAST, VIAF, etc. (Argula)
    * create a map (Péter)
  * date extraction and normalisation (Péter)
    * create a timeline (Péter)
    * Consider using bibliographic data to visualise the history of early book editions from the time of their first printing (geomapping and timelines). (Arnoud)
  * subjects
    * analysing subject coverage in a collection (Argula)
* how to work across two datasets computationally (Argula)

Objectives, principles, general questions:
* Assist catalogers/metadata librarians in their day-to-day work and specialized projects (Doreen)
* How to help book historians in answering their questions? (Péter)
* Copy cataloging versus original cataloging depending on the topic of the project (Halie)
* Also being aware of local cataloging practices that may or may not impact the analysis or computational methods (Doreen)

Datasets:
* a smaller library catalogue (e.g. Estonian nat. bibl.), or a part of a larger one (Belgian, German, Czech etc.) (Péter)
* https://github.com/pkiraly/qa-catalogue#datasources
* https://about.muse.jhu.edu/muse/open-access-marc (Doreen)
* Could you pull based on a specific category in MARC or subject headings etc and then create around that. (Halie)

Open questions:
* Question for Peter (and anyone else who is interested in contributing): Is the lesson goal to show researchers how to use marc records to answer their research questions? (I.e. need to explain how to navigate a set of marc records?) Starting from sample research questions then find datasets and methods to work with them? (I am reminded of this link Peter showed me: https://bibliodata.substack.com/p/an-outline-of-an-imagined-training) Or is it to select a small set of marc records and build a model or something that can be used for i.e. lesson 2 or 6 or linked sticky notes? (Doreen)
* The focus is on training and fine-tuning a small LLM to make it an expert in dealing with bibliographic data. (Arnoud)

