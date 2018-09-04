ipa={"Interface":["FastEthernet0/0","FastEthernet1/0","Serial2/0","Serial3/0","FastEthernet4/0","FastEthernet5/0"],"IP-Address":["192.168.1.242","unassigned","192.168.1.250","192.168.1.233","unassigned","unassigned"],"OK":["YES","YES","YES","YES","YES","YES"],"Method Status":["manual up","unset","manual up","manual up","unset","unset"],"Protocol":["up","down","up","up","down","down"]}
lst1=ipa["Interface"]
lst2=ipa["Method Status"]
print "Displaying Interface and Method Status for all the interfaces:"
for i in range(len(lst1)):
    print lst1[i],",",lst2[i]
