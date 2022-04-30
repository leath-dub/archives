#!/bin/sh

# when testing, comment/uncomment the following "exec" line
# comment - output goes to screen
# uncomment - output goes to file

clickable()
{
    while read line
    do
        file=`echo "$line" | cut -f1 -d':'`
        hit=`echo "$line" | cut -f2 -d':'`
        echo "<a href='$file'>$file</a>: $hit <br>"
    done
}

exec > $HOME/gweb.output.html           


# cd /users/tutors/mhumphrysdculab/share/shakespeare
# cd $HOME/.dev/my_website/
cd /shared/humphrys/shakespeare
echo '<pre>'
grep -i "$1"  */*html | sed -e 's|<|\&lt;|g' | sed -e 's|>|\&gt;|g' | clickable
echo '</pre>'
