import argparse
import praw
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--graphtoken')
    parser.add_argument('--groupid')
    parser.add_argument('--redditClientID')
    parser.add_argument('--redditSecret')
    parser.add_argument('--redditUserName')
    parser.add_argument('--redditPassword')
    args = parser.parse_args()

    reddit = praw.Reddit(client_id=args.redditClientID,
                         client_secret=args.redditSecret,
                         user_agent="testscript by /u/ryuuzaki82",
                         username=args.redditUserName,
                         password=args.redditPassword)
    print(reddit.user.me())

    feeds = pd.read_csv('linksVideos.csv', encoding='utf-8-sig')

    dssg = reddit.subreddit('datasciencesg')

    for i in range(5):
        # dssg.submit('fb redirect: '+i.article_Title[0], i.article_Link[0] +
        #                 '\n\n'+i.article_Description[0]+
        #                 '\n\n'+'postedby: '+i.postedby[0]+
        #                 '\n\n'+'usermessage: '+str(i.user_Message[0])+
        #                 '\n\n'+'fb postid: https://www.facebook.com/'+str(i.postid[0]))

        dssg.submit('fb: ' + feeds.iloc[i].article_Title, feeds.iloc[i].article_Link +
                    '\n\n' + feeds.iloc[i].article_Description +
                    '\n\n' + 'postedby: ' + feeds.iloc[i].postedby +
                    '\n\n' + 'usermessage: ' + str(feeds.iloc[i].user_Message) +
                    '\n\n' + 'fb postid: https://www.facebook.com/' + str(feeds.iloc[i].postid))

        print 'article id: ' + str(feeds.iloc[i].postid)
        print 'article title: '+ feeds.iloc[i].article_Title.encode("utf-8-sig")

if __name__ == "__main__":
    main()
