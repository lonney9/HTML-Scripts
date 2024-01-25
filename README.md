# HTML Scripts

These scripts were used to tidy and make the Cebik pages HTML compliant with styling set by one CSS file.

The finished result is hosted at [www.antenna2.net/cebik](https://www.antenna2.net/cebik/).

The pages were sourced from [www.on5au.be/Cebik%20documents.html](http://www.on5au.be/Cebik%20documents.html). The "Cebik Style" version was used as the starting point, in addition to the scripts a number of manual edits were made where HTML formatting issues tripped up [HTML Tidy](https://www.html-tidy.org/), it doesn't magically handle every possible syntax situation correctly.

In addition to cleaning up the HTML, a pair of scripts were used to generate a linked topics footer and a topics index page based on meta keywords and the page title names.

The scripts were written by ChatGPT. I know a little shell scripting, but nothing regarding Python other than what the script is doing at a high level, and can make simple changes.

A quick summary of what they do:

- Remove font tags, simplify the body tag, remove bold tags from around pre tags, remove doctype
- HTML tidy is run with out CSS option, output ascii (converts non-basic characters to HTML entities)
- Add the link to the style sheet
- De-duplicate header and navigation images
- Add the linked topics footer and topics index page
- Generate sitemap.xml
- Misc scripts to strip out custom tags, search and replace of meta keywords, heading h2 > h1 tag (SEO)

The scripts also have some comments added.
