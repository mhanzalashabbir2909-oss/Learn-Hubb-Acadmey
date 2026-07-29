import os
import traceback

os.chdir(r'd:\Visual code editor\Learning Hub')
from app import app

client = app.test_client()
paths = [
    '/', '/signin', '/signup', '/dashboard', '/olevel-courses.html',
    '/alevel-courses.html', '/phy-ol/phy-ol.html', '/courses.html',
    '/maths-ol.html', '/Computer_Science-ol.html', '/eco-ol.html', 'phy-ol/Book.html', 'templates/courses.html', 'phy-ol/Formula_sheet.html', 'phy-ol/phy-p2 questions.html',
    'phy-ol/Questions/Waves', 'phy-ol/Questions/deformation', 'phy-ol/Questions/temperature', 'phy-ol/Questions/radioactivity', 'phy-ol/Questions/pressure', 'phy-ol/Questions/light', 'phy-ol/Questions/kinematics',
    'phy-ol/Notes/revision_notes', 'phy-ol/Notes/notes', 'phy-ol/Notes/atp_notes', 'Accounting-ol/accounting-ol',
    '/accounting-ol/accounting-ol.html', '/accounting-ol/Notes/revision_notes.html', '/accounting-ol/cath-book.html', '/accounting-ol/frank-book',
    'bus-ol/bus-ol', 'bus-ol/Bus-book', 'bus-ol/Notes_1', 'bus-ol/Notes_2', 'bus-ol/Notes_3',
    'Commerce-ol/commerce-ol', 'Commerce-ol/Book', 'Commerce-ol/Notes', 'Commerce-ol/Notes/1', 'Commerce-ol/Notes/2', 'Commerce-ol/Notes/3', 'Commerce-ol/Notes/4', 'Commerce-ol/Notes/5', 'Commerce-ol/Notes/6', 'Commerce-ol/Notes/7', 'Commerce-ol/Notes/8', 'Commerce-ol/Notes/9',
    'Commerce-ol/Notes/10', 'Commerce-ol/Notes/11', 'Commerce-ol/Notes/12', 'Commerce-ol/Notes/13', 'Commerce-ol/Notes/14', 'Commerce-ol/Notes/15', 
    'CS-ol/Computer_Science-ol','CS-ol/book.html', 'CS-ol/wbook','CS-ol/notes',
    'CS-ol/Notes/Data_Representation','CS-ol/Notes/Hardware', 'CS-ol/Notes/Software' ,'CS-ol/Notes/Uses_of_internet','CS-ol/Notes/AI','CS-ol/Notes/Programming'
    'Eco-ol/eco.ol' ,'Eco-ol/Susan-book', 'Eco-ol/Paul-book', 'Eco-ol/Notes', 'Eco-ol/Quicknotes'
    'isl-ol/islamiat-ol','isl-ol/Hammad','isl-ol/Hammad2','isl-ol/Nighat' 
    ,'Math-ol/maths-ol' ,'Math-ol/Book','Math-ol/p2_topical','Math-ol/Numbers','Math-ol/Co-ordinate_geo'
    , 'Pakstudies-ol/pak-ol.html','Pakstudies-ol/Geo_Book','Pakstudies-ol/History_Book','Pakstudies-ol/hisnotes'
    ,'Pakstudies-ol/history/Section1','Pakstudies-ol/history/Section2','Pakstudies-ol/history/Section3','Pakstudies-ol/history/sec3/early_govt',
    'Pakstudies-ol/history/sec3/ayub','Pakstudies-ol/history/sec3/bangla','Pakstudies-ol/history/sec3/zulfi','Pakstudies-ol/history/sec3/zia'
    ,'Pakstudies-ol/history/sec3/bena','Pakstudies-ol/history/sec3/nawaz','Pakstudies-ol/history/sec3/7mark'
    , 'Pakstudies-ol/geonotes','Pakstudies-ol/geo/1','Pakstudies-ol/geo/2','Pakstudies-ol/geo/3','Pakstudies-ol/geo/4','Pakstudies-ol/geo/5','Pakstudies-ol/geo/6'
    , 'Pakstudies-ol/geo/7','Pakstudies-ol/geo/8','Pakstudies-ol/geo/9','Pakstudies-ol/geo/10','Pakstudies-ol/geo/11_12',
]

for path in paths:
    try:
        res = client.get(path)
        print(path, res.status_code)
    except Exception:
        print('EXCEPTION', path)
        traceback.print_exc()
