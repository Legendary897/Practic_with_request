import requests


#if __name__ == "__main__":
    #while True:
    #    result = input()
    #    print(requests.get('http://localhost:2002/add_info/{0}'.format(result)))
list_p = ["0002 C1 01:13:02.877 00[CR]", "0003 C1 01:13:02.877 01[CR]", "0004 C1 01:13:02.877 00[CR]",
          "0009 C1 01:13:02.877 01[CR]", "0001 C1 01:13:02.877 00[CR]", "0007 C1 01:13:02.877 01[CR]"]
for i in list_p:
    requests.get('http://localhost:2002/add_info/{0}'.format(i))
