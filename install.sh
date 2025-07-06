#!/bin/bash
echo "Removing old version"
rm -rd $HOME/.local/bin/sfid_
rm -rf $HOME/.local/bin/sfid

cp -r ../sfid $HOME/.local/bin/sfid_
chmod u+x $HOME/.local/bin/sfid_/mid.sh
mv $HOME/.local/bin/sfid_/sfid $HOME/.local/bin/sfid
chmod u+x $HOME/.local/bin/sfid.sh
echo "Downloading sonyflake..."
python3 -m pip install --no-cache --target $HOME/.local/bin/sfid_/ sonyflake-py 