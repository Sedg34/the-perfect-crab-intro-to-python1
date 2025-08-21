# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  removed_hyphen = remove_hyphen(words)
  long_words = remove_short_words(removed_hyphen)
  shortened_words = shorten_long_words(long_words)
  return format_report(shortened_words)

def remove_hyphen(words):
  removed_hyphen = []
  for word in words:
    if "-" not in word:
      removed_hyphen.append(word)
  return removed_hyphen

def remove_short_words(words):
  long_words = []
  for word in words:
    if len(word) >=10:
      long_words.append(word)
  return long_words

def shorten_long_words(words):
  shortened_words = []
  for word in words:
    if len(word) >15:
      word = word[0:15] +"..."
      shortened_words.append(word)
    else:
      shortened_words.append(word)
  return shortened_words

def format_report(words):
  report = "These words are quite long: "
  if not words :
    return report
  else:
      for word in words:
        report = report + word + ", "
      return report[0:-2]

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
