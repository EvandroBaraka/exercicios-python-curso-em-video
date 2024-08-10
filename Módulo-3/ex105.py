def notas(*nota, sit=False):
    n = {}
    n['total'] = len(nota)
    n['maior'] = max(nota)
    n['menor'] = min(nota)
    n['media'] = sum(nota) / len(nota)
    
    if sit:
        if n['media'] >= 7:
            n['situação'] = 'BOA'
        elif n['media'] >= 6:
            n['situação'] = 'RAZOÁVEL'
        else:
            n['situação'] = 'RUIM'
            
    return n
    
    
print('-' * 40)
print(notas(6.5, 5, 6, 7, 7.5, 10, sit=True))
