# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClassActivity(models.Model):
    activityid = models.IntegerField(db_column='ActivityId', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='ActivityName', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    activitytype = models.CharField(db_column='ActivityType', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    activitytime = models.DateTimeField(db_column='ActivityTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'class_activity'


class InternetRecord(models.Model):
    internetid = models.IntegerField(db_column='InternetId', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    overtime = models.DateTimeField(db_column='OverTime', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'internet_record'


class StudentConsumption(models.Model):
    consumptionid = models.IntegerField(db_column='ConsumptionId', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'student_consumption'


class StudentDormitory(models.Model):
    dormitoryid = models.IntegerField(db_column='DormitoryId', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime', blank=True, null=True)  # Field name made lowercase.
    leavetime = models.DateTimeField(db_column='LeaveTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'student_dormitory'


class StudentInfo(models.Model):
    sudentid = models.BigIntegerField(db_column='SudentID', primary_key=True)  # Field name made lowercase.
    stufentname = models.CharField(db_column='StufentName', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    admissiondate = models.DateField(db_column='AdmissionDate', blank=True, null=True)  # Field name made lowercase.
    graduationdate = models.DateField(db_column='GraduationDate', blank=True, null=True)  # Field name made lowercase.
    studentnumber = models.BigIntegerField(db_column='StudentNumber', blank=True,
                                           null=True)  # Field name made lowercase.
    homeaddress = models.TextField(db_column='HomeAddress', blank=True, null=True)  # Field name made lowercase.
    native = models.CharField(db_column='Native', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birth = models.DateField(db_column='Birth', blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='Nation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    politicallandscape = models.CharField(db_column='PoliticalLandscape', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase.
    idnumber = models.BigIntegerField(db_column='IdNumber', blank=True, null=True)  # Field name made lowercase.
    phone = models.BigIntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    familyfinances = models.CharField(db_column='FamilyFinances', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    isonlychild = models.IntegerField(db_column='isOnlyChild', blank=True, null=True)  # Field name made lowercase.
    isorphan = models.IntegerField(db_column='isOrphan', blank=True, null=True)  # Field name made lowercase.
    ispreferential = models.IntegerField(db_column='isPreferential', blank=True,
                                         null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='Birthplace', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    healthstatus = models.CharField(db_column='HealthStatus', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    graduatedschool = models.CharField(db_column='GraduatedSchool', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'student_info'


class StudentRp(models.Model):
    rpid = models.IntegerField(db_column='RPId', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    time = models.DateField(blank=True, null=True)
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'student_rp'


class SudentScore(models.Model):
    scoreid = models.BigIntegerField(db_column='ScoreId', primary_key=True)  # Field name made lowercase.
    studentid = models.BigIntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    examtime = models.DateField(db_column='ExamTime', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.BigIntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sudent_score'


class TeacherInfo(models.Model):
    teacherid = models.IntegerField(db_column='TeacherId', primary_key=True)  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(db_column='Education', max_length=255)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    famousrate = models.FloatField(db_column='FamousRate', blank=True, null=True)  # Field name made lowercase.
    firstbatchrate = models.FloatField(db_column='FirstBatchRate', blank=True, null=True)  # Field name made lowercase.
    undergraduaterate = models.FloatField(db_column='UndergraduateRate', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'teacher_info'
