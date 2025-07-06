machine_id=$(cat /etc/machine-id)
echo -n $machine_id | cksum | awk '{print $1}'