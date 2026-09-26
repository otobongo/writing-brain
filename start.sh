#!/bin/sh
# Opens the Writer Science study page (video + read-along transcript + concept index)
cd "$(dirname "$0")"
(python3 -m http.server 8765 --directory site >/dev/null 2>&1 &)
sleep 1; open http://localhost:8765/index.html
