from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    name = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False, default="info")


class Department(models.Model):
    name = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False, default="info")


class Foto(models.Model):
    foto = models.ImageField(upload_to='images/')


class Curriculo(models.Model):
    apresentacao_curriculo = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    curriculo = models.OneToOneField(
        Foto, on_delete=models.CASCADE, blank=True, null=True, related_name="foto_curriculo")
    apresentacao_pessoal = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    foto = models.OneToOneField(
        Foto, on_delete=models.CASCADE, blank=True, null=True, related_name="foto_perfil")
    apresentacao_observacao = models.CharField(max_length=500)
    nome = models.CharField(max_length=220, blank=False)
    data_de_nascimento = models.CharField(
        max_length=100, blank=False)
    idade = models.IntegerField(blank=False)
    cpf = models.CharField(max_length=20, blank=False)
    rg = models.CharField(max_length=15)
    telefone = models.CharField(max_length=20, blank=False)
    telefone_adicional = models.CharField(max_length=20, blank=False)
    estado_civil = models.CharField(max_length=100, blank=False)
    escolaridade = models.CharField(max_length=100, blank=False)
    possui_cursos_complementares = models.BooleanField(blank=False)
    cursos_observacao = models.CharField(max_length=500, blank=False)
    possui_dependentes = models.BooleanField(blank=False)
    numero_dependentes = models.IntegerField(blank=False)
    observacao_dependentes = models.CharField(max_length=500, blank=False)
    cep = models.CharField(max_length=20)
    uf = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200, blank=False)
    bairro = models.CharField(max_length=200, blank=False)
    rua = models.CharField(max_length=300, blank=False)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=300)
    possui_experiencia = models.BooleanField(blank=False)
    relato_experiencia = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    relato_desligamento = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    observacao_experiencia = models.CharField(max_length=500, blank=False)
    relato_motivacao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    lojas_interesse = models.ManyToManyField(
        Store, related_name="curriculo_lojas_interesse")
    setores_interesse = models.ManyToManyField(
        Department, related_name="curriculo_setores_interesse")
    relato_interesse = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    relato_equipe = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    restricoes_horario = models.BooleanField(blank=False)
    observacoes_entrevista = models.CharField(max_length=500)
    entrevistador = models.CharField(max_length=220, blank=False)
    setores_ideal = models.ManyToManyField(
        Department, related_name="curriculo_setores_ideal")
    apto_contratacao = models.BooleanField(blank=False)
    ex_funcionario = models.BooleanField(blank=False)
    atualmente_contratado = models.BooleanField(blank=False)
    observacao = models.CharField(max_length=500)
    ultima_atualizacao = models.CharField(max_length=100)
