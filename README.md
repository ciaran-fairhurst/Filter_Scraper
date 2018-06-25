# Filter_Scraper
Get all the telescope filters you could ever want from the Spanish virtual observatory website.

Simply run the script and the filters will be output to "./filters/\<telescope\>/\<instrument\>/\<filter\>.txt"
  
Each ".txt" file is in two columns, the first is the wavelength in Angstroms, the second is the fractional throughput at that wavelength (i.e. a second column value of 0 means it is completely opaque, and a value of 1 means it is perfectly transparent).

using python the following will work to efficently load a filter:

lam,T = numpy.loadtxt( './filters/telescope/instrument/filter.txt' , unpack=True )


Feel free to email me at c.fairhurst@sussex.ac.uk if you have any comments/questions or wish to use it for something.
