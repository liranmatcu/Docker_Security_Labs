git clone https://github.com/liranmatcu/Docker_Security_Labs.git
cd  Docker_Security_Labs/password_strength_estimator

# Start 
docker-compose run --rm pse
score('a-password-of-your-choice')
Example: score('correcthorse')



# Result Scoring (https://github.com/dropbox/zxcvbn#usage)
Integer from 0-4 (useful for implementing a strength bar)
  0 # too guessable: risky password. (guesses < 10^3)

  1 # very guessable: protection from throttled online attacks. (guesses < 10^6)

  2 # somewhat guessable: protection from unthrottled online attacks. (guesses < 10^8)

  3 # safely unguessable: moderate protection from offline slow-hash scenario. (guesses < 10^10)

  4 # very unguessable: strong protection from offline slow-hash scenario. (guesses >= 10^10)


# Exit
press Ctrl+C twice or Ctrl+D or type .exit