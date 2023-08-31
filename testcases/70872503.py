import unittest
import requests
import lxml
from bs4 import BeautifulSoup
import csv

def myFunc():

    names = []

    url = 'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='lxml')
    headers = soup.find_all('th')
    headers_refined = []
    headers_refined.append(headers[0])
    headers_refined.append(headers[1])
    headers_refined.append(headers[6])
    ips = soup.find_all('td')


    ips = ips[::8]
    ports = soup.find_all('td')
    ports = ports[1::8]

    element_index = 0
    for i in ips:
        ips[element_index] = str(ips[element_index])
        element_index += 1

    element_index = 0
    for i in headers_refined:
        headers_refined[element_index] = str(headers_refined[element_index])
        element_index += 1

    element_index = 0
    for i in ports:
        ports[element_index] = str(ports[element_index])
        element_index += 1

    ips = ' '.join(ips).replace('&lt;td&gt;', '').split()
    ips = ' '.join(ips).replace('&lt;/td&gt;', '').split()
    ips = ips[:-43:]
    headers_refined = ' '.join(headers_refined).replace('&lt;th&gt;', '').split()
    headers_refined = ' '.join(headers_refined).replace('&lt;/th&gt;', '').split()
    headers_refined = ' '.join(headers_refined).replace('&lt;th class=&quot;hx&quot;&gt;', '').split()
    ports = ' '.join(ports).replace('&lt;td&gt;', '').split()
    ports = ' '.join(ports).replace('&lt;/td&gt;', '').split()
    while len(ports) > len(ips):
        ports=ports[:-1:]
    prev_len_ips=len(ips)
    index=0
    for i in range(prev_len_ips):
        ips.insert(i+1,ports[i])


    # print(headers_refined)
    # print(ips)
    # print(ports)
    print(prev_len_ips)
    print(len(ports))



    ips = [*zip(ips[::2])]
    with open('ips.csv', '+w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(ips)


class TestMyFunc(unittest.TestCase):

    def test_ip_length(self):
        result = myFunc()
        self.assertEqual(len(result), 5)  # assuming there are 5 IPs obtained from the website

    def test_csv_written(self):
        myFunc()
        with open('ips.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = [row for row in csv_reader]
        self.assertEqual(len(rows), 5)  # assuming there are 5 IPs obtained from the website


if __name__ == '__main__':
    unittest.main()