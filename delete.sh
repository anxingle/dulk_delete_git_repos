#!/bin/bash
# replace XXXXXX with your own token code !
cat bulk_delete_repos.txt | while read line
do 
    echo "${line}"
    echo $line
    curl  -XDELETE -H 'Authorization: token XXXXXXXXXXXXXXXXXXX' "https://api.github.com/repos/anxingle/$line"
done
