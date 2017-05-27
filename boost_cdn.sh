#!/bin/bash

# Alternative CDN site 
cat > mapping <<EOF
fonts.googleapis.com         fonts.lug.ustc.edu.cn
ajax.googleapis.com          ajax.lug.ustc.edu.cn
themes.googleusercontent.com google-themes.lug.ustc.edu.cn
fonts.gstatic.com            fonts-gstatic.lug.ustc.edu.cn
EOF

while read line 
do
    regexp=${line%% *}
    replacement=${line##* }
    find pelican-theme/ -type f -print | xargs -i sed -i "s/$regexp/$replacement/" {}
done < mapping

rm mapping
