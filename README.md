# csv_compare

CSV compare provides a way to compare the full contents of a Digital commons inventory csv with the contents of a 
database (al_db or alf_db).  Best used for locating MQPS, IQPS and ETDs that have fallen through the cracks of monthly uploads


### Dependencies
CSV Dictreader
json
mysql connector

### Instructions
1. Download a full metadata inventory from digital commons. For best output, limit it to one series
2.  enter database information 
3.  specify the csv, the id field and the link to the record in the csv in in the compare_list function
4.  Output will be a list.  Currently, it will require being run through mysqlf to get full text


### Future development
1.  refactor main part of script
2.  Add ability to work with more types of file formats (rdf in the future?)
3.  produce better output for using in the mysqlf file, or allow the functions to be called by a script that will create files
