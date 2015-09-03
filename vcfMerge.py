import time
f = open("topluYedek.vcf", "w")
phats = ["phat/contacts1.vcf","phat/contacts2.vcf","phat/contacts3.vcf","phat/contacts4.vcf",]
first = ''
version = ''
n = ''
fn = ''
tel = ''
number = []
tel2 = ''
a = 0
for phat in phats:
    countLine = 0
    with open(phat) as fp:
        for line in fp:

            if line.count('BEGIN'):
                first = line
            elif line.count('VERSIO'):
                version = line
            elif  (line.count('N:') == 1): 
                n = line
            elif  line.count('FN:') == 1:
                fn = line
            elif line.count('TEL;'):
                tel = line
                tel2 = line.split(':')[1]
                
                if number.count(tel2) == 0 :
                    f.write(first+'')
                    f.write(version+'')
                    f.write(n+'')
                    f.write(fn+'')
                    f.write(tel+'')
                    f.write('END:VCARD\n')
                    number.append(tel2)
                    first = ''
                    version = ''
                    n = ''
                    fn = ''
                    tel = ''
                    countLine = countLine + 1
          

    print countLine
    print 'bitti'
f.close()
