import urllib2
archivo = urllib2.urlopen('https://github.com/nyphilarchive/PerformanceHistory/blob/master/Programs/json/2011-12_TO_NOW.json')
descarga = archivo.read()