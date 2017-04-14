import sys
#import scrapy
import urllib2
import time
#import requests
#from __builtin__ import type
#from bs4 import BeautifulSoup
#import mechanize
#import ssl

from flask.globals import request
from twisted.pair import raw
from twisted.protocols.sip import dashCapitalize


def dashed():
    print "---------------------------------------------------------"

med_type = ""
def get_input():
    dashed()
    print "\t\tDIGITAL MEDICINE REPOSITORY"
    dashed()
    print "\nWhat would you like to do?\n"
    print "1. What is inside my drug?\n2. What does my drug do?\n3. What are the side effects?\n\nAnything else to exit.\n"
    dashed()
    choice = input ("Enter choice: ")
    dashed()
    return choice



def generate_url(med_name):
    med_name.replace(' ', '-')
    return "http://www.tabletwise.com/" + med_name + "-" + med_type


if __name__ == '__main__':
    choice = get_input()
    while choice < 4:

        if choice == 1:
            med_name = raw_input("Enter the name of the drug: ")
            med_type = raw_input("\nEnter drug type:\n[tablet, capsule or syrup]\n")
            dashed()
            med_name = med_name.lower()
            url = generate_url(med_name)
            # print url
            handle = urllib2.urlopen(url)
            source = handle.read()

            strr = ""
            skip = ""
            if med_name in source:
                here = source.find("Composition and Active Ingredients")
                i = here
                index = here - 1
                # print index
                # sys.exit()
                z = here + 400
                if here:
                    # for index in range(here, here+300):
                    while index < z:
                        index += 1
                        # print index

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        strr += source[index]
                print
                medlen = med_name.__len__()
                # print medlen
                print med_name.upper() + " contains: " + strr[103 + medlen:strr.find("Please")-1]
                print
                dashed()

            else:
                print "Invalid medicine name"

        # -----------------------------------------------------------------------------------------------------------------
        elif choice == 2:
            med_name = raw_input("Enter the name of the drug: ")
            med_type = raw_input("\nEnter drug type:\n[tablet, capsule or syrup]\n")

            dashed()
            med_name = med_name.lower()
            url = generate_url(med_name)
            # print url
            handle = urllib2.urlopen(url)
            source = handle.read()

            strr = ""
            skip = ""
            if med_name in source:
                here = source.find("used for the ")
                i = here
                index = here - 1
                # print index
                # sys.exit()
                z = here + 400
                if here:
                    # for index in range(here, here+300):
                    while index < z:
                        index += 1
                        # print index

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        strr += source[index]
                print
                medlen = med_name.__len__()
                # print medlen
                strr = strr[:strr.find("References")]
                print med_name.upper() + " is used for the treatment, control, prevention and \nimprovement of \
the following conditions and symptoms:\n"
                symptoms = (strr[103 + medlen:strr.find("Please") - 1]).split("  ")
                for symptom in symptoms[1:]:
                    symptom = symptom.lstrip()
                    join = symptom.find("Join")
                    if join:
                        symptom = symptom[:join - 1]
                    print "-> " + symptom
                print
                dashed()

            else:
                print "Invalid medicine name"

        # -----------------------------------------------------------------------------------------------------------------
        elif choice == 3:
            med_name = raw_input("Enter the name of the drug: ")
            med_type = raw_input("\nEnter drug type:\n[tablet, capsule or syrup]\n")

            dashed()
            med_name = med_name.lower()
            url = generate_url(med_name)
            # print url
            handle = urllib2.urlopen(url)
            source = handle.read()

            strr = ""
            skip = ""
            if med_name in source:
                here = source.find("go away")
                i = here
                index = here - 1
                # print index
                # sys.exit()
                z = here + 410
                if here:
                    # for index in range(here, here+300):
                    while index < z:
                        index += 1
                        # print index

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        if source[index] == "<":
                            while source[index] != ">":
                                skip += source[index]
                                index += 1

                        if source[index] == ">":
                            index += 1

                        strr += source[index]
                print
                medlen = med_name.__len__()
                # print medlen
                strr = strr[:strr.find("If you notice")]
                print "Possible side-effects of using " + med_name.upper() + " may include:\n"
                sidefx = (strr[10:]).split("  ")# + medlen:strr.find("Please") - 1]).split("  ")
                for fct in sidefx:
                    fct = fct.strip()
                    if fct == "":
                        continue
                    print "-> " + fct
                print
                dashed()

            else:
                print "Invalid medicine name!"

        dashed()
        dashed()
        choice = input("Enter choice: ")
        dashed()
    print "\t\t\tQuitting"
    dashed()
    time.sleep(2)