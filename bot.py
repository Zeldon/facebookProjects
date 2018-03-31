import praw

print('Loading function')

def dssgbot(event, context):

	reddit = praw.Reddit(client_id="9s2cRzgYc_biBw", client_secret="1pVPgcmY2bpeiuBj9AZcZxpPXD4", user_agent="testscript by /u/ryuuzaki82", username='dssgfbbot', password='dssgisth3b3st')
	dssg = reddit.subreddit('datasciencesg')

	print(event)
	
	dssg.submit('fb: ' + event.get('title','no title'), event.get('articlelink','- no url link -') +
                    '\n\n' + event.get('description','- no description -') +
                    '\n\n' + 'postedby: ' + event.get('postedby', '- poster error -')+
                    '\n\n' + 'usermessage: ' + str(event.get('usermsg','- no user message -')) +
                    '\n\n' + 'fb postid: https://www.facebook.com/' + str(event.get('postid','null')))



	return None