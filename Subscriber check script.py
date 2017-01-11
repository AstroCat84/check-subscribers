import praw

def send_message(user_to_send,subr,client_id,client_secret,username,password):
    """
    Takes the name of a redditor and a subreddits name and pm's the redittor the subscriber count of the subreddit.
    
    :params:
    user_to_send//String// : Name of the redittor to whom the message has to be sent
    subr//String// : Name of the subreddit whose subscriber count has to be sent. Don't add '/r/'
    client_id,client_secret//String//: OAuth credentials required by reddit.Visit "https://www.reddit.com/prefs/apps/" to obtain one
    username//String//: Your reddit username
    password//String//: Your reddit password
    
    :return:
    Bool value True if Message was sent successfully,False otherwise
    """
    try:
        reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='Personal Message botfor Subscriber count by /u/             MrAnthem',username=username,password=password)
      
        s = reddit.subreddit(subr).subscribers
    
        reddit.redditor(user_to_send).message('Subscriber count',"Hello {0} the number of subscribers for /r/{1} is: {2}".format(user_to_send,subr,s))
        return True

    #TODO: Implement a better error catching method
    except:
        return False


if '__main__' == __name__:
    user_to_send = input("Enter the username to whom you wish to send a message")
    subr = input("Enter the subreddit to count the users for")
    client_id = input("Enter your clientid")
    client_secret = input("Enter your client secret")
    username = input("Enter your username")
    password = input("Enter your password")
    status = send_message(user_to_send,subr,client_id,client_secret,username,password)
    
    if status:
        print("Message was sent successfully")
    else:
        print("Something went wrong,please check if you have entered all the details correctly and try again")

