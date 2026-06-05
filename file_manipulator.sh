#!/bin/bash
source ./exe.sh
source ./open_vim.sh

read -p "Enter the file name to check: " file
if [[ -f $file ]]; then
	echo "file is exist"
	sleep 2
	cat $file
else 
	echo "file is not exist"
	sleep 2
	echo "#!/bin/bash"> $file
	echo "file created successfully"
	echo "file is opening..."
	sleep 3
	cat $file
fi

echo ""
if [[ ! -x $file ]];  then
	read -p "Would you like to make it executable [Y/n]: " choice
	if [[ $choice == "y" || $choice == "Y" ]]; then
	echo "$file becoming executable .."
	exe $file
	else
	echo "Cancel to executable"
	fi
fi
echo ""
read -p "Would you like to edit this file [Y/n]: " choose
if [[ $choose == "y" || $choose == "Y" ]]; then
	open $file

else 
	sleep 1
	echo "script complete!"
fi
