from datetime import datetime

begin_date = datetime.now()
end_date = datetime(2021, 10, 28, 19, 00, 00)
redirect = "127.0.0.1"

hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
website_blocked = ["facebook.com", "www.facebook.com", "instagram.com", "www.instagram.com", "twitter.com",
                   "www.twitter.com"]
def site_blocked():
    if begin_date < end_date:
        print("Block sites")
        with open(hosts_path, "r+") as hosts_file:
            hosts_content = hosts_file.read()
            for site in website_blocked:
                if site not in hosts_content:
                    hosts_file.write(redirect+ " " + site + "\n")
    else:
        print("unblock sites")
        with open(hosts_path, "r+") as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)
            for line in lines:
                if not any(site in line for site in website_blocked):
                    hosts_file.write(line)
            hosts_file.truncate()

site_blocked()





