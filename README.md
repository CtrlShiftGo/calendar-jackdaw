# calendar-parser
## Usage

`./calendar-parser.py <start-date> [end-date]`

`<start-date>` and `[end-date]` should be in ISO8601 format:
  * 2017-01-01
  * 1969-12-31

Output file will be named `<start-date>.csv` and will contain statistics about calendar events which are in the range `<start-date>` to `[end-date]`. If a file has already been created with this start date, the program will append any additional dates to this document.
