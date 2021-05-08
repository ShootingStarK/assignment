import random
import time

purchase = int(input("구매할 장 수를 입력하세요 : "))
lists = [[]for i in range(purchase)]

num = random.randint(1,45)

for i in range(purchase):
    for j in range(6):
        while num in lists[i]:
            num = random.randint(1,45)
        lists[i].append(num)


for i in range(purchase):
    lists[i].sort()
    print(lists[i])
now = time.localtime()
print("%04d/%02d/%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))

win_number =[]
for i in range(6):
    while num in win_number:
        num = random.randint(1,45)
    win_number.append(num)
win_number.sort()

sec_number = random.randint(1,45)
while sec_number in win_number:
    sec_number = random.randint(1,45)
print("당첨 번호 : ", end = " ")
print(win_number, end=" ")
print(sec_number)

is_winner =[[]for i in range(purchase)]
for i in range(purchase):
    is_winner[i] = list(set(lists[i]).intersection(win_number))

count1 = count2 = count3 = count4 = count5 = 0
for i in range(purchase):
    if len(is_winner[i]) == 6:
        print("1등")
        count1 += 1
    elif len(is_winner[i]) == 5 and sec_number in is_winner[i]:
        print("2등")
        count2 += 1
    elif len(is_winner[i]) == 5:
        print("3등")
        count3 += 1
    elif len(is_winner[i]) == 4:
        print("4등")
        count4 += 1
    elif len(is_winner[i]) == 3:
        print("5등")
        count5 += 1
    else:
        print("당첨되지 않았음/맞은 숫자 : {0}개".format(len(is_winner[i])))

print("1등:{0}번 2등:{1}번 3등:{2}번 4등:{3}번 5등:{4}번".format(count1, count2, count3, count4, count5))



# 4 사이트 회원가입
# 회원가입을 위해서 id 비밀번호 email 이름 을 입력받고 이를 데이터로 저장
# 아이디 및 email은 저장된 데이터들과 비교하여 중복여부를 확인
# 비밀번호는 특수문자 대문자 소문자 숫자를 모두 포함한 8자리 이상으로 이루어져야함
# 추가점수 : 비밀번호 재입력 확인, 회원탈퇴 기능

import re

def passwordcheck(pwd):
    if len(pwd) < 8:
        print("비밀번호는 최소 8자리 이상이어야 합니다")
        return False

    elif re.search("[0-9]+", pwd) is None:
        print("비밀번호는 최소 1개 이상의 숫자를 포함해야 합니다")
        return False

    elif re.search("[A-Z]+", pwd) is None:
        print("비밀번호는 최소 1개 이상의 대문자를 포함해야 합니다")
        return False

    elif re.search("[a-z]+", pwd) is None:
        print("비밀번호는 최소 1개 이상의 소문자를 포함해야 합니다")
        return False

    elif re.search("[`~!@#$%^&*(),<.>/?]+", pwd) is None:
        print("비밀번호는 최소 1개 이상의 특수문자를 포함해야 합니다")
        return False
    
    else:
        print("가능한 비밀번호입니다")
        return True

id_list=[]
password_list=[]
email_list=[]
name_list=[]
while True:
    id = input("생성할 id를 입력하세요: ")
    while id in id_list:
        print("이미 해당 id가 있습니다. 다른 id를 만들어주세요")
        id = input("생성할 id를 입력하세요: ")
    id_list.append(id)

    password = input("비밀 번호를 입력하세요 : ")
    while passwordcheck(password) == False:
        password = input("비밀 번호를 입력하세요:")
    password_again = input("비밀 번호 확인 : ")
    while password != password_again:
        print("입력한 비밀 번호가 다릅니다. 다시 입력하세요.")  
        password_again = input("비밀 번호 확인 : ")
    print("비밀번호가 일치합니다")
    password_list.append(password)

    email = input("email을 입력하세요 : ")
    while email in email_list:
        print("이미 해당 email이 있습니다. 다른 email을 입력해주세요")
        email = input("email을 입력하세요 : ")
    email_list.append(email)

    name = input("이름을 입력하세요 : ")
    name_list.append(name)
    # print(id_list, password_list, email_list, name_list)
    
    classify_num = input("프로그램을 종료하시려면 0번, 회원탈퇴를 하시려면 1번, 새로운 회원가입을 원하시면 아무 키를 입력해주세요 : ")
    if classify_num == '0':
        break
    elif classify_num == '1': 
        while True:
            withdraw_id = input("탈퇴하시려는 id를 입력하세요 : ")
            if withdraw_id in id_list:
                id_list.remove(withdraw_id)
            else:
                print("없는 아이디입니다. 아이디를 다시 입력하세요")
                continue
            withdraw_password = input("탈퇴하려는 id의 비밀번호를 입력하세요 : ")
            if withdraw_password in password_list:
                password_list.remove(withdraw_password)
            else:
                print("비밀번호가 일치하지 않습니다. 처음부터 다시 입력해주세요")
                id_list.append(withdraw_id)
                continue
            withdraw_email = input("가입할 때 사용한 email을 입력하세요 : ")
            if withdraw_email in email_list:
                email_list.remove(withdraw_email)
            else:
                print("이메일이 일치하지 않습니다. 처음부터 다시 입력해주세요")
                id_list.append(withdraw_id)
                password_list.append(withdraw_password)
                continue
            withdraw_name = input("사용하던 이름을 입력하세요 : ")
            if withdraw_name in name_list:
                name_list.remove(withdraw_name)
                break
            else:
                print("이름이 일치하지않습니다. 처음부터 다시 입력해주세요")
                id_list.append(withdraw_id)
                password_list.append(withdraw_password)
                email_list.append(withdraw_email)
                continue
        print("회원 탈퇴가 완료되었습니다")
        # print(id_list, password_list, email_list, name_list)
        classify_num2 = input("프로그램을 종료하시려면 0번, 다시 회원가입을 원하시면 아무 키를 입력해주세요 : ")
        if classify_num2 == '0':
            break
            
        else:
            pass
    else:
        pass
    