def notas(*nota, sit=False):
    """
    => Recebe qualquer quantidade de notas (nota), adiciona em um dicionário, e exibe o dicionário com a quantidade de notas informadas, a maior, a menor e média. Recebe também um parametro sit=True, que adiciona a situação do aluno de acordo com a média.
    :param nota: recebe as notas do aluno
    :param sit: (opcional) exibe a situação do aluno
    :return n: um dicionário com as informações das notas  
    """
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
