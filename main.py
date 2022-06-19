import find_best
import find_natural
import ssl
from OSMPythonTools.api import Api


def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    api = Api()
    query = 'relation/' + str(3600534847)
    print(query)
    name = api.query(query)
    print(name)

    #    find_natural.search('Munich', ['way', 'relation'], '"natural"="water"')
    # find_best.search()


if __name__ == "__main__":
    main()
