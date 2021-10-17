#import
import requests

#function for scanning subdomain
def scanner(domainName,subDomain):
    print("---- Starting The Enumerator ----")
    print("---- URL after scanning subdomains ----")

    #looping for getting URL's
    for subdomain in subDomain:

        #making URL by putting subdomain one by one 
        url = f"https://{subdomain}.{domainName}"

        #using try catch block to avoid crash of the program
        try:
            #sending get request to url
            requests.get(url)

            #if after putting subdomain one by one url is valid then printing the url
            print(f"[+] {url}")

        except requests.ConnectionError:
            pass

#main function
if __name__ == '__main__':

    #inputting the domain name 
    domain_name = input("enter the Domain Name")

    #opening the subdomain text file 
    with open("subdomain_list","r") as file:

        #reading the file 
        name = file.read()

        #using splitlines() function storing the list of splitted strings
        sub_name = name.splitlines()

    #calling the function for scannning the subdomains and getting the url 
    scanner(domain_name,sub_name)

