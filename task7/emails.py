import csv
import argparse
import pprint

def init_parser():
    parser = argparse.ArgumentParser(description='Distributes emails to groups.')
    parser.add_argument('csv_file', type=file, help='File containing emails.')
    return parser.parse_args()

def parse_email_domain(values):
    email, username = values
    domain = email.split("@")[1]
    return domain

def get_domain_flag(domain, mail_domains, power_of_two):
    if domain in mail_domains:
        domain_flag = mail_domains[domain]
    else:
        domain_flag = pow(2, power_of_two)
        power_of_two += 1
    return domain_flag, power_of_two

def main():
    args = init_parser()
    power_of_two = 0
    mail_domains = {}
    emails_entry = [0]
    sorted_emails = [[]]
    reader = csv.reader(args.csv_file)
    for i, row in enumerate(reader):
        if i != 0:
            domain = parse_email_domain(row)
            domain_flag, power_of_two = get_domain_flag(domain, mail_domains, power_of_two)
            mail_domains[domain] = domain_flag
            added = False
            for i, entry in enumerate(emails_entry):
                if entry & domain_flag != domain_flag:
                    sorted_emails[i].append((row[0], row[1]))
                    emails_entry[i] = emails_entry[i] | domain_flag
                    added = True
                    break
            if not added:
                emails_entry.append(domain_flag)
                sorted_emails.append([(row[0], row[1])])
    result = [tuple(group) for group in sorted_emails]
    pp = pprint.PrettyPrinter()
    pp.pprint(result)


if __name__ == '__main__':
    main()
