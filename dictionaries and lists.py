addresses = [{'name':'kev','street':'mei avenue','Hse No':'214','city':'naiv'},
             {'name':'felix','street':'mei avenue','Hse No':'234','city':'nairobi'},
             {'name':'kiv','street':'musi avenue','Hse No':'234','city':'mombasa'},
             {'name':'kavv','street':'mui avenue','Hse No':'254','city':'dasani'},
             {'name':'seb','street':'musi avenue','Hse No':'2384','city':'naikuru'},
             {'name':'munga','street':'musi avenue','Hse No':'2384','city':'eldoret'},
             {'name':'muti','street':'moi avenue','Hse No':'214','city':'Kampala'},
             {'name':'asdin','street':'mui avenue','Hse No':'234','city':'Juba'},
             {'name':'dan','street':'mi avenue','Hse No':'2384','city':'Thika'},
             {'name':'kim','street':'mu avenue','Hse No':'234','city':'Meru'}]
count=0
for i in range(len(addresses)):
    y = addresses[i]['street'],addresses[i]['Hse No']
    j = 0
    while j<len(addresses):
        x = addresses[j]['street'],addresses[j]['Hse No']
        if j > i and y == x:
            k =addresses[i]['name']+' and '+addresses[j]['name']
            count+=1
            print(k)
        j =j+1
if count ==0:
    print('no such poeple')

































































































































        




