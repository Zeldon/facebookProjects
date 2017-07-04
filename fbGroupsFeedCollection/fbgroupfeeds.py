# This script uses python 3.5 instead of 2.7
# run this script on command line with arguments --graphtoken and --groupid
import argparse
import facebook
import csv
from datetime import datetime
import sys


def main():
    # print command line arguments
    #for arg in sys.argv[1:]:
    #    print(arg)

    parser = argparse.ArgumentParser()
    parser.add_argument('--graphtoken')
    parser.add_argument('--groupid')
    args = parser.parse_args()

    print()
    print("graphtoken: {0}".format(args.graphtoken))
    print("group id: {0}".format(args.groupid))
    print()

    print("By the way please use python 3 instead of 2 for this...")
    print()

    graph = facebook.GraphAPI(
        #access_token='EAACEdEose0cBALGZAUtRBSWNovpkRQO5BH7BTve62LFSQ0WDzZCIeMThvKjpsuzmZBSmDWZCxS9LmOZARoG748mDECor1sMPkpi6XWDY8LNhco61ScMhqZCBT2TEBZCCYE5vJVwkyGF2tfTYlZCFsftbCuaihsZC7SDW0ZCe2n4haUxqyBfwjZBhPZAec6kiKP6Al1oZD',
        access_token=args.graphtoken,
        version='2.9')

    feeds = graph.get_connections(args.groupid,
                                  #'157938781081987',
                                  'feed', fields='from,message,type,name,description,link,caption,created_time,likes')

    # Test print 3 items
    print("test printing 3 line items ...")
    print("...")
    print()
    for i in feeds['data'][:3]:
        print("id : {0}".format(i.get('id', '')))
        print("from : {0}".format(i.get('from', '')))
        print("message : {0}".format(i.get('message', '').encode("UTF-8", "ignore")))
        print("type : {0}".format(i.get('type', '')))
        print("name : {0}".format(i.get('name', '').encode("UTF-8", "ignore")))
        print("description : {0}".format(i.get('description', '').encode("UTF-8", "ignore")))
        print("link : {0}".format(i.get('link', '')))
        print("caption : {0}".format(i.get('caption', '')))
        print("created_time : {0}".format(i.get('created_time', '')))
        print("likes : {0}".format(i.get('likes', '')))
        # for j in i:
        #    print " {0} : {1}".format(j.encode('utf-8', 'ignore'), i[j].encode('utf-8', 'ignore') if isinstance(i[j], str) else i[j])
        print()

    print()
    print("By the way please use python 3 instead of 2 for this...")
    print()

    print()
    print("getting all data ...")
    finaldata = graph.get_all_connections('157938781081987',
                                          'feed', fields='from,message,type,name,description,link,caption,created_time')

    print()
    print("parsing data ...")
    finallist = []
    for i, dat in enumerate(finaldata):
        finallist.append(dat)
        if i % 1000 == 0:
            print("{0} records parsed ...".format(i))

    print()
    # len(finallist)
    # 6793 items as of 4th July 2017 1925hrs
    #finallist[6792]

    print("writing csv ...")
    print()
    f = open('feeds'+datetime.now().strftime("%Y%m%d_%H%MHR")+'.csv','w', newline='')
    fcsv = csv.writer(f)
    fields = ['postid', 'postedby', 'poster_id', 'created_time', 'user_Message',
              'article_type', 'article_Title', 'article_Description', 'article_Source', 'article_Link']

    # write csv file
    fcsv.writerow(fields)

    # parse each row item and write to csv file
    for i, row in enumerate(finallist):
        print(i)
        rowdata = []
        rowdata.append(row.get("id", "")) #postid
        try:
            rowdata.append(row.get("from", "").get("name", "").encode(sys.stdout.encoding, errors='replace')) #postedby
            rowdata.append(row.get("from", "").get("id", ""))  # posted_id

        except:
            rowdata.append("error")
        rowdata.append(row.get("created_time", "")) #created_time
        rowdata.append(row.get("message", "").encode(sys.stdout.encoding, errors='replace')) #user_Message
        rowdata.append(row.get("type", "").encode(sys.stdout.encoding, errors='replace'))  # article_type
        rowdata.append(row.get("name", "").encode(sys.stdout.encoding, errors='replace')) #article_Title
        rowdata.append(row.get("description", "").encode(sys.stdout.encoding, errors='replace')) #article_Description
        rowdata.append(row.get("caption", "")) #article_Source
        rowdata.append(row.get("link", ""))  # article_Link

        fcsv.writerow(rowdata)

    f.close()
    print("End of Data Output Process hehehe...")
    print("Surprise! :D ")

if __name__ == "__main__":
    main()
