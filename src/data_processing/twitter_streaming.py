# import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


class StdOutListener(StreamListener):

    def on_data(self, data):
        return True

    def on_error(self, status):


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')

    terms = ['negraiada', 'negaiada', 'ladr', 'bandid', 'saci', 'racista',
     'racismo', 'escrav', 'senzala', 'neg', 'negr', 'neguin', 'neguim',
     'criol', 'crioul', 'moren', 'morenin', 'morenim', 'preto', 'preta',
     'pixaim', 'pixain', 'macaco', 'macaca', 'urubu', 'cabelo ruim', 'mulat',
     'empregadinha', 'africa', 'nariz', 'beiço', 'crespo', 'cota']


     
    #stream.filter(track=terms, languages=['pt'])
    stream.filter(follow=['219112689', '14907774', '35693211', '123358294',
                          '3990050255', '222529351', '2515357319', '54337535',
                          '870678636277399552'], languages=['pt'], track=terms)
