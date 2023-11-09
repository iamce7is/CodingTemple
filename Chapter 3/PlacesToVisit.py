Visit = ['Japan', 'New York', 'Brazil', 'Miami', 'Italy']
print(Visit)

print(sorted(Visit))
print(Visit)

Visit.reverse()
print(Visit)

Visit.reverse()
print(Visit)

print(sorted(Visit))

Visit.sort(reverse=False)
print(Visit)

Visit.sort(reverse=True)
print(Visit)

Peaks = ['Popocateptl', 'Mt. Fuji', 'Mt Everest', 'Mt. Saint Helens']
print(Peaks[0])
print(Peaks[1])
print(Peaks[2])
print(Peaks[3])
Peaks.append('Shoshone')
print(Peaks)
Peaks.insert(0, 'Cerro')
print(Peaks)

PoppedPeak = Peaks.pop()
print(Peaks)

print(PoppedPeak)

print(Peaks)
Peaks.reverse()
print(Peaks)
Peaks.sort()
print(Peaks)

Peaks.insert(0, 'Shoshone')
print(Peaks)

Peaks.remove('Shoshone')
print(Peaks)

print(len(Peaks))
