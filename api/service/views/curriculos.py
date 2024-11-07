from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from common.utils import check_required_fields
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from service.models import Curriculo, Store, Department, Foto
from datetime import datetime


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_curriculos(request):
    if not request.user.groups.filter(name__in=['admin', 'rh']).exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    curriculos = Curriculo.objects.all()
    curriculos_data = []
    for curriculo in curriculos:
        lojas_interesse = []
        setores_interesse = []
        setores_ideal = []
        for loja in curriculo.lojas_interesse.all():
            lojas_interesse.append(
                {'id': loja.id, 'name': loja.name, 'color': loja.color})

        for setor in curriculo.setores_interesse.all():
            setores_interesse.append(
                {'id': setor.id, 'name': setor.name, 'color': setor.color})

        for setor in curriculo.setores_ideal.all():
            setores_ideal.append(
                {'id': setor.id, 'name': setor.name, 'color': setor.color})

        curriculo_data = {
            'id': curriculo.id,
            'apresentacao_curriculo': curriculo.apresentacao_curriculo,
            'apresentacao_pessoal': curriculo.apresentacao_pessoal,
            'apresentacao_observacao': curriculo.apresentacao_observacao,
            'nome': curriculo.nome,
            'data_de_nascimento': curriculo.data_de_nascimento,
            'idade': curriculo.idade,
            'cpf': curriculo.cpf,
            'rg': curriculo.rg,
            'telefone': curriculo.telefone,
            'telefone_adicional': curriculo.telefone_adicional,
            'estado_civil': curriculo.estado_civil,
            'escolaridade': curriculo.escolaridade,
            'possui_cursos_complementares': curriculo.possui_cursos_complementares,
            'cursos_observacao': curriculo.cursos_observacao,
            'possui_dependentes': curriculo.possui_dependentes,
            'numero_dependentes': curriculo.numero_dependentes,
            'observacao_dependentes': curriculo.observacao_dependentes,
            'cep': curriculo.cep,
            'uf': curriculo.uf,
            'cidade': curriculo.cidade,
            'bairro': curriculo.bairro,
            'rua': curriculo.rua,
            'numero': curriculo.numero,
            'complemento': curriculo.complemento,
            'possui_experiencia': curriculo.possui_experiencia,
            'relato_experiencia': curriculo.relato_experiencia,
            'relato_desligamento': curriculo.relato_desligamento,
            'observacao_experiencia': curriculo.observacao_experiencia,
            'relato_motivacao': curriculo.relato_motivacao,
            'lojas_interesse': lojas_interesse,
            'setores_interesse': setores_interesse,
            'relato_interesse': curriculo.relato_interesse,
            'relato_equipe': curriculo.relato_equipe,
            'restricoes_horario': curriculo.restricoes_horario,
            'observacoes_entrevista': curriculo.observacoes_entrevista,
            'entrevistador': curriculo.entrevistador,
            'setores_ideal': setores_ideal,
            'apto_contratacao': curriculo.apto_contratacao,
            'ex_funcionario': curriculo.ex_funcionario,
            'atualmente_contratado': curriculo.atualmente_contratado,
            'observacao': curriculo.observacao,
            'ultima_atualizacao': curriculo.ultima_atualizacao
        }
        
        if(curriculo.curriculo != None):
            curriculo_data['curriculo'] = {'id': curriculo.curriculo.id, 'foto': curriculo.curriculo.foto.url}
            
        if(curriculo.foto != None):
            curriculo_data['foto'] = {'id': curriculo.foto.id, 'foto': curriculo.foto.foto.url}
        
        curriculos_data.append(curriculo_data)

    return Response(curriculos_data, status=200)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_curriculo(request, cpf):
    print(cpf)
    if not request.user.groups.filter(name__in=['admin', 'rh', 'user']).exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    try:
        curriculo = Curriculo.objects.get(
            cpf=cpf)
    except Curriculo.DoesNotExist:
        print(cpf)
        return Response({"error": "Currículo não encontrado."}, status=404)

    lojas_interesse = []
    setores_interesse = []
    setores_ideal = []
    for loja in curriculo.lojas_interesse.all():
        lojas_interesse.append(
            {'id': loja.id, 'name': loja.name, 'color': loja.color})

    for setor in curriculo.setores_interesse.all():
        setores_interesse.append(
            {'id': setor.id, 'name': setor.name, 'color': setor.color})

    for setor in curriculo.setores_ideal.all():
        setores_ideal.append(
            {'id': setor.id, 'name': setor.name, 'color': setor.color})

    curriculo_data = {
        'id': curriculo.id,
        'apresentacao_curriculo': curriculo.apresentacao_curriculo,
        'apresentacao_pessoal': curriculo.apresentacao_pessoal,
        'apresentacao_observacao': curriculo.apresentacao_observacao,
        'nome': curriculo.nome,
        'data_de_nascimento': curriculo.data_de_nascimento,
        'idade': curriculo.idade,
        'cpf': curriculo.cpf,
        'rg': curriculo.rg,
        'telefone': curriculo.telefone,
        'telefone_adicional': curriculo.telefone_adicional,
        'estado_civil': curriculo.estado_civil,
        'escolaridade': curriculo.escolaridade,
        'possui_cursos_complementares': curriculo.possui_cursos_complementares,
        'cursos_observacao': curriculo.cursos_observacao,
        'possui_dependentes': curriculo.possui_dependentes,
        'numero_dependentes': curriculo.numero_dependentes,
        'observacao_dependentes': curriculo.observacao_dependentes,
        'cep': curriculo.cep,
        'uf': curriculo.uf,
        'cidade': curriculo.cidade,
        'bairro': curriculo.bairro,
        'rua': curriculo.rua,
        'numero': curriculo.numero,
        'complemento': curriculo.complemento,
        'possui_experiencia': curriculo.possui_experiencia,
        'relato_experiencia': curriculo.relato_experiencia,
        'relato_desligamento': curriculo.relato_desligamento,
        'observacao_experiencia': curriculo.observacao_experiencia,
        'relato_motivacao': curriculo.relato_motivacao,
        'lojas_interesse': lojas_interesse,
        'setores_interesse': setores_interesse,
        'relato_interesse': curriculo.relato_interesse,
        'relato_equipe': curriculo.relato_equipe,
        'restricoes_horario': curriculo.restricoes_horario,
        'observacoes_entrevista': curriculo.observacoes_entrevista,
        'entrevistador': curriculo.entrevistador,
        'setores_ideal': setores_ideal,
        'apto_contratacao': curriculo.apto_contratacao,
        'ex_funcionario': curriculo.ex_funcionario,
        'atualmente_contratado': curriculo.atualmente_contratado,
        'observacao': curriculo.observacao,
        'ultima_atualizacao': curriculo.ultima_atualizacao
    }
    
    if(curriculo.curriculo != None):
        curriculo_data['curriculo'] = {'id': curriculo.curriculo.id, 'foto': curriculo.curriculo.foto.url}
        
    if(curriculo.foto != None):
        curriculo_data['foto'] = {'id': curriculo.foto.id, 'foto': curriculo.foto.foto.url}

    return Response(curriculo_data, status=200)


@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def import_curriculo(request):

    data = request.data

    cpf = data.get('cpf')
    if Curriculo.objects.filter(cpf=cpf).exists():
        curriculo = Curriculo.objects.get(cpf=cpf)

        curriculo.apresentacao_curriculo = data.get('apresentacao_curriculo')
        curriculo.apresentacao_pessoal = data.get('apresentacao_pessoal')
        curriculo.nome = data.get('nome')
        curriculo.idade = data.get('idade')
        curriculo.telefone = data.get('telefone')
        curriculo.telefone_adicional = data.get('telefone')
        curriculo.data_de_nascimento = '01-01-2000'
        curriculo.estado_civil = data.get('estado_civil')
        curriculo.escolaridade = data.get('escolaridade')
        curriculo.possui_cursos_complementares = data.get(
            'possui_cursos_complementares')
        curriculo.cursos_observacao = data.get('cursos_observacao')
        curriculo.possui_dependentes = data.get('possui_dependentes')
        curriculo.numero_dependentes = data.get('numero_dependentes')
        curriculo.observacao_dependentes = data.get('observacao_dependentes')
        curriculo.cidade = data.get('cidade')
        curriculo.bairro = data.get('bairro')
        curriculo.rua = data.get('rua')
        curriculo.possui_experiencia = data.get('possui_experiencia')
        curriculo.relato_experiencia = data.get('relato_experiencia')
        curriculo.relato_desligamento = data.get('relato_desligamento')
        curriculo.observacao_experiencia = data.get('observacao_experiencia')
        curriculo.relato_motivacao = data.get('relato_motivacao')
        curriculo.relato_interesse = data.get('relato_interesse')
        curriculo.relato_equipe = data.get('relato_equipe')
        curriculo.restricoes_horario = data.get('restricoes_horario')
        curriculo.entrevistador = data.get('entrevistador')
        curriculo.apto_contratacao = data.get('apto_contratacao')
        curriculo.ex_funcionario = data.get('ex_funcionario')
        curriculo.atualmente_contratado = data.get('atualmente_contratado')
        curriculo.ultima_atualizacao = data.get('ultima_atualizacao')
        curriculo.apresentacao_observacao = data.get('apresentacao_observacao')
        curriculo.rg = data.get('rg')
        curriculo.cep = data.get('cep')
        curriculo.uf = data.get('uf')
        curriculo.numero = data.get('numero')
        curriculo.complemento = data.get('complemento')
        curriculo.observacao = data.get('observacao')
        curriculo.observacoes_entrevista = data.get('observacoes_entrevista')

        setores = data.get('setores_interesse')
        setores = setores.split(';')
        for setor in setores:
            formatted_setor = setor.strip().lower()
            formatted_setor = ' '.join(word.capitalize()
                                       for word in formatted_setor.split())

            departamento, created = Department.objects.get_or_create(
                name=formatted_setor)

            if departamento not in curriculo.setores_interesse.all():
                curriculo.setores_interesse.add(departamento)

        curriculo.save()

        return Response({"message": "Curriculo updated successfully."}, status=200)

    else:
        curriculo = Curriculo.objects.create(
            apresentacao_curriculo=data.get('apresentacao_curriculo'),
            apresentacao_pessoal=data.get('apresentacao_pessoal'),
            nome=data.get('nome'),
            idade=data.get('idade'),
            cpf=data.get('cpf'),
            telefone=data.get('telefone'),
            telefone_adicional=data.get('telefone'),
            data_de_nascimento='01-01-2000',
            estado_civil=data.get('estado_civil'),
            escolaridade=data.get('escolaridade'),
            possui_cursos_complementares=data.get(
                'possui_cursos_complementares'),
            cursos_observacao=data.get('cursos_observacao'),
            possui_dependentes=data.get('possui_dependentes'),
            numero_dependentes=data.get('numero_dependentes'),
            observacao_dependentes=data.get('observacao_dependentes'),
            cidade=data.get('cidade'),
            bairro=data.get('bairro'),
            rua=data.get('rua'),
            possui_experiencia=data.get('possui_experiencia'),
            relato_experiencia=data.get('relato_experiencia'),
            relato_desligamento=data.get('relato_desligamento'),
            observacao_experiencia=data.get('observacao_experiencia'),
            relato_motivacao=data.get('relato_motivacao'),
            relato_interesse=data.get('relato_interesse'),
            relato_equipe=data.get('relato_equipe'),
            restricoes_horario=data.get('restricoes_horario'),
            entrevistador=data.get('entrevistador'),
            apto_contratacao=data.get('apto_contratacao'),
            ex_funcionario=data.get('ex_funcionario'),
            atualmente_contratado=data.get('atualmente_contratado'),
            ultima_atualizacao=data.get('ultima_atualizacao'),
            apresentacao_observacao=data.get('apresentacao_observacao'),
            rg=data.get('rg'),
            cep=data.get('cep'),
            uf=data.get('uf'),
            complemento=data.get('complemento'),
            observacao=data.get('observacao'),
            observacoes_entrevista=data.get('observacoes_entrevista')
        )

        setores = data.get('setores_interesse')
        setores = setores.split(';')
        for setor in setores:
            formatted_setor = setor.strip().lower()
            formatted_setor = ' '.join(word.capitalize()
                                       for word in formatted_setor.split())

            departamento, created = Department.objects.get_or_create(
                name=formatted_setor)

            if departamento not in curriculo.setores_interesse.all():
                curriculo.setores_interesse.add(departamento)

        curriculo.save()

        return Response({"message": "Curriculo created successfully."}, status=201)


@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_curriculo(request):
    if not request.user.groups.filter(name__in=['admin', 'rh', 'user']).exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    required_fields = [
        "apresentacao_curriculo",
        "apresentacao_pessoal",
        "nome",
        "data_de_nascimento",
        "idade",
        "cpf",
        "telefone",
        "telefone_adicional",
        "estado_civil",
        "escolaridade",
        "possui_cursos_complementares",
        "cursos_observacao",
        "possui_dependentes",
        "numero_dependentes",
        "observacao_dependentes",
        "cidade",
        "bairro",
        "rua",
        "possui_experiencia",
        "relato_experiencia",
        "relato_desligamento",
        "observacao_experiencia",
        "relato_motivacao",
        "relato_interesse",
        "relato_equipe",
        "restricoes_horario",
        "entrevistador",
        "apto_contratacao",
        "ex_funcionario",
        "atualmente_contratado"
    ]

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    cpf = data.get('cpf')

    if Curriculo.objects.filter(cpf=cpf).exists():
        return Response({"error": "Curriculo already exists."}, status=400)

    curriculo = Curriculo.objects.create(
        apresentacao_curriculo=data.get('apresentacao_curriculo'),
        apresentacao_pessoal=data.get('apresentacao_pessoal'),
        nome=data.get('nome'),
        data_de_nascimento=data.get('data_de_nascimento'),
        idade=data.get('idade'),
        cpf=data.get('cpf'),
        telefone=data.get('telefone'),
        telefone_adicional=data.get('telefone_adicional'),
        estado_civil=data.get('estado_civil'),
        escolaridade=data.get('escolaridade'),
        possui_cursos_complementares=data.get('possui_cursos_complementares'),
        cursos_observacao=data.get('cursos_observacao'),
        possui_dependentes=data.get('possui_dependentes'),
        numero_dependentes=data.get('numero_dependentes'),
        observacao_dependentes=data.get('observacao_dependentes'),
        cidade=data.get('cidade'),
        bairro=data.get('bairro'),
        rua=data.get('rua'),
        possui_experiencia=data.get('possui_experiencia'),
        relato_experiencia=data.get('relato_experiencia'),
        relato_desligamento=data.get('relato_desligamento'),
        observacao_experiencia=data.get('observacao_experiencia'),
        relato_motivacao=data.get('relato_motivacao'),
        relato_interesse=data.get('relato_interesse'),
        relato_equipe=data.get('relato_equipe'),
        restricoes_horario=data.get('restricoes_horario'),
        entrevistador=data.get('entrevistador'),
        apto_contratacao=data.get('apto_contratacao'),
        ex_funcionario=data.get('ex_funcionario'),
        atualmente_contratado=data.get('atualmente_contratado'),
        ultima_atualizacao=datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    )

    if 'lojas_interesse' in data:
        for loja in data.get('lojas_interesse'):
            if not Store.objects.filter(id=loja["id"]).exists():
                return Response({"error": "Store not found."}, status=400)
            else:
                store = Store.objects.filter(id=loja["id"]).first()
                curriculo.lojas_interesse.add(store)
    if 'setores_interesse' in data:
        for setor in data.get('setores_interesse'):
            if not Department.objects.filter(id=setor["id"]).exists():
                return Response({"error": "Department not found."}, status=400)
            else:
                departament = Department.objects.filter(id=setor["id"]).first()
                curriculo.setores_interesse.add(departament)
    if 'setores_ideal' in data:
        for setor in data.get('setores_ideal'):
            if not Department.objects.filter(id=setor["id"]).exists():
                return Response({"error": "Department not found."}, status=400)
            else:
                departament = Department.objects.filter(id=setor["id"]).first()
                curriculo.setores_ideal.add(departament)
                
    if 'foto' in data:
        if not Foto.objects.filter(id=data.get('foto')["id"]).exists():
            return Response({"error": "Foto not found."}, status=400)
        else:
            foto_perfil = Foto.objects.filter(id=data.get('foto')["id"]).first()
            curriculo.foto = foto_perfil
    
    if 'curriculo' in data:
        if not Foto.objects.filter(id=data.get('curriculo')["id"]).exists():
            return Response({"error": "Curriculo not found."}, status=400)
        else:
            foto_curriculo = Foto.objects.filter(id=data.get('curriculo')["id"]).first()
            curriculo.curriculo = foto_curriculo

    curriculo.apresentacao_observacao = data.get(
        'apresentacao_observacao', None)
    curriculo.rg = data.get('rg', None)
    curriculo.cep = data.get('cep', None)
    curriculo.uf = data.get('uf', None)
    curriculo.numero = data.get('numero', None)
    curriculo.complemento = data.get('complemento', None)
    curriculo.observacao = data.get('observacao', None)
    curriculo.observacoes_entrevista = data.get('observacoes_entrevista', None)

    curriculo.save()

    return Response({"message": "Curriculo created successfully."}, status=201)


@api_view(['PUT'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_curriculo(request, cpf):
    if not request.user.groups.filter(name__in=['admin', 'rh', 'user']).exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    required_fields = [
        "apresentacao_curriculo",
        "apresentacao_pessoal",
        "nome",
        "idade",
        "telefone",
        "telefone_adicional",
        "data_de_nascimento",
        "estado_civil",
        "escolaridade",
        "possui_cursos_complementares",
        "cursos_observacao",
        "possui_dependentes",
        "numero_dependentes",
        "observacao_dependentes",
        "cidade",
        "bairro",
        "rua",
        "possui_experiencia",
        "relato_experiencia",
        "relato_desligamento",
        "observacao_experiencia",
        "relato_motivacao",
        "relato_interesse",
        "relato_equipe",
        "restricoes_horario",
        "entrevistador",
        "apto_contratacao",
        "ex_funcionario",
        "atualmente_contratado"
    ]

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    try:
        curriculo = Curriculo.objects.get(cpf=cpf)
    except Curriculo.DoesNotExist:
        return Response({"error": "Curriculo not found."}, status=404)

    curriculo.apresentacao_curriculo = data.get('apresentacao_curriculo')
    curriculo.apresentacao_pessoal = data.get('apresentacao_pessoal')
    curriculo.nome = data.get('nome')
    curriculo.data_de_nascimento = data.get('data_de_nascimento')
    curriculo.idade = data.get('idade')
    curriculo.telefone = data.get('telefone')
    curriculo.telefone_adicional = data.get('telefone_adicional')
    curriculo.estado_civil = data.get('estado_civil')
    curriculo.escolaridade = data.get('escolaridade')
    curriculo.possui_cursos_complementares = data.get(
        'possui_cursos_complementares')
    curriculo.cursos_observacao = data.get('cursos_observacao')
    curriculo.possui_dependentes = data.get('possui_dependentes')
    curriculo.numero_dependentes = data.get('numero_dependentes')
    curriculo.observacao_dependentes = data.get('observacao_dependentes')
    curriculo.cidade = data.get('cidade')
    curriculo.bairro = data.get('bairro')
    curriculo.rua = data.get('rua')
    curriculo.possui_experiencia = data.get('possui_experiencia')
    curriculo.relato_experiencia = data.get('relato_experiencia')
    curriculo.relato_desligamento = data.get('relato_desligamento')
    curriculo.observacao_experiencia = data.get('observacao_experiencia')
    curriculo.relato_motivacao = data.get('relato_motivacao')
    curriculo.relato_interesse = data.get('relato_interesse')
    curriculo.relato_equipe = data.get('relato_equipe')
    curriculo.restricoes_horario = data.get('restricoes_horario')
    curriculo.entrevistador = data.get('entrevistador')
    curriculo.apto_contratacao = data.get('apto_contratacao')
    curriculo.ex_funcionario = data.get('ex_funcionario')
    curriculo.atualmente_contratado = data.get('atualmente_contratado')
    curriculo.ultima_atualizacao = datetime.now().strftime('%m/%d/%Y %H:%M:%S')

    curriculo.lojas_interesse.clear()
    curriculo.setores_interesse.clear()
    curriculo.setores_ideal.clear()
    curriculo.foto = None
    curriculo.curriculo = None
        
    if 'lojas_interesse' in data:
        for loja in data.get('lojas_interesse'):
            if not Store.objects.filter(id=loja["id"]).exists():
                return Response({"error": "Store not found."}, status=400)
            else:
                store = Store.objects.filter(id=loja["id"]).first()
                curriculo.lojas_interesse.add(store)
                
    if 'setores_interesse' in data:
        for setor in data.get('setores_interesse'):
            if not Department.objects.filter(id=setor["id"]).exists():
                return Response({"error": "Department not found."}, status=400)
            else:
                departament = Department.objects.filter(id=setor["id"]).first()
                curriculo.setores_interesse.add(departament)
                
    if 'setores_ideal' in data:
        for setor in data.get('setores_ideal'):
            if not Department.objects.filter(id=setor["id"]).exists():
                return Response({"error": "Department not found."}, status=400)
            else:
                departament = Department.objects.filter(id=setor["id"]).first()
                curriculo.setores_ideal.add(departament)
                
    if 'foto' in data:
        if not Foto.objects.filter(id=data.get('foto')["id"]).exists():
            return Response({"error": "Foto not found."}, status=400)
        else:
            foto_perfil = Foto.objects.filter(id=data.get('foto')["id"]).first()
            curriculo.foto = foto_perfil
    
    if 'curriculo' in data:
        if not Foto.objects.filter(id=data.get('curriculo')["id"]).exists():
            return Response({"error": "Curriculo not found."}, status=400)
        else:
            foto_curriculo = Foto.objects.filter(id=data.get('curriculo')["id"]).first()
            curriculo.curriculo = foto_curriculo

    curriculo.apresentacao_observacao = data.get(
        'apresentacao_observacao', None)
    curriculo.rg = data.get('rg', None)
    curriculo.cep = data.get('cep', None)
    curriculo.uf = data.get('uf', None)
    curriculo.numero = data.get('numero', None)
    curriculo.complemento = data.get('complemento', None)
    curriculo.observacao = data.get('observacao', None)
    curriculo.observacoes_entrevista = data.get('observacoes_entrevista', None)

    curriculo.save()

    return Response({"message": "Curriculo updated successfully."}, status=200)


@api_view(['DELETE'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_curriculo(request, cpf):

    if not request.user.groups.filter(name__in=['admin', 'rh']).exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    try:
        curriculo = Curriculo.objects.get(cpf=cpf)
    except Curriculo.DoesNotExist:
        return Response({"error": "Curriculo not found."}, status=404)

    curriculo.delete()
    return Response({"message": "Curriculo deleted successfully."}, status=200)
