def MaxArray(arr):
    if len(arr)==1:
        return arr[0]
    mitad=len(arr)//2
    arr_izq=arr[0:mitad]
    arr_der=arr[mitad:]

    max_izq=MaxArray(arr_izq)
    max_der=MaxArray(arr_der)
    max_mitad=CalcMaxMitad(arr,mitad)
    return max(max_izq,max_der,max_mitad)
def CalcMaxMitad(arr,mitad):
    suma=0
    max_izq=-1000000
    for numero in arr[mitad-1::-1]:
        suma=suma+numero
        if suma>max_izq:
            max_izq=suma
    suma=0
    max_der=-1000000
    for numero in arr[mitad:]:
        suma=suma+numero
        if suma>max_der:
            max_der=suma
    return max_izq+max_der
print(MaxArray([1,2,6,4,2]))
    