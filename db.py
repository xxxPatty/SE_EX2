from pymongo import MongoClient

DB = MongoClient('mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net')['testCram']

STUDENT_COLLECTION = DB['student']
TEACHER_COLLECTION = DB['teacher']
BOSS_COLLECTION = DB['boss']

RECHEDULER_COLLECTION = DB['rescheduler']
