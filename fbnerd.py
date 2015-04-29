#!/usr/bin/python

# FreshBlookNerd is created by Wasin Thonkaew
# Anything in mind, contact me via twitter @haxpor
#
# Read Readme.md file for more information
# Source code is under MIT License.

import facebook
import sys
import getopt

global_access_token = "CAAXOc4sUIrABABZBGzw6tOaQibJ2yxMkNEDj0du35JGixve4cAbX3bwZA1Iydwuur9OoB2ZAASZBIfhkUjNV5heDGSZBbX1ZBkyYh9bZCcZA4ZCxZBhK6Y1zVyU2dQLxwKR8cHfFtoChgX5iz3EAGpokjgfDZCVZAGqSRpEW33lttP3CuR3ALxxClJfuWEVPlJKuZB4EcxFLdmAytfcFM9E41WNSZB"
global_graph = None

def main(argv):
  global global_graph

  # get api
  global_graph = facebook.GraphAPI(global_access_token)

  optTypeString = None
  isOptTypeEntered = False

  try:
    opts, args = getopt.getopt(argv, "t:m:p:", ["type=", "message=", "path=", "attach_name=", "attach_link=", "attach_caption=", "attach_description=", "attach_picture="])
  except getopt.GetoptError:
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-t", "--type"):
      optTypeString = arg
      isOptTypeEntered = True

  # If user didn't enter -t, then exit immediately
  if isOptTypeEntered == False:
    print "Error: no -t provided"
    sys.exit(2)

  # otherwise, then process according to the type of operation type (-t)
  if optTypeString == "status":
    message = None

    for opt, arg in opts:
      if opt in ("-m", "--message"):
        message = arg

    # Check if all parameters are specified
    if message == None:
      print "Error: -m not specified yet"
      sys.exit(2)

    # Execute
    post_status(message)

  elif optTypeString == "link":
    message = None
    attach_name = ''
    attach_link = ''
    attach_caption = ''
    attach_description = ''
    attach_picture = ''

    # Collect all parameters
    for opt, arg in opts:
      if opt in ("-m", "--message"):
        message = arg
      elif opt in ("--attach_name"):
        attach_name = arg
      elif opt in ("--attach_link"):
        attach_link = arg
      elif opt in ("--attach_caption"):
        attach_caption = arg
      elif opt in ("--attach_description"):
        attach_description = arg
      elif opt in ("--attach_picture"):
        attach_picture = arg

    # Check if all parameters are specified
    if message == None:
      print "Error: -m not specified yet"
      sys.exit(2)
    if attach_link == '':
      print "Error: -atn or --attach_link not specified yet"
      sys.exit(2)

    # Execute
    post_link(message, attach_name, attach_link, attach_caption, attach_description, attach_picture)
    
  elif optTypeString == "photo":
    imagePath = None
    message = None
    
    # Collect all parameters
    for opt, arg in opts:
      if opt in ("-p", "--path"):
        imagePath = arg
      elif opt in ("-m", "--message"):
        message = arg

    # Check if all parameters are specified
    if imagePath == None:
      print "Error: -p not specified yet"
      sys.exit(2)
    if message == None:
      print "Error: -m not specified yet"
      sys.exit(2)

    # Execute
    post_photo(imagePath, message)
  else:
    print "Error: not recognize type of post"
    sys.exit(2)

# Post on user's wall as status
def post_status(statusText):
  print statusText
  global_graph.put_object(parent_object="me", connection_name="feed", message=statusText)

  print "Posted status"
  return

# Post on user's wall as link
def post_link(message, attach_name, attach_link, attach_caption, attach_description, attach_picture):
  attachment = {
    'name' : attach_name,
    'link' : attach_link,
    'caption' : attach_caption,
    'description' : attach_description,
    'picture' : attach_picture
  }

  global_graph.put_wall_post(message=message, attachment=attachment)

  print "Posted link"
  return

# Post on user's wall as photo
def post_photo(imagePath, message):
  global_graph.put_photo(image=open(imagePath), message=message)

  print "Posted a photo"
  return

if __name__ == "__main__":
  main(sys.argv[1:])