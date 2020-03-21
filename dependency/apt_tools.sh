# sudo chmod 707 pdf_id/pdfid.py
sudo apt install whois
sudo apt install exiftool
sudo apt update
echo " "
echo " ---------------------------------------------------"
echo " "
echo " "
echo -e "\e[33m [*] Need API Key To InterAct With VirusTotal [*]"
echo " "
echo " "
echo -e "\e[92m create an account:\e[34m https://www.virustotal.com/gui/join-us"
echo " "
echo -e "\e[92m Get API KEY:\e[34m https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key"
echo " "
echo -e "\e[39m "
./dependency/vt init
