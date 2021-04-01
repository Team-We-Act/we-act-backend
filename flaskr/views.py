from flask import Blueprint, render_template

bp = Blueprint('views', __name__, url_prefix='/')

@bp.route('/volunteer_classes')
def hello_volunteer_classes():
  samples = [
    {'country': '필리핀', 'subject1': '아두이노 따라잡기', 'subject2': '포토샵 일러스트 도전해보기'},
    {'country': '우간다', 'subject1': 'MS Office 시작하기', 'subject2': '앱인벤터의 신비함'},
    {'country': '탄자니아', 'subject1': '아두이노 고급', 'subject2': 'AutoCAD란?'},
  ]
  target_sample = {
    'className': '쉽게 배우는 프로그래밍', 
    'countryName': '우간다',
    'language': '영어',
    'duration': '2021년 02월 ~ 2020년 05월',
    'subject': 'C++ 언어'
  };
  lectures_sample = [
    {'title': 'HTML 튜토리얼', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
    {'title': '자바스크립트 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요! 으악 코딩 너무 힘들어요.....'},
    {'title': '타입스크립트 시작하기', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
    {'title': '리액트 프로그래밍 입문', 'description': '웹앱, 웹 표준에 대해 배웁니다! 애니메이션 효과가 모두 적용된 실제 스타벅스 페이지를 똑같이 만들어요!'},
  ]
  # db 의 데이터 query해서 딕셔너리 형식으로 변수
  # all_lectures = firebase_db.child("lectures").get()
  # for lecture in all_lectures.each():
  #   lectures_sample.append(lecture.val())

  return render_template('volunteer_classes.html', 
    contents=samples, 
    target=target_sample,
    lectures=lectures_sample
    )

@bp.route('/create_new_lecture')
def hellp_create_new_class():
  return render_template('create_new_lecture.html')

@bp.route('/recipient_classes')
def hello_recipient_classes():
  lecture_samples = []
  # all_lectures = firebase_db.child("lectures").get()

  # for lecture in all_lectures.each():
    # lecture_samples.append(lecture.val())
  # return render_template('recipient_classes.html', lectures=lecture_samples)
  return render_template('recipient_classes.html')

@bp.route('/lecture_info/<target>')
def get_lecture_by_targe(target):
  # lecture = firebase_db.child("lectures").child(target).get().val()
  # print(lecture)
  # return render_template('lecture_info.html', lecture=lecture)
  return render_template('lecture_info.html')


from .models import Lecture

@bp.route('/register_lecture', methods=['POST'])
def register_lecture():
  if request.method == 'POST':
    data = request.form.to_dict(flat=True)
    lectureTitle = data['title']
    lectureContent = data['contents']
    lectureFile = data['file']
    payload = {'input': lectureContent}
    response = requests.request("POST", url, data=payload)
    firstQA = ""
    print(response)
    if not response.ok == False:
      obj = response.json()
      pushing_data = {
        "title": lectureTitle, 
        "description":lectureContent,
        'question': obj['question']['0'],
        'answer': obj['answer']['0'],
      }
      # firebase_db.child("lectures").child(lectureTitle).set(pushing_data)

    else:
      pushing_data = {
        "title": lectureTitle, 
        "description":lectureContent,
      }
      # firebase_db.child("lectures").child(lectureTitle).set(pushing_data)
    return redirect(url_for('.hello_volunteer_classes'))
  print('fail')

@bp.route('/lectures', methods=['POST'])
def postLectureQuiz():
  title = request.json.get('title')
  content = request.json.get('content')
  className = request.json.get('className')
  lecturer = request.json.get('lecturer')

  if content:
    payload = {'input': content}
    response = requests.request("POST", url, data=payload)
    firstQA = ""
    if not response.ok == False:
      obj = response.json()
      firstQA = {'question': obj['question']['0'],
                 'answer': obj['answer']['0']
                 }
    import re
    if title:
      new_lecture = Lecture(title, content, className, lecturer)
      db.session.add(new_lecture)
      db.session.commit()
      # finalData = str.replace( "//""")
      # new_lecture=new_lecture.toJSONString().replace("\\","")
      return make_response(json.dumps({'lecture':re.sub("\\\\","",new_lecture.toJSONString()),'quiz':firstQA}))

@bp.route('/classes', methods=['POST'])
def postClasses():
  # className=request.form.to_dict('className')
  className=request.json.get('className')
  subject=request.json.get('subject')
  tutorId=request.json.get('tutorId')
  if not (className and subject and tutorId):
    return jsonify({'error':'No arguments'}), 400
  classObj=Classes()
  classObj.className=className
  classObj.subject=subject
  classObj.tutorId=tutorId
  classesList.append(classObj)
  return jsonify(classObj),201
# @app.route(base_url+'classes')
# quiz는 get 