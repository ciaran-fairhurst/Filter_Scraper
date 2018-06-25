import requests
import urllib
import os
import sys

url_to_scrape =  'http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse'
                # http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse&gname=Subaru'
                # http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse&gname=Subaru&gname2=MOIRCS
# find a list of all the instruments form the main page
page = requests.get(url_to_scrape).text.split('gname=')[1:]

instruments = []
list_of_filters = []

for line in page:
    instruments.append( line.split('"')[0] )


print( ' *** LIST OF INSTRUMENTS DONE *** ' )



for ins in instruments:#[-2:]:

    url_to_scrape_2 = url_to_scrape + '&gname=' + ins
    page = requests.get(url_to_scrape_2).text

    cameras = []
    for i in page.split('index.php?mode=browse&gname='+ins+'&gname2=')[1:]:
        cameras.append(i.split('">')[0] )

    if cameras != []:
        for cam in cameras:
            url_to_scrape_3 = url_to_scrape_2 + '&gname2=' + cam

            page = requests.get(url_to_scrape_3).text

            filters = [ page.split('href="index.php?id='+ins)[1:][i].split('&&')[0] for i in range(len(page.split('href="index.php?id='+ins)[1:]  )) ]

            for filt in filters:
                list_of_filters.append( ins  + filt )
                print(ins  + filt)


    else:
        page = requests.get(url_to_scrape_2).text

        filters = [ page.split('href="index.php?id='+ins)[1:][i].split('&&')[0] for i in range(len(page.split('href="index.php?id='+ins )[1:])) ]


        for filt in filters:
            list_of_filters.append( ins  + filt )

            print(ins  + filt)



print(' *** LIST OF FILTERS DONE ***')




for i,filt in enumerate(list_of_filters):

    path = './filters/' + '/'.join( [filt.split('.')[0].split('/')[0].upper(),filt.split('.')[0].split('/')[1].lower()] )
    filename = filt.split('.')[1].lower()
    if not os.path.exists( path ):
        os.makedirs(   path   )

    if not os.path.exists( path+'/'+filename+".txt" ):
        urllib.request.urlretrieve ("http://svo2.cab.inta-csic.es/svo/theory/fps/getdata.php?format=ascii&id="+filt, path+'/'+filename+".txt")

    print('WRITING FILTER FILES: ' + str(round(float(i)*100/float(len(list_of_filters)), 2)) + '%')
    sys.stdout.write("\033[F")


print(' *** ALL DONE! ***                                       ')


#http://svo2.cab.inta-csic.es/svo/theory/fps/getdata.php?format=ascii&id=2MASS/2MASS.H
#find line with 'gname' in
#find every instance of gname, and add the bit between = and " >> the instrument name
