from django.db import models


class Materias(models.Model):
    nome_materia = models.CharField(max_length=100)


class Turma(models.Model):
    Serie = models.CharField(max_length=100)
    Periodo = models.CharField(max_length=100)


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    serie = models.ForeignKey(Turma, on_delete= models.CASCADE)
    materias = models.ForeignKey(Materias, null=False, blank=False, on_delete=models.CASCADE)


class NotasAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=False)
    nota = models.DecimalField(max_digits=8, decimal_places=2)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)
