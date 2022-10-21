# Program to identify some acronyms

# Create a dictionary of acronyms and their meanings
# The dictionary have the most common acronyms
acronymsList = {'FIS': "Facultad de Ingeniería de Sistemas",
                'AEIS': "Asociación de Estudiantes de Ingeniería de Sistemas",
                'NASA': "National Aeronautics and Space Administration",
                'UNESCO': "United Nations Educational, Scientific and Cultural Organization",
                'UNICEF': "United Nations Children's Fund",
                'AI': "Artificial Intelligence",
                'UFO': "Unidentified Flying Object",
                'IaaS': "Infrastructure as a Service",
                'PaaS': "Platform as a Service",
                'SaaS': "Software as a Service",
                'IoT': "Internet of Things",
                'API': "Application Programming Interface",
                'OTPaaS': "One Time Password as a Service",
                'MFA': "Multi-Factor Authentication",
                'LCD': "Liquid Crystal Display",
                'LED': "Light Emitting Diode",
                'RAM': "Random Access Memory",
                'ROM': "Read Only Memory",
                'CPU': "Central Processing Unit",
                'GPU': "Graphics Processing Unit",
                'SSD': "Solid State Drive",
                'HDD': "Hard Disk Drive",
                'USB': "Universal Serial Bus",
                'PCI': "Peripheral Component Interconnect",}

def searchAcronym(acronym):
    # Search the acronym in the dictionary
    if acronym in acronymsList:
        return acronymsList[acronym]
    else:
        pass

def main():
    # Ask the user for an acronym
    phrase = input("Enter a phrase: ")
    # Split the phrase in words
    words = phrase.split()
    # Search the acronym in the dictionary
    for word in words:
        meaning = searchAcronym(word)
        if meaning != None:
            print(meaning)

main()