import requests
import json


def nxapi_show_version():
    url =  "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = "admin"
    switchpassword = "Admin_1234!"

    http_headers = {'content-type': 'application/json-rpc'}
    payload = [{"jsonrpc": "2.0",
                "method": "cli",
                "params": {"cmd": "show version",
                           "version": 1}, "id": 1}]
    response = requests.post(url, data=json.dumps(payload), auth=(switchuser, switchpassword), headers=http_headers, verify=False)
    
    version = response.json()['result']['body']['kickstart_ver_str']
    return version


if __name__ == '__main__':
    result = nxapi_show_version()
    print(result)