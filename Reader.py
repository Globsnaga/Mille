from tkinter import filedialog


class FileHandler():

    def Reader(self):
        return self

    def readFile(self,file):

        list = []
        substitutiontable = self.readTable()
        i = -1
        j = 0

        with open (file, 'r') as inputfile:
            for line in inputfile:
                line.replace('\r\n','')
                seperated = line.split(',')
                if seperated [0] == '0' and seperated[1] == '0':
                    i = i + 1
                    date = seperated[7].split(';')[0] #Hier ändern wenn datumsfeld wieder anders ist.
                    #list.append([seperated[6]])

                elif seperated[2] in substitutiontable.keys() and '6' == substitutiontable[seperated[2]][3]:
                        temp2 = seperated[2]
                        gegenkonto = str(substitutiontable[seperated[2]][4])
                        textfield = str(substitutiontable[seperated[2]][1])
                        seperated[2] = substitutiontable[seperated[2]][0]
                        seperated[3] = seperated[3].split('/')[1].replace('.',',')
                        temp = seperated[2]
                        seperated[2] = seperated[1]
                        seperated[1] = temp
                        list.append(date+';'+';'.join(seperated).strip('\n')+';'+textfield+';' + gegenkonto)
                        print(temp2)
                        if temp2 == '952':
                            seperated[1] = substitutiontable['4711'][0]
                            list.append(date+';'+';'.join(seperated).strip('\n')+';'+'Trinkgeld Auszahlung Unbar'+';'+substitutiontable['4711'][4])

                elif seperated[1] in substitutiontable.keys() and seperated[0] == substitutiontable[seperated[1]][3] and seperated[2] != '-1001':
                        textfield = str(substitutiontable[seperated[1]][1])
                        gegenkonto = str(substitutiontable[seperated[1]][4])
                        if(substitutiontable[seperated[1]][2] == '-1'):
                            seperated[3] = '-'+seperated[3].split('/')[1].replace('.', ',')
                        else:
                            seperated[3] = seperated[3].split('/')[1].replace('.', ',')
                        seperated[1] = substitutiontable[seperated[1]][0]

                        list.append(date+';'+';'.join(seperated).strip('\n')+';'+textfield+';' + gegenkonto)
        return list

    def writeFile(self,file,list):


        with open(file,'w') as outfile:
            for val in list:
                outfile.write(str(val));
                outfile.write('\n')


    def remover(self,val,table):

        if val[2] not in table.keys() and val[2] != '.':
            return False
        return True

    def readTable(self):

        substitution = {}
        with open(filedialog.askopenfilename(),'rU') as file:
            for line in file:
                seperatedline = line[0:-1].split(';')
                substitution[seperatedline[1]] = [seperatedline[2],seperatedline[3],seperatedline[4],seperatedline[0],seperatedline[5]]
        return substitution