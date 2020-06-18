import telepot
from parsing import*
from loading import*
import telegram
import time

TOKEN = '1135530839:AAGK-02uBO0TZQzKaNs6fa7ZS_UqvSKh3M4'
CHAT_ID = '1259659704'
USER_NAME = 'kpu_script_2020_jobSearching_bot'
FIRST_NAME = '취업, 어디까지 알아봤니'

datas = Data()

quit = False

firstMessage = "안녕하세요. 취업, 어디까지 알아봤니 봇입니다. \n" \
               "찾으시는 학과를 입력해주세요. "
secondMessage = " 다음 명령어 중에서 입력해 주세요." \
                     " \n\t 1. 학교검색 2. 학과정보 3. 취업정보\n" \
                "학과를 재검색을 원하시면 학과 이름을 입력해주세요"
bot = telepot.Bot(TOKEN)

curHandle = 0

def Send(message):
    bot.sendMessage(CHAT_ID,message)

def SendUniversityData():
    uniNamdStr = ""
    for uni in datas.UniDict:
        uniNamdStr += uni +'\n'
    Send("해당 학과가 있는 학교 목록입니다")
    Send(uniNamdStr)

def SendMajorData():
    majorStr = "학과이름 : " + datas.majorData.major + "\n\n"
    majorStr += "학과 계열  : " + datas.majorData.subject + '\n\n'
    majorStr += "세부 관련 학과 : " + datas.majorData.department + '\n\n'
    majorStr += "주요 과목 : " + datas.majorData.main_subjects  + '\n\n'
    majorStr += "졸업 후 취업분야 : " + datas.majorData.graduates + '\n\n'
    majorStr += "성비\n\t 남자 : " + datas.majorData.gender["남자"] + '\n\t 여자: ' + datas.majorData.gender["여자"]

    Send("학과정보입니다")
    Send(majorStr)

def SendJobData():
    jobStr = "취업률\n\t"
    for i in datas.jobData.employmentRate:
        jobStr += '\t' +i + " : " + datas.jobData.employmentRate[i] +'\n'
    jobStr += "\n임금\n\t"
    for i in datas.jobData.salary:
        jobStr += '\t' +i + " : " + datas.jobData.salary[i] + '\n'
    jobStr+= "\n첫 직장 만족도\n\t"
    for i in datas.jobData.satisfaction:
        jobStr += '\t' +i + " : " + datas.jobData.satisfaction[i] + '\n'
    jobStr += "\n졸업 후 상황\n"
    for i in datas.jobData.afterGraduation:
        jobStr += '\t' + i + " : " + datas.jobData.afterGraduation[i] + '\n'
    jobStr+= "\n관련 직업 : " + datas.jobData.job + '\n\n'
    jobStr += "관련 자격 : " + datas.jobData.qualification

    Send("취업정보입니다")
    Send(jobStr)

def handle(msg):
    global quit
    if quit:
        return

    # 학과정보를 입력받는다
    global bot, datas

    contentType , chatType, chatId = telepot.glance(msg)
    if contentType != 'text':
        Send("텍스트로 입력해주세요")
        return

    if msg['text'] == "학교검색":
        SendUniversityData()
        Send(secondMessage)
    elif msg['text'] == "학과정보":
        SendMajorData()
        Send(secondMessage)
    elif msg['text'] == "취업정보":
        SendJobData()
        Send(secondMessage)
    elif msg['text'] == '/start' or msg['text'] =="야" or msg['text'] == "시작" or msg['text'] =="재시작" or msg['text'] =="hey":
        Send(firstMessage)
    elif msg['text'] == "바보" or msg['text'] =="멍청이" or msg['text'] =="ㅗ" or msg['text'] == '멍청아' or msg['text'] == '바보야':
        Send("말씀이 너무 지나치시네요! 봇을 종료하겠습니다")
        quit = True
    elif msg['text'] == '김정윤':
        Send("그 변태는 왜찾으시죠?? 불쾌해졌어요. 저 갈래요")
        quit = True
    elif msg['text'] == "김유림" or msg['text'] == "정진선":
        Send("오셨습니까!!! 형님!!!!")
    else:
        Send("잠시만 기다려주세요...")
        try:
             datas.MakeUniversityData(msg['text'])
        except KeyError:
            Send("해당 학과/명령어 가 존재하지 않습니다.")
            return
        datas.MakeMajorData()
        datas.MakeJobData()
        Send(secondMessage)


bot.message_loop(handle)
while True:
    time.sleep(10)



