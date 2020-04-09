import sys ,csv
my_hist=[]
with open(sys.argv[1]+"/input_hw_2.csv","r") as dosya:
    for i in dosya:
        my_hist.append(int(i.split(";")[3].split("-")[1]))

print(my_hist)
def bubble_sort(liste):
    n=len(liste)
    print(liste)
    for i in range (n-1,-1,-1):
        for j in range(0,i):
            if not (liste[j]<liste[j+1]):
                temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=temp
    return liste
sıralı=bubble_sort(my_hist)
print(sıralı)

def my_frequency_with_dict(liste):
    frequency_dict={}
    for item in liste:
        if item in frequency_dict.keys():
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
hist=my_frequency_with_dict(sıralı)
print(hist)

son=list(hist.values())


def my_median(liste):
    liste=bubble_sort(liste)
    n=len(liste)

    if n%2==1:
        middle=int(n/2)+1
        median=liste[middle]
    else:
        middle_1 = int(n / 2) - 1
        middle_2 = middle_1 + 1
        median=(liste[middle_1]+liste[middle_2])/2
    return median


def ortalama(liste):
    s,toplam=0,0
    for i in liste:
        s=s+1
        toplam=toplam+i

    mean_=toplam/s

    return mean_

ort=int(ortalama(son))
medyan=my_median(son)


with open(sys.argv[2]+"160401056_hw_2_output.txt","w")as file:
   ## file.write("ortalama=")
    ##file.write(str(my_mean()))
   ## file.write("\n")
   ## file.write("medyan=")
  ## file.write(str(my_median()))
  file.write("ortalama:"+str(ort)+"\n"+"medyan:"+str(medyan))