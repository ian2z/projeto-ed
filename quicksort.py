def quicksort(alunos, low, high):
    if low < high:
        pi = partition(alunos, low, high)
        quicksort(alunos, low, pi - 1)
        quicksort(alunos, pi + 1, high)

def partition(alunos, low, high):
    pivot = alunos[high].nome.lower()
    i = low - 1
    for j in range(low, high):
        if alunos[j].nome.lower() <= pivot:
            i += 1
            alunos[i], alunos[j] = alunos[j], alunos[i]
    alunos[i + 1], alunos[high] = alunos[high], alunos[i + 1]
    return i + 1