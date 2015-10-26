import praw
r = praw.Reddit(user_agent='Test PM Script by /u/mewkyy')
r.login('mewkyy', 'PASSWORD')
r.send_message('haekuh', 'test!', 'You are awesome!')
