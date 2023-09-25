medida = float(input('uma distancia em metro: '))
cm = medida * 100
mm = medida * 1000
print('a medida de {} corresponde:\n em {:.0f}cm\n em {:.0f}mm. '.format(medida, cm, mm))
