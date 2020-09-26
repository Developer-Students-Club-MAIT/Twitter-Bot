# Twitter-Bot
This twitter bot will be associated with DSC MAIT twitter account. Whenever someone tags us with appropriate hashtag and share their experience of any workshop/session they attended, the bot should take the necessay action depending upon the tweet sentiment.

# Workflow
- Every 5 seconds, the bot checks whether there is any updated tweet made. Whenever this action takes place, the tweet id is checked if it has been replied or not. 
- This is done by storing the previous tweet id in a file called last_seen.txt.
- After this verification, the appropriate hastag is checked. 
- After all these checks, tweet sentiment is obtained. Depending on this following actions are taken:
    - If it is a positive sentiment, the tweet is liked and retweeted. 
    - For negative sentiement, the messages the person that why the experience was bad and any feedback they can provide.
    - If the person has direct message privacy issues then no action takes place

# Deployment
5 options are available:
- Heroku
- AWS lambda
- GCP
- Pythonanywhere
- Dockerisation and GitHub actions integrations

Currently I am trying 5th option, i.e, Dockerisation. Anyone interestd in doing other deployment service can make the pull request or contact on slack channel

# Feedbacks and improvemnts
Do give your valuable feedback in the slack channel regarding any issue you are facing, any bug or new features you want to add.
