# snwldaoinfo
The purpose of this script is to quickly retrieve the DAO information from a diagnostic report pulled from a SonicWall firewall and output it in a way one could pipe the output to a CSV file.

This tool will take all of the SonicWall TSRs (.wri files) that are in a folder and will output CSV-formatted information about all of the FQDN Dynamic Address Objects, such as the name of the object, configured FQDN, and resolved addresses.

It looks for object headers, then looks for the RETRY COUNT statistic (which is only on FQDN objects), and if it's there based on it's index in the list object, will create variables for the line indexes around it. The end result is comma-separated printing the object's name, configured FQDN, and resolved addresses/TTL information to the console. With a little editing you can add the other lines to include the other info such as the object's UUID, references, etc. if you need them. Or you could find other patterns and modify to extract what you want.

