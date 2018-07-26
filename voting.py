import datetime
now = datetime.datetime.now()
i=1
pti=0
pmln=0
ji=0
mqm=0
ppp=0
psp=0
tl=0
idp=0
aml=0
anp=0
print("Pakistan Genral Election,2018\n  ")
while i<=50:
        print("Voter no",i)
        name=str(input("Enter Your name:"))
        ID=input("enter ID no:")
        while len(ID)!=13:
            print("Invalid ID no")
            ID=input("Enter ID no again:")
        print("Parties names are:\nPTI for Pakistan Tahreek-e-Insaf\nPMLN for Pakistan Muslim League Nawaz\nPPP for Pakistan Peoples Party\nMQM for Mutheda Qoumi Moment\nPSP for Pak Sarzmeen Party\nTL for Tahreeky-labaik\nJI for Jamat-e-Islami\nIDP for Independent\nAML for Awami Muslim League\nANP for Awami National Party")
        print(end="\n")
        vote=str(input("To which Party do you want to vote:"))
        if vote.upper()=="PTI":
                print(name,"(",ID,")","you voted for Pakistan Tahreek-e-Insaf at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                pti+=1
        elif vote.upper()=="PMLN":
                print(name,"(",ID,")","you voted for Pakistan Muslim League Nawaz at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                pmln+=1
        elif vote.upper()=="PPP":
                print(name,"(",ID,")","you voted for Pakistan Peoples Party at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                ppp+=1
        elif vote.upper()=="JI":
                print(name,"(",ID,")","you voted for Jamat-e-Islami at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                ji+=1
        elif vote.upper()=="MQM":
                print(name,"(",ID,")","you voted for MQM for Mutheda Qoumi Moment at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                mqm+=1
        elif vote.upper()=="PSP":
                print(name,"(",ID,")","you voted for Pak Sarzmeen Party at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                psp+=1
        elif vote.upper()=="TL":
                print(name,"(",ID,")","you voted for Tahreeky-labaik at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                tl+=1
        elif vote.upper()=="IDP":
                print(name,"(",ID,")","you voted for Independent Person at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                idp+=1
        elif vote.upper()=="AML":
                print(name,"(",ID,")","you voted for Awami Muslim League at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                aml+=1
        elif vote.upper()=="ANP":
                print(name,"(",ID,")","you voted for Awami National Party at",now.strftime("%H:%S:%M"))
                print("Thank you so much for your time\nBest of luck to your Party")
                print("")
                anp+=1

        i+=1
print("Results")
print("")
print("PTI = ",pti)
print("PMLN = ",pmln)
print("PPP = ",ppp)
print("PSP = ",psp)
print("JI = ",ji)
print("MQM = ",mqm)
print("TL = ",tl)
print("IDP = ",idp)
print("AML = ",aml)
print("ANP = ",anp)

