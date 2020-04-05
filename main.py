import twint
from datetime import datetime
if datetime.now().strftime('%I %p') == '12 AM':
    output_name = input("Name of the outputted text file: ")
    content = input('Word to look for in tweet (Zoom or Zoom ID are good ones): ')
    time = datetime.now().strftime('%Y-%m-%d 00:00:00')
    c = twint.Config()
    c.Search = content
    c.Since = str(time)
    c.Output = output_name + '.txt'
    twint.run.Search(c)
    print("SHOWING ALL TWEETS SINCE 12 AM")
else:
    hours = int(input("How many hours behind to look for (1 is better because zooms don't last long will break if its 12 AM if it is 12 AM then input '0'): "))
    output_name = input("Name of the outputted text file: ")
    content = input('Word to look for in tweet (Zoom or Zoom ID are good ones): ')
    hour = int(datetime.now().strftime('%I')) - hours
    time = datetime.now().strftime('%Y-%m-%d {}:%M:%S'.format(hour))  
    c = twint.Config()
    c.Search = content
    c.Since = str(time)
    c.Output = output_name + '.txt'
    twint.run.Search(c)
