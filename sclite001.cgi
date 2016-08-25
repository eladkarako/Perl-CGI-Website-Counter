#!/usr/local/bin/perl

##################################################################################
# File = sclite version 1.                                                       #
# Author = David Stanley (htmlite).                                              #
# Created = May 2002.                                                            #
# Cost = Free.                                                                   #
##################################################################################

#parses the query string and creates the scalar variables
#stores pass values in the hash FORM
@values = split(/&/,$ENV{'QUERY_STRING'});
              foreach $i (@values) {
                  ($varname, $mydata) = split(/=/,$i);
                  $FORM{$varname} = $mydata;
              }

# Sets filename for use later.
$filename = $FORM{'filename'};

# Set the counter file.
$count_file = "$filename" . ".dat";

# Open the counter file and get current number.
open (COUNT, $count_file);
$current_count=<COUNT>;
close (COUNT);

# Increase the counter number by one.
$current_count++;

# Open the counter file for replacing current number new one.
open (COUNT, ">$count_file");
print COUNT $current_count;
close (COUNT);

#################################################################################
# If you are using this counter for a normal page link counter, then change the #
# zip extension below to the correct extension type.                            #
#################################################################################

$filename2 = "$filename" . ".zip";

#################################################################################
# Enter your correct URL path to the download folder. Include any subfolders    #
# as required. Example : http://www.mysite.com/downloads/                       #
# Keep the Locatoin: at the start.                                              #
# Keep the $filename2\n\n at the end.                                           #
#################################################################################

print "Location: http://www.yourdomain.com/" . "$filename2\n\n";