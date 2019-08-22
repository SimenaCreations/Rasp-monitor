if [ -e /tmp/nmap_output.txt ]; then
  echo ""
  echo "Reading IP from old file:"
  echo ""
  ip="$(grep 'Raspberry Pi' -B3 /tmp/nmap_output.txt| grep 'Nmap scan'|cut -d' ' -f5)"
else
  touch /tmp/nmap_output.txt
  chmod 755 /tmp/nmap_output.txt
  echo ""
  echo "Getting fresh nmap output:"
  echo ""
  sudo nmap -sP $(ifconfig | grep 'broadcast 192.168.0.255'|cut -d' ' -f2)/24 >> /tmp/nmap_output.txt
  ip="$(grep 'Raspberry Pi' -B3 /tmp/nmap_output.txt| grep 'Nmap scan'|cut -d' ' -f5)"
fi
user='pi'

echo ""
echo " ###################################"
echo " IP for Raspberry Pi: " ${ip}
echo " Logging into the host now"
echo " ###################################"
echo ""

ssh $user@$ip -q -o "StrictHostKeyChecking no"
