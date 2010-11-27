=================================================
API Documentation
=================================================

Overview
-------------------------------------------------

Guides
-------------------------------------------------

**methods**

  * *GET*
  * *PUT*
  * *POST*
  * *DELETE*

Users
-------------------------------------------------

**/api/v1/users/**

  * *GET* - 
  * *PUT* - not used
  * *POST*
  * *DELETE* - not used

Markup
-------------------------------------------------

The following formats are currently supported:

  * markdown
  * restructured text
  * texttile

**/api/v1/markup/{format}/**

  * *GET* - not used
  * *PUT* - not used
  * *POST* - returns the given text block formatted to the requested
    format. If no format is specified, it defaults to markdown.
  * *DELETE* - not used
