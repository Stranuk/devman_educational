import smtplib

email_text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''

url = 'dvmn.org'
friend_name = 'Владимир'
my_name = 'Максим'

text = email_text.replace('%website%', url)
text = text.replace('%friend_name%', friend_name)
text = text.replace('%my_name%', my_name)
email_login = "admin@strannuk.ru"
email_password = "#"
email_from = "admin@strannuk.ru"
email_to = "mbogdanov@yandex.ru"
email_subject = "Invite"
email = f'''\
From: {email_from}
To: {email_to}
Subject: {email_subject}
Content-Type: text/plain; charset="UTF-8";


{text}'''


email = email.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')

server.login(email_login, email_password)
server.sendmail(email_from, email_to, email)
server.quit()