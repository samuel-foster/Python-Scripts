import gzip
import re

def remove_ip_addresses(input_file, output_file):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_replacement = '[IP ADDRESS REMOVED]'

    with gzip.open(input_file, 'rt', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                line = re.sub(ip_pattern, ip_replacement, line)
                f_out.write(line)

if __name__ == "__main__":
    input_log_file = "your_input_log_file.log.gz"
    output_log_file = "output_log_file.log"

    remove_ip_addresses(input_log_file, output_log_file)
