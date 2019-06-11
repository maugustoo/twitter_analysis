# import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "1133162248036397057-4nr0ov5wckscIl7qn7VDpc4ZH0qpMZ"
access_token_secret = "pcVwjsXX6rjojG739RN5Xg5bGaqMqiLzNec530a3X8SrT"
consumer_key = "IXqcqpM5dmljm41bAGkhJuspR"
consumer_secret = "C18QoAzAGYeX0CxMlRFBsXS2lJ5BN4Zp6ZTdBTme6sdx6va5Ny"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #lazaro ramos, gilberto gil, preta gil, elisa lucinda, liniker, iza, djamila ribeiro, marielle, Maria Júlia Coutinho
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    terms = ['negraiada', 'negaiada', 'ladr', 'bandid', 'saci', 'racista',
             'racismo', 'escrav', 'senzala', 'neg', 'negr', 'neguin', 'neguim',
             'criol', 'crioul', 'moren', 'morenin', 'morenim', 'preto', 'preta',
             'pixaim', 'pixain', 'macaco', 'macaca', 'urubu', 'cabelo ruim',
             'negra bonita', 'beleza exótica', 'mulat', 'empregadinha', 'africa',
             'nariz', 'beiço', 'denegrir', 'esclarecer', 'crespo', 'cota',
             'morena clara', 'moreno claro']
    #stream.filter(track=terms, languages=['pt'])
    stream.filter(follow=['219112689', '14907774', '35693211', '123358294',
                          '3990050255', '222529351', '2515357319', '54337535',
                          '870678636277399552'], languages=['pt'])
