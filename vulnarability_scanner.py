#!/usr/bin/env python
import scanner
target_url = "http://127.0.0.1/dvwa/vulnerabilities/xss_s"
links_to_ignore = ["http://127.0.0.1/dvwa/logout.php"]
data_dict = {"username" : "admin" , "password" : "password" , "Login" : "submit"}
vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://127.0.0.1/dvwa/login.php" , data=data_dict)
print(target_url)
vuln_scanner.crawl()
vuln_scanner.run_scanner()


